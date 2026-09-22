#!/usr/bin/env python3
"""design-chain init: the seven questions, and the files the chain needs written from the answers.

WHY. The chain refuses a round whose inputs are missing, and it refuses well: it names the file.
What it cannot do is TELL SOMEONE NEW what to put in that file, and a tool whose first hour is
reading a gate's refusals one at a time is a tool nobody adopts. So this asks, in order, and
writes each file the moment the answer is in. Every question shows an example answer. Nothing
here judges an answer; the seal judges the round.

    python3 init.py [project-dir]                       ask on the terminal
    python3 init.py [project-dir] --answers answers.json   the same, from a file (what the
                                                          /design-chain-init command does after
                                                          asking in conversation)
    ... --capture       also capture the exemplars now (needs playwright) and derive the standard
    ... --print-questions   the questions as JSON, for whoever asks them

Writes, relative to the project dir:
    design-chain.json                 the config the gate reads (load_config walks up to it)
    design/VISION.md                  vision_problems(): dated founder blocks with quoted words
    design/owners/buyer.md            an owner AND readers.persona_file: the buyer, in their words
    design/owners/the-idea.md         an owner: the one sentence the page repeats
    design/owners/not-this.md         an owner: what it must not look like, with reasons
    design/references/exemplars.json  the roster design-exemplar-capture.py reads (append-only)
    design/references/NARRATIVE.md    the human read of the group (craft.require_grounding)
    design/exemplars/                 the captures directions.md must cite (exemplars_dir)
    design/specs/, design/rounds/     empty, for the chain to fill

It then checks what it wrote the way the gate will: every anchor regex matches its owner file
live, the vision has enough founder blocks, the persona is an owner, the narrative names every
exemplar host. Those are the inputs; the seal is still the only verdict on a round.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
TODAY = _dt.date.today().isoformat()

# The questions, in the order they are asked. `key` is the answers.json field. `many` means a
# list of lines. `example` is what a blank prompt shows, so nobody stares at nothing.
QUESTIONS = [
    {"key": "project", "many": False,
     "ask": "What is the product, in one line? (the config's project name is derived from it)",
     "example": "Ledgerline, invoicing for freelance designers"},
    {"key": "vision", "many": True, "min": 3,
     "ask": "What is the page trying to BE? Three or more sentences in YOUR words, verbatim, one per line. "
            "Not constraints, not features: what a visitor should understand and feel.",
     "example": ["They need to hit the site and immediately understand how I can help them.",
                 "These are professionals looking to alleviate a pain. Treat them that way, and be impressive.",
                 "Nobody should have to play around on the site to find the point."]},
    {"key": "buyer", "many": False,
     "ask": "Who arrives? One paragraph: their role, their day, the moment they land on this page.",
     "example": "A freelance designer with six clients, invoicing from a spreadsheet at 11pm, who just "
                "got paid late for the third time this quarter."},
    {"key": "buyer_words", "many": True, "min": 3,
     "ask": "Three or more phrases the buyer ACTUALLY said, from calls, tickets, reviews or posts. One per "
            "line, their words, not yours. The first one becomes a brief anchor the gate checks verbatim.",
     "example": ["I spend Sunday night chasing invoices instead of designing.",
                 "I never know which client owes me what.",
                 "The tool I tried made me set up a whole accounting system first."]},
    {"key": "idea", "many": False,
     "ask": "The one idea. One sentence the whole page repeats.",
     "example": "Every invoice knows whether it has been paid, so you never have to ask."},
    {"key": "not_this", "many": True, "min": 1,
     "ask": "What must it NOT look like? One per line, each with a reason after a colon.",
     "example": ["A generic SaaS template: every competitor already looks like that.",
                 "A dashboard screenshot as the hero: the buyer does not want a dashboard, they want to be paid."]},
    {"key": "exemplars", "many": True, "min": 3,
     "ask": "Three to six sites you admire, one URL per line. They are captured and measured, and the "
            "standard is derived from them, so pick pages you would be proud to sit beside.",
     "example": ["https://stripe.com", "https://linear.app", "https://calendly.com"]},
    {"key": "narrative_shared", "many": False,
     "ask": "Looking at those sites together: what do they SHARE? One paragraph.",
     "example": "One idea per screen, a real product image in the first fold, generous space, a single "
                "accent colour that means one thing, and copy that names the reader's situation."},
    {"key": "narrative_each", "many": True, "min": 1,
     "ask": "What does each one do that the others do not? One line per site, starting with its host "
            "(stripe.com: ...).",
     "example": ["stripe.com: the gradient is a signature, not decoration, and it never touches type.",
                 "linear.app: motion carries the product story; nothing on the page is static for long.",
                 "calendly.com: the headline is the whole offer in six words."]},
    {"key": "narrative_ours", "many": False,
     "ask": "Which of that applies to YOUR page, and which does not? One paragraph. This becomes the "
            "first craft requirements, so be concrete.",
     "example": "The product image in the first fold applies: show the invoice. The signature gradient "
                "does not: our accent is one flat colour. Motion applies only to the one number that changes."},
    {"key": "labels", "many": True, "min": 2,
     "ask": "What might a stranger think this page is selling? Two to five short labels, one per line; the "
            "first is the right answer. Readers are asked to pick one, and the seal reads their pick.",
     "example": ["invoicing for freelancers", "accounting software", "a design agency"]},
    {"key": "signal", "many": False, "optional": True,
     "ask": "The one signal colour, as a hex, or blank. It may mean one thing on the page and nothing else.",
     "example": "#0066b3"},
]


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.casefold()).strip("-")[:40] or "project"


def host(url: str) -> str:
    return (urlparse(url.strip()).netloc or url.strip()).removeprefix("www.")


def ask_terminal() -> dict:
    out = {}
    for q in QUESTIONS:
        print("\n" + q["ask"])
        ex = q["example"]
        print("  example: " + (" / ".join(ex) if isinstance(ex, list) else ex))
        if q["many"]:
            print("  (one per line; an empty line ends the list)")
            lines = []
            while True:
                try:
                    ln = input("  > ").strip()
                except EOFError:
                    ln = ""
                if not ln:
                    if len(lines) >= q.get("min", 1) or q.get("optional"):
                        break
                    print(f"  {q.get('min', 1)} or more needed")
                    continue
                lines.append(ln)
            out[q["key"]] = lines
        else:
            while True:
                try:
                    v = input("  > ").strip()
                except EOFError:
                    v = ""
                if v or q.get("optional"):
                    break
                print("  an answer is needed")
            out[q["key"]] = v
    return out


def check_answers(a: dict) -> list[str]:
    probs = []
    for q in QUESTIONS:
        v = a.get(q["key"])
        if q["many"]:
            if not isinstance(v, list) or not all(isinstance(x, str) and x.strip() for x in v):
                probs.append(f"{q['key']}: a list of non-empty lines is needed")
            elif len(v) < q.get("min", 1):
                probs.append(f"{q['key']}: {q.get('min', 1)} or more lines are needed, got {len(v)}")
        elif not q.get("optional") and not (isinstance(v, str) and v.strip()):
            probs.append(f"{q['key']}: an answer is needed")
    for u in a.get("exemplars", []) if isinstance(a.get("exemplars"), list) else []:
        if not re.match(r"^https?://\S+$", u.strip()):
            probs.append(f"exemplars: {u!r} is not a URL")
    sig = (a.get("signal") or "").strip()
    if sig and not re.match(r"^#[0-9a-fA-F]{6}$", sig):
        probs.append(f"signal: {sig!r} is not a six-digit hex colour")
    return probs


def anchor_for(line: str) -> str:
    """A regex that matches this line at the start of a line, verbatim."""
    return "^" + re.escape(line.strip())


def write(project: Path, a: dict) -> dict:
    """Write every input file. Returns {relative path: what it is} for the report."""
    d = project / "design"
    for sub in ("owners", "references", "exemplars", "specs", "rounds"):
        (d / sub).mkdir(parents=True, exist_ok=True)
    wrote = {}
    name = slug(a["project"])

    # VISION.md: FOUNDER_QUOTE_RE wants a line naming the founder, a colon, then a quote mark
    vision = ["# " + a["project"].strip() + ": vision", "",
              "Running notebook. Your words, dated, kept verbatim. `design-chain-gate.py` (vision_problems)",
              "reads this before any round can brief: it needs the founder blocks below, and every brief",
              "has to quote one of them word for word.", "", "---", ""]
    for line in a["vision"]:
        vision += [f"**Founder, {TODAY}:** \"{line.strip().strip(chr(34))}\"", ""]
    (d / "VISION.md").write_text("\n".join(vision))
    wrote["design/VISION.md"] = "the vision, in the founder's words"

    # owners: buyer.md is both an owner and the reader persona, so the anchor is the buyer's first phrase
    buyer_lines = ["# The buyer", "", a["buyer"].strip(), "", "## In their own words", ""]
    for w in a["buyer_words"]:
        buyer_lines += [f"> \"{w.strip().strip(chr(34))}\"", ""]
    buyer_lines += ["## For a reader role-playing this person", "",
                    "You are the person described above. You have the problems in the quotes. Judge the",
                    "page only as this person would, from what is on the screen.", ""]
    (d / "owners" / "buyer.md").write_text("\n".join(buyer_lines))
    wrote["design/owners/buyer.md"] = "the buyer, their words, and the reader persona"

    idea_lines = ["# The one idea", "", f"**{a['idea'].strip().rstrip('.')}.**", "",
                  "The sentence the whole page repeats. A screen that does not say it is off the page.", ""]
    (d / "owners" / "the-idea.md").write_text("\n".join(idea_lines))
    wrote["design/owners/the-idea.md"] = "the one idea"

    not_lines = ["# Not this", "", "What the page must not look like, each with its reason.", ""]
    for n in a["not_this"]:
        not_lines.append(f"- {n.strip()}")
    not_lines.append("")
    (d / "owners" / "not-this.md").write_text("\n".join(not_lines))
    wrote["design/owners/not-this.md"] = "what it must not look like"

    # exemplars roster (append-only through the capture script; init only creates it)
    ex_path = d / "references" / "exemplars.json"
    if not ex_path.is_file():
        ex_path.write_text(json.dumps({"exemplars": [{"url": u.strip(), "added": TODAY} for u in a["exemplars"]],
                                       "_dropped": []}, indent=2) + "\n")
        wrote["design/references/exemplars.json"] = "the exemplar roster"

    # NARRATIVE.md: one heading per host, so the gate finds every exemplar in it
    nar = ["# The exemplar group: what defines it", "", "The human half of the grounding. `MEASUREMENTS.md`",
           "is regenerated by `design-exemplar-capture.py`; this file is written by a person and every",
           "technique in a craft manifest must cite it. Re-read the group every time an exemplar is added.",
           "", "## What they share", "", a["narrative_shared"].strip(), "", "## Each one, on its own", ""]
    each = {ln.split(":", 1)[0].strip().removeprefix("www."): ln.split(":", 1)[1].strip() if ":" in ln else ""
            for ln in a["narrative_each"]}
    for u in a["exemplars"]:
        h = host(u)
        nar += [f"### {h}", "", each.get(h) or "(not yet read: write what this site does that the others do not)", ""]
    nar += ["## What applies to this page, and what does not", "", a["narrative_ours"].strip(), ""]
    (d / "references" / "NARRATIVE.md").write_text("\n".join(nar))
    wrote["design/references/NARRATIVE.md"] = "the narrative of the group"

    labels = [x.strip() for x in a["labels"]]
    sig = (a.get("signal") or "").strip() or "#0066b3"
    cfg = {
        "project": name,
        "_what": "Design-chain config. Every brief must quote each anchor VERBATIM, read live from the owner "
                 "files below. Paraphrase fails. If an owner file changes, yesterday's brief fails.",
        "rounds_dir": "design/rounds",
        "exemplars_dir": "design/exemplars",
        "owners": [
            {"file": "design/owners/buyer.md", "anchors": [anchor_for(f"> \"{a['buyer_words'][0].strip().strip(chr(34))}\"")]},
            {"file": "design/owners/the-idea.md", "anchors": [anchor_for(f"**{a['idea'].strip().rstrip('.')}.**")]},
            {"file": "design/owners/not-this.md", "anchors": [anchor_for(f"- {a['not_this'][0].strip()}")]},
        ],
        "standard": {
            "_source": "Starting floors. `design-standard-from-exemplars.py design-chain.json --apply` "
                       "re-derives them from the captured exemplars and records what moved and why.",
            "max_type_sizes": 5, "max_large_elements": 4, "large_px": 40, "max_words": 80,
            "min_body_px": 15, "max_line_chars": 90, "signal": sig, "max_signal_elements": 2,
            "viewports": [[1440, 900], [390, 844]],
            "hero_align": "center", "hero_center_tolerance_pct": 5,
            "max_hero_pieces": 2, "max_hero_words": 18, "max_hero_lines": 3,
        },
        "craft": {
            "_what": "The BAR half. The standard above is a FLOOR: it measures counts and the absence of "
                     "AI-default tells and cannot see craft. These switches make a wireframe non-compliant.",
            "tier": "craft",
            "require_craft_manifest": True,
            "require_impeccable": True,
            "min_asset_elements": 1,
            "min_animated_elements": 1,
            "require_grounding": "design/references/NARRATIVE.md",
            "require_dispositions": True,
            "require_fresh_brief": True,
            "require_gap_check": True,
        },
        "vision": {
            "file": "design/VISION.md",
            "specs_dir": "design/specs",
            "min_founder_quotes": 3,
            "require_brief_quotes_vision": True,
        },
        "readers": {
            "_what": "Fresh model readers role-play the buyer against the served page. persona_file must be "
                     "one of the owners. labels: what a stranger might think is sold; the first is right.",
            "persona_file": "design/owners/buyer.md",
            "labels": labels,
            "n": 3,
            "floor": 1.0,
            "viewports": [[1440, 900]],
        },
        "checks": [{"name": "tripwire"}],
    }
    (project / "design-chain.json").write_text(json.dumps(cfg, indent=1) + "\n")
    wrote["design-chain.json"] = "the config the gate reads"
    return wrote


def verify(project: Path) -> list[str]:
    """The inputs, checked the way the gate reads them. [] means a round can be briefed."""
    probs = []
    cfg_path = project / "design-chain.json"
    try:
        cfg = json.loads(cfg_path.read_text())
    except (OSError, ValueError) as e:
        return [f"design-chain.json: {e}"]
    for own in cfg.get("owners", []):
        f = project / own["file"]
        if not f.is_file():
            probs.append(f"owner {own['file']} is missing")
            continue
        text = f.read_text()
        for anc in own.get("anchors", []):
            if not re.search(anc, text, re.M):
                probs.append(f"anchor {anc!r} matches nothing in {own['file']}")
    vf = project / cfg["vision"]["file"]
    quote_re = re.compile(r"(?im)^\s*[*_>\s-]*Founder[^\n:]*:\s*.*?[\"“‘']")
    n = len(quote_re.findall(vf.read_text())) if vf.is_file() else 0
    if n < cfg["vision"]["min_founder_quotes"]:
        probs.append(f"{cfg['vision']['file']} carries {n} founder block(s); {cfg['vision']['min_founder_quotes']} needed")
    pf = cfg["readers"]["persona_file"]
    if pf not in {o["file"] for o in cfg.get("owners", [])}:
        probs.append(f"readers.persona_file {pf} is not an owner")
    ground = project / cfg["craft"]["require_grounding"]
    roster = ground.parent / "exemplars.json"
    if not roster.is_file():
        probs.append("design/references/exemplars.json is missing")
    else:
        hosts = [host(e["url"]) for e in json.loads(roster.read_text()).get("exemplars", [])]
        if not hosts:
            probs.append("the exemplar roster is empty")
        ntext = ground.read_text() if ground.is_file() else ""
        for h in hosts:
            if h not in ntext:
                probs.append(f"NARRATIVE.md does not mention {h}")
    # the gate's own reading of the readers block, if it is beside us
    gate = HERE / "design-reader-gate.py"
    if gate.is_file():
        import importlib.util
        spec = importlib.util.spec_from_file_location("drg_for_init", gate)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
            mod.check_readers(cfg["readers"])
        except ValueError as e:
            probs.append(f"readers block: {e}")
        except Exception:
            pass
    return probs


def capture(project: Path) -> list[str]:
    """Capture the exemplars and derive the standard; the messages to show."""
    msgs = []
    refs = project / "design" / "references"
    r = subprocess.run([sys.executable, str(HERE / "design-exemplar-capture.py"), str(refs)],
                       capture_output=True, text=True)
    msgs.append(f"capture: exit {r.returncode}. {(r.stdout + r.stderr).strip()[-600:]}")
    if r.returncode == 0:
        ex = project / "design" / "exemplars"
        n = 0
        for png in refs.glob("*-laptop.png"):
            (ex / png.name).write_bytes(png.read_bytes())
            n += 1
        msgs.append(f"{n} laptop capture(s) copied into design/exemplars/ for directions.md to cite")
        r2 = subprocess.run([sys.executable, str(HERE / "design-standard-from-exemplars.py"),
                             str(project / "design-chain.json"), "--refs", str(refs), "--apply"],
                            capture_output=True, text=True)
        msgs.append(f"standard: exit {r2.returncode}. {(r2.stdout + r2.stderr).strip()[-600:]}")
    return msgs


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("project", nargs="?", default=".")
    ap.add_argument("--answers", help="answers as JSON, keyed like --print-questions shows")
    ap.add_argument("--capture", action="store_true", help="capture the exemplars now and derive the standard")
    ap.add_argument("--print-questions", action="store_true")
    a = ap.parse_args(argv)
    if a.print_questions:
        print(json.dumps(QUESTIONS, indent=1))
        return 0
    project = Path(a.project).resolve()
    if (project / "design-chain.json").is_file():
        print(f"{project / 'design-chain.json'} already exists; init writes a new project and never "
              f"overwrites one. Edit the files under design/ directly.", file=sys.stderr)
        return 2
    answers = json.loads(Path(a.answers).read_text()) if a.answers else ask_terminal()
    probs = check_answers(answers)
    if probs:
        print("the answers are not complete:", file=sys.stderr)
        for p in probs:
            print("  - " + p, file=sys.stderr)
        return 2
    project.mkdir(parents=True, exist_ok=True)
    wrote = write(project, answers)
    for rel, what in wrote.items():
        print(f"wrote {rel}: {what}")
    if a.capture:
        for m in capture(project):
            print(m)
    else:
        print("exemplars not captured (no --capture). Before the first round, run:\n"
              f"  python3 {HERE / 'design-exemplar-capture.py'} {project / 'design' / 'references'}\n"
              f"  python3 {HERE / 'design-standard-from-exemplars.py'} {project / 'design-chain.json'} "
              f"--refs {project / 'design' / 'references'} --apply\n"
              "and copy the *-laptop.png captures into design/exemplars/.")
    probs = verify(project)
    if probs:
        print("\nstill missing before a round can be briefed:")
        for p in probs:
            print("  - " + p)
        return 1
    print("\nevery input the chain needs is in place. Next: /design-chain, for the first round.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
