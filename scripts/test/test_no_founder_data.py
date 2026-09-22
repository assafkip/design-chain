#!/usr/bin/env python3
"""The tool carries nobody's identity.

WHY. This chain was extracted from one person's working repo, where the scripts' docstrings
quoted him by name, cited his issue tracker, and pointed at paths on his machine. A public
tool that names its author's clients, domain or home directory in its code is leaking on
every install. So every file of the TOOL is swept for a denylist, and a hit fails.

SCOPE, deliberately. The sweep covers scripts/, hooks/, commands/, skills/, templates/, docs/
and the repo root. It does NOT cover example/: the bundled example is a real product site,
by decision, and its vision, persona and canon are that product's on purpose. Nor vendor/,
which is third-party code under its own license.

Two patterns look like hits and are not: the leak DETECTORS in test_dc_dependency_census.py
and test_dc_fixture_redaction.py carry the bare string "/Users/" so they can refuse a real
path, so the path pattern here needs a username after it.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SWEPT_DIRS = ("scripts", "hooks", "commands", "skills", "templates", "docs")
SKIPPED_DIRS = {"example", "vendor", ".git", "__pycache__", "node_modules"}
TEXT_SUFFIXES = {".py", ".json", ".md", ".sh", ".txt", ".html", ".css", ".js", ".mjs", ".yml", ".yaml", ".toml"}

# Anything that identifies the original author, their business, their clients, their issue
# tracker or their machine. Extend it when a new identity leaks; never narrow it to pass.
DENYLIST = [
    # a public GitHub path (assafkip/<repo>) is an install source, the one allowed use of the handle:
    # this plugin's own repo, and the marketplace four of the engines come from
    (re.compile(r"assaf(?!kip/[a-z0-9-]+)", re.I), "the author's name"),
    (re.compile(r"kipnis", re.I), "the author's name"),
    (re.compile(r"askconsulting", re.I), "the author's business"),
    (re.compile(r"ktlyst", re.I), "the author's other business"),
    (re.compile(r"\bASK-\d+\b"), "the author's issue tracker"),
    # the private repos and the instance layout; the kipi marketplace itself is public and is
    # named as an engine source, so "kipi-system" as a marketplace path is not on this list
    (re.compile(r"cole-gtm|q-consult|q-system", re.I), "the author's other repos"),
    (re.compile(r"/Users/[a-z]"), "a path on the author's machine"),
    (re.compile(r"\b(thaena|norri|prodigy gold|pure spectrum|all points)\b", re.I), "the author's clients"),
]


ATTRIBUTION = {".claude-plugin/plugin.json", "LICENSE"}   # authorship is attribution, not a leak


def swept_files():
    files = [p for p in ROOT.iterdir() if p.is_file() and p.suffix in TEXT_SUFFIXES]
    for d in SWEPT_DIRS:
        base = ROOT / d
        if not base.is_dir():
            continue
        for p in base.rglob("*"):
            if p.is_file() and p.suffix in TEXT_SUFFIXES and not (set(p.relative_to(ROOT).parts) & SKIPPED_DIRS):
                files.append(p)
    return files


class NoFounderData(unittest.TestCase):
    def test_no_identifying_string_in_the_tool(self):
        hits = []
        for p in swept_files():
            if p.name == Path(__file__).name or str(p.relative_to(ROOT)) in ATTRIBUTION:
                continue
            for i, line in enumerate(p.read_text(errors="replace").splitlines(), 1):
                for pat, why in DENYLIST:
                    if pat.search(line):
                        hits.append(f"{p.relative_to(ROOT)}:{i}: {why}: {line.strip()[:100]}")
        self.assertEqual(hits, [], "\n" + "\n".join(hits))

    def test_the_sweep_sees_the_tool(self):
        names = {p.name for p in swept_files()}
        for must in ("design-chain-gate.py", "design-engine-door.py", "hooks.json", "round.md", "init.md", "README.md"):
            self.assertIn(must, names, f"{must} is outside the sweep")

    def test_the_sweep_would_catch_a_leak(self):
        # a negative control: the sweep is only evidence if it can fail
        sample = "see /Users/someone/projects/x and ticket " + "ASK-" + "1234"
        self.assertTrue(any(p.search(sample) for p, _ in DENYLIST))


if __name__ == "__main__":
    unittest.main()
