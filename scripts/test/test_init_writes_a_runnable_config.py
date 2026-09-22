#!/usr/bin/env python3
"""init writes inputs the gate accepts, from the example answers alone.

WHY. The wizard is the front door. If what it writes is not what design-chain-gate.py reads, a
new person's first round fails on files a tool wrote for them, which is worse than no tool. So
this drives init.py from the bundled example answers (the ones every question shows) in a temp
project, then reads the result with the GATE's own functions: load_config finds the config from
a page inside the rounds dir, vision_problems accepts a brief that quotes the vision, the anchor
regexes match their owner files live, and check_readers accepts the readers block.

Temp directories only; nothing here touches a live project.
"""
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent
INIT = SCRIPTS / "init.py"
GATE = SCRIPTS / "design-chain-gate.py"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def example_answers() -> dict:
    qs = json.loads(subprocess.run([sys.executable, str(INIT), "--print-questions"],
                                   capture_output=True, text=True, check=True).stdout)
    return {q["key"]: q["example"] for q in qs}


class InitWritesARunnableConfig(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="dcinit-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.project = self.tmp / "proj"
        self.answers = self.tmp / "answers.json"
        self.answers.write_text(json.dumps(example_answers()))

    def run_init(self, *extra):
        return subprocess.run([sys.executable, str(INIT), str(self.project), "--answers", str(self.answers), *extra],
                              capture_output=True, text=True)

    def test_the_example_answers_produce_a_complete_project(self):
        r = self.run_init()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("every input the chain needs is in place", r.stdout)
        for rel in ("design-chain.json", "design/VISION.md", "design/owners/buyer.md", "design/owners/the-idea.md",
                    "design/owners/not-this.md", "design/references/exemplars.json", "design/references/NARRATIVE.md"):
            self.assertTrue((self.project / rel).is_file(), rel)

    def test_the_gate_reads_what_init_wrote(self):
        self.assertEqual(self.run_init().returncode, 0)
        gate = load(GATE, "gate_for_init_test")
        cfg = json.loads((self.project / "design-chain.json").read_text())
        # every anchor matches its owner file live, the way chain_problems reads them
        for own in cfg["owners"]:
            text = (self.project / own["file"]).read_text()
            for anc in own["anchors"]:
                self.assertTrue(re.search(anc, text, re.M), f"{anc!r} in {own['file']}")
        # a round inside rounds_dir finds this config and no other
        rd = self.project / cfg["rounds_dir"] / "2026-01-01"
        rd.mkdir(parents=True)
        page = rd / "Home-laptop.html"
        page.write_text("<html><body><p>x</p></body></html>")
        found, cfg_path = gate.load_config(page)
        self.assertEqual(cfg_path, self.project / "design-chain.json")
        self.assertEqual(found["project"], cfg["project"])
        # the vision stage: a brief quoting one vision line verbatim passes; none quoted is named
        vision = (self.project / "design/VISION.md").read_text()
        quoted = next(ln for ln in vision.splitlines() if ln.startswith("**Founder"))
        (rd / "brief.md").write_text("# brief\n\nparaphrase only\n")
        probs = gate.vision_problems(rd, cfg, cfg_path)
        self.assertTrue(any("quotes no line" in p for p in probs), probs)
        (rd / "brief.md").write_text("# brief\n\n" + quoted + "\n")
        self.assertEqual(gate.vision_problems(rd, cfg, cfg_path), [])
        # the readers block is one the reader gate accepts, and its persona is an owner
        reader = load(SCRIPTS / "design-reader-gate.py", "reader_for_init_test")
        reader.check_readers(cfg["readers"])
        self.assertIn(cfg["readers"]["persona_file"], {o["file"] for o in cfg["owners"]})
        self.assertIsNone(reader.persona_owner_problem(cfg, self.project, rd))
        # the checks block names only checks the gate runs
        names, why = gate.declared_checks(cfg)
        self.assertIsNone(why)
        self.assertEqual(names, ["tripwire"])

    def test_init_never_overwrites_a_project(self):
        self.assertEqual(self.run_init().returncode, 0)
        before = (self.project / "design/VISION.md").read_text()
        r = self.run_init()
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertIn("already exists", r.stderr)
        self.assertEqual((self.project / "design/VISION.md").read_text(), before)

    def test_thin_answers_are_refused_by_name(self):
        a = example_answers()
        a["vision"] = a["vision"][:2]           # the gate wants three founder blocks
        a["exemplars"] = ["not a url"]
        self.answers.write_text(json.dumps(a))
        r = self.run_init()
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertIn("vision: 3 or more", r.stderr)
        self.assertIn("not a URL", r.stderr)
        self.assertFalse(self.project.exists(), "a refused init wrote files anyway")

    def test_every_exemplar_host_is_in_the_narrative(self):
        a = example_answers()
        a["narrative_each"] = a["narrative_each"][:1]     # the person only wrote about one site
        self.answers.write_text(json.dumps(a))
        r = self.run_init()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)     # init fills a placeholder heading
        nar = (self.project / "design/references/NARRATIVE.md").read_text()
        for u in a["exemplars"]:
            self.assertIn(u.split("//")[1], nar)
        self.assertIn("not yet read", nar)


if __name__ == "__main__":
    unittest.main()
