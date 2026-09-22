#!/usr/bin/env python3
"""The bundled example is a project the chain accepts, and its round is the record it claims.

WHY. The example is the answer key. If it drifts from what the gate accepts, a new person
copies a shape that fails. So this reads example/consulting-site with the gate's own functions:
init.verify finds nothing missing, load_config resolves from inside the round, every anchor
matches its owner live, vision_problems is clean against the round's real brief, and the gate's
passive `status` reports every page COMPLETE.

THE ROUND IS WITHDRAWN, on purpose. Its manifest carries `status: withdrawn` with the founder's
reason, so the seal leaves it alone ("nothing to seal, no receipt written") and a copy of it
cannot be resealed into something else. It also predates several gates (brief-reads, the reader
gate, the exemplar floor), so the CURRENT chain would refuse it if the status were cleared, and
that refusal names those gates. The RESEAL test below does exactly that on a copy, with the real
producers (playwright, node, the vendored detector), and asserts the refusal rather than a seal:
the producers ran, the chain read the result, and the gate said no for the right reasons. It
runs only under DESIGN_CHAIN_RESEAL=1, never on the example itself.
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
ROUND = EXAMPLE / "design" / "2026-09-18"
GATE = SCRIPTS / "design-chain-gate.py"


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

    def gate(self, *args, timeout=1800):
        r = subprocess.run([sys.executable, str(GATE), *args], capture_output=True, text=True,
                           env=self.env, timeout=timeout)
        return r.returncode, r.stdout + r.stderr

    def test_init_finds_nothing_missing(self):
        init = load(SCRIPTS / "init.py", "init_for_example")
        self.assertEqual(init.verify(EXAMPLE), [])

    def test_the_gate_reads_the_example(self):
        gate = load(GATE, "gate_for_example")
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
        # the round sits beside references/, which is where the gap producer looks for captures
        self.assertEqual(cfg["rounds_dir"], "design")
        self.assertTrue((ROUND.parent / "references" / "NARRATIVE.md").is_file())

    def test_status_reports_every_page_complete(self):
        rc, out = self.gate("status", str(ROUND))
        pages = sorted(p.name for p in ROUND.glob("*-laptop.html"))
        self.assertEqual(len(pages), 3, pages)
        for p in pages:
            self.assertIn(f"{p}: COMPLETE", out, out)

    def test_the_round_is_withdrawn_with_a_reason_and_seal_leaves_it_alone(self):
        man = json.loads((ROUND / "craft-manifest.json").read_text())
        self.assertEqual(man.get("status"), "withdrawn")
        self.assertTrue(str(man.get("reason", "")).strip(), "a withdrawn round says why")
        tmp = Path(tempfile.mkdtemp(prefix="dcex-copy-"))
        self.addCleanup(shutil.rmtree, tmp, True)
        copy = tmp / "consulting-site"
        shutil.copytree(EXAMPLE, copy)
        rd = copy / "design" / "2026-09-18"
        before = (rd / "receipts.json").read_bytes()
        rc, out = self.gate("seal", str(rd), timeout=300)
        self.assertEqual(rc, 0, out)
        self.assertIn("withdrawn", out.lower())
        self.assertEqual((rd / "receipts.json").read_bytes(), before, "seal rewrote a withdrawn round's receipt")

    def test_the_example_carries_the_scrub_placeholders(self):
        # client names were replaced by "Client A".. before the example shipped; the placeholders
        # are the visible trace of that, and an owner file without them was copied unscrubbed
        owners = EXAMPLE / "design" / "owners"
        text = "".join(p.read_text() for p in owners.glob("*.md"))
        self.assertIn("Client A", text)
        self.assertIn("Client B", text)

    @unittest.skipUnless(os.environ.get("DESIGN_CHAIN_RESEAL") == "1",
                         "set DESIGN_CHAIN_RESEAL=1 with playwright, chromium and node installed")
    def test_the_producers_run_on_a_copy_and_the_current_chain_refuses_the_old_round(self):
        tmp = Path(tempfile.mkdtemp(prefix="dcex-copy-"))
        self.addCleanup(shutil.rmtree, tmp, True)
        copy = tmp / "consulting-site"
        shutil.copytree(EXAMPLE, copy)
        rd = copy / "design" / "2026-09-18"
        mp = rd / "craft-manifest.json"
        man = json.loads(mp.read_text())
        man.pop("status", None)
        man.pop("reason", None)
        mp.write_text(json.dumps(man, indent=1) + "\n")
        (rd / "receipts.json").unlink()
        rc, out = self.gate("seal", str(rd))
        self.assertEqual(rc, 2, out)
        # every producer ran: the seal logs one timed line per stage
        for stage in ("stage standard", "stage gap", "stage impeccable", "stage check:tripwire"):
            self.assertIn(stage, out, out)
        # and the refusal is the current chain's, naming the gates this 2026-09-18 round predates
        self.assertIn("brief-reads", out)
        self.assertIn("reader", out.lower())
        self.assertNotIn("Traceback", out)


if __name__ == "__main__":
    unittest.main()
