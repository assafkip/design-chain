#!/usr/bin/env python3
"""The doctor tells a stranger what is missing and where it comes from.

Scans a fake ~/.claude under a temp dir (DESIGN_CHAIN_CLAUDE_HOME), never the real one.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent
DOCTOR = SCRIPTS / "doctor.py"
ENGINES = json.loads((SCRIPTS / "design-engines.json").read_text())["engines"]


class Doctor(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="dcdoc-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.home = self.tmp / "claude-home"
        self.home.mkdir()

    def run_doctor(self, *args):
        env = {**os.environ, "DESIGN_CHAIN_CLAUDE_HOME": str(self.home)}
        r = subprocess.run([sys.executable, str(DOCTOR), *args], capture_output=True, text=True, env=env)
        return r.returncode, r.stdout + r.stderr

    def test_every_engine_names_where_it_comes_from(self):
        for e in ENGINES:
            self.assertTrue(e.get("source", "").strip(), f"{e['skill']} has no source")

    def test_an_empty_machine_is_told_what_is_missing_and_where(self):
        rc, out = self.run_doctor("--json")
        r = json.loads(out)
        # the only engine that can be present on an empty machine is the one this plugin ships
        present = {row["skill"] for row in r["engines"] if row["installed"]}
        self.assertLessEqual(present, {"design-room"})
        rc, out = self.run_doctor()
        self.assertIn("not installed: marketplace anthropics/claude-code", out)   # frontend-design's source
        self.assertIn("not installed: the hyperframes project", out)

    def test_a_personal_skill_and_a_marketplace_skill_are_both_found(self):
        (self.home / "skills" / "frontend-design").mkdir(parents=True)
        (self.home / "skills" / "frontend-design" / "SKILL.md").write_text("---\nname: frontend-design\n---\n")
        mp = self.home / "plugins" / "marketplaces" / "acme" / "plugins" / "acme-design" / "skills" / "ui-ux-pro-max"
        mp.mkdir(parents=True)
        (mp / "SKILL.md").write_text("---\nname: ui-ux-pro-max\n---\n")
        rc, out = self.run_doctor("--json")
        rows = {row["skill"]: row for row in json.loads(out)["engines"]}
        self.assertTrue(rows["frontend-design"]["installed"])
        self.assertIn("personal", rows["frontend-design"]["where"])
        self.assertTrue(rows["ui-ux-pro-max"]["installed"])
        self.assertIn("marketplace acme", rows["ui-ux-pro-max"]["where"])
        self.assertIn("plugin acme-design", rows["ui-ux-pro-max"]["where"])

    def test_exit_code_follows_the_site_lane_and_the_runtime(self):
        rc, out = self.run_doctor("--json")
        r = json.loads(out)
        want = 0 if (all(v["ok"] for v in r["runtime"].values()) and r["site_lane_has_an_engine"]) else 1
        self.assertEqual(rc, want, out)


if __name__ == "__main__":
    unittest.main()
