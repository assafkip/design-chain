#!/usr/bin/env python3
"""The bundled example is a project the chain accepts, and its round reads as sealed.

WHY. The example is the answer key. If it drifts from what the gate accepts, a new person
copies a shape that fails. So this reads example/consulting-site with the gate's own functions:
init.verify finds nothing missing, load_config resolves from inside the round, every anchor
matches its owner live, vision_problems is clean against the round's real brief, and the gate's
passive `status` reports every page COMPLETE.

A full RESEAL (playwright, chromium, node, and `claude -p` for the readers) is the stronger
proof and runs only when DESIGN_CHAIN_RESEAL=1 is set, on a COPY of the example under a temp
directory, never on the example itself. CI sets it where those are installed.
"""
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent
ROOT = SCRIPTS.parent
EXAMPLE = ROOT / "example" / "consulting-site"
ROUND = EXAMPLE / "design" / "rounds" / "2026-09-18"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TheExampleIsAnAnswerKey(unittest.TestCase):
    def setUp(self):
        self.state = Path(tempfile.mkdtemp(prefix="dcex-state-"))
        self.addCleanup(shutil.rmtree, self.state, True)
        self.env = {**os.environ, "DESIGN_CHAIN_STATE": str(self.state)}

    def test_init_finds_nothing_missing(self):
        init = load(SCRIPTS / "init.py", "init_for_example")
        self.assertEqual(init.verify(EXAMPLE), [])

    def test_the_gate_reads_the_example(self):
        gate = load(SCRIPTS / "design-chain-gate.py", "gate_for_example")
        cfg = json.loads((EXAMPLE / "design-chain.json").read_text())
        found, cfg_path = gate.load_config(ROUND / "D1-astro-laptop.html")
        self.assertEqual(cfg_path, EXAMPLE / "design-chain.json")
        for own in cfg["owners"]:
            text = (EXAMPLE / own["file"]).read_text()
            for anc in own["anchors"]:
                self.assertTrue(re.search(anc, text, re.M), f"{anc!r} in {own['file']}")
        self.assertEqual(gate.vision_problems(ROUND, cfg, cfg_path), [])
        names, why = gate.declared_checks(cfg)
        self.assertIsNone(why)
        reader = load(SCRIPTS / "design-reader-gate.py", "reader_for_example")
        reader.check_readers(cfg["readers"])
        self.assertIsNone(reader.persona_owner_problem(cfg, EXAMPLE, ROUND))

    def test_status_reports_every_page_complete(self):
        r = subprocess.run([sys.executable, str(SCRIPTS / "design-chain-gate.py"), "status", str(ROUND)],
                           capture_output=True, text=True, env=self.env)
        out = r.stdout + r.stderr
        pages = sorted(p.name for p in ROUND.glob("*-laptop.html"))
        self.assertEqual(len(pages), 3, pages)
        for p in pages:
            self.assertIn(f"{p}: COMPLETE", out, out)

    def test_the_example_carries_the_scrub_placeholders(self):
        # client names were replaced by "Client A".. before the example shipped; the placeholders
        # are the visible trace of that, and an owner file without them was copied unscrubbed
        owners = EXAMPLE / "design" / "owners"
        text = "".join(p.read_text() for p in owners.glob("*.md"))
        self.assertIn("Client A", text)
        self.assertIn("Client B", text)

    @unittest.skipUnless(os.environ.get("DESIGN_CHAIN_RESEAL") == "1",
                         "set DESIGN_CHAIN_RESEAL=1 with playwright, chromium, node and claude installed")
    def test_the_example_reseals_on_a_copy(self):
        tmp = Path(tempfile.mkdtemp(prefix="dcex-copy-"))
        self.addCleanup(shutil.rmtree, tmp, True)
        copy = tmp / "consulting-site"
        shutil.copytree(EXAMPLE, copy)
        rd = copy / "design" / "rounds" / "2026-09-18"
        r = subprocess.run([sys.executable, str(SCRIPTS / "design-chain-gate.py"), "seal", str(rd)],
                           capture_output=True, text=True, env=self.env, timeout=1800)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue((rd / "receipts.json").is_file())


if __name__ == "__main__":
    unittest.main()
