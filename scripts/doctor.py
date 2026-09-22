#!/usr/bin/env python3
"""design-chain doctor: what this machine has, what a round will need, and where to get the rest.

WHY. The build step of a round calls design ENGINES: skills the door gates and records, none of
which ship in this repo. A stranger who installed the plugin would reach step 4, call one, and
meet a refusal about a tool they never heard of. So this says, before any round, which engines
are installed, which are not, and where each comes from (docs/ENGINES.md holds the same table).
It also checks the three runtime needs: playwright with chromium, node, and the claude CLI.

    python3 doctor.py            the report
    python3 doctor.py --json     the same, as JSON (init and the command read this)

Exit 0 when the runtime is complete and at least one site-lane engine is installed; 1 otherwise.
Nothing here installs anything.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENGINES = HERE / "design-engines.json"
import os
# DESIGN_CHAIN_CLAUDE_HOME points the scan at another ~/.claude, for tests
CLAUDE = Path(os.environ.get("DESIGN_CHAIN_CLAUDE_HOME") or (Path.home() / ".claude"))


def installed_skills() -> dict[str, str]:
    """{skill name: where it lives} for every SKILL.md Claude Code can load on this machine:
    personal skills, and every plugin under every marketplace clone."""
    found: dict[str, str] = {}
    personal = CLAUDE / "skills"
    if personal.is_dir():
        for p in personal.glob("*/SKILL.md"):
            found.setdefault(p.parent.name, "personal (~/.claude/skills)")
    mps = CLAUDE / "plugins" / "marketplaces"
    if mps.is_dir():
        remotes: dict[str, str] = {}
        for p in mps.glob("*/**/skills/*/SKILL.md"):
            rel = p.relative_to(mps).parts
            mp = rel[0]
            if mp not in remotes:
                r = subprocess.run(["git", "-C", str(mps / mp), "remote", "get-url", "origin"],
                                   capture_output=True, text=True)
                url = r.stdout.strip().removesuffix(".git").replace("https://github.com/", "github.com/") if r.returncode == 0 else ""
                remotes[mp] = f" ({url})" if url else ""
            found.setdefault(p.parent.name, f"marketplace {mp}{remotes[mp]}, plugin {rel[-4] if len(rel) >= 4 else '?'}")
    # a plugin's own skills, when this repo is loaded with --plugin-dir
    for p in (HERE.parent / "skills").glob("*/SKILL.md"):
        found.setdefault(p.parent.name, "this plugin")
    return found


def runtime() -> dict[str, dict]:
    out = {}
    try:
        import playwright  # noqa: F401
        ok = True
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as pw:
                b = pw.chromium.launch()
                b.close()
            detail = "playwright with chromium"
        except Exception as e:  # missing browser binary is the common case
            ok = False
            detail = f"playwright is installed but chromium is not: run `playwright install chromium` ({type(e).__name__})"
    except ImportError:
        ok, detail = False, "pip install playwright && playwright install chromium"
    out["playwright"] = {"ok": ok, "detail": detail}
    try:
        import PIL  # noqa: F401
        out["Pillow"] = {"ok": True, "detail": "installed"}
    except ImportError:
        out["Pillow"] = {"ok": False, "detail": "pip install Pillow"}
    node = shutil.which("node")
    if node:
        v = subprocess.run([node, "--version"], capture_output=True, text=True).stdout.strip()
        major = int(v.lstrip("v").split(".")[0]) if v.lstrip("v").split(".")[0].isdigit() else 0
        out["node"] = {"ok": major >= 18, "detail": v if major >= 18 else f"{v}; 18 or newer is needed"}
    else:
        out["node"] = {"ok": False, "detail": "install Node 18 or newer (the anti-pattern detector)"}
    claude = shutil.which("claude")
    out["claude"] = {"ok": bool(claude), "detail": claude or "the Claude Code CLI is not on PATH (the reader gate runs `claude -p`)"}
    det = HERE.parent / "vendor" / "impeccable" / "detector" / "detect-antipatterns.mjs"
    out["impeccable"] = {"ok": det.is_file(), "detail": str(det) if det.is_file() else "vendor/impeccable is missing from this checkout"}
    return out


def report() -> dict:
    engines = json.loads(ENGINES.read_text())["engines"]
    have = installed_skills()
    rows = []
    for e in engines:
        rows.append({"skill": e["skill"], "lane": e["lane"], "stage": e["stage"], "source": e.get("source", ""),
                     "installed": e["skill"] in have, "where": have.get(e["skill"])})
    rt = runtime()
    site_ok = any(r["installed"] for r in rows if r["lane"] == "site")
    return {"runtime": rt, "engines": rows,
            "ok": all(v["ok"] for v in rt.values()) and site_ok,
            "site_lane_has_an_engine": site_ok}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    r = report()
    if a.json:
        print(json.dumps(r, indent=1))
        return 0 if r["ok"] else 1
    print("runtime")
    for k, v in r["runtime"].items():
        print(f"  {'ok ' if v['ok'] else 'NO '} {k:<11} {v['detail']}")
    print("\nengines (the build step calls these; the door records each run)")
    by_lane: dict[str, list] = {}
    for row in r["engines"]:
        by_lane.setdefault(row["lane"], []).append(row)
    for lane, rows in by_lane.items():
        print(f"  {lane}")
        for row in rows:
            mark = "ok " if row["installed"] else "-- "
            print(f"    {mark} {row['skill']:<26} {row['where'] or 'not installed: ' + (row['source'] or 'see docs/ENGINES.md')}")
    missing = [row["skill"] for row in r["engines"] if not row["installed"]]
    print()
    if not r["site_lane_has_an_engine"]:
        print("no site-lane engine is installed: a round can be briefed and measured, but the build step has "
              "nothing to call. docs/ENGINES.md says where each one comes from.")
    elif missing:
        print(f"{len(missing)} engine(s) not installed; a round only needs the ones its lane uses. "
              "docs/ENGINES.md says where each one comes from.")
    else:
        print("every listed engine is installed.")
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
