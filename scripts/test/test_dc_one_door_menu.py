#!/usr/bin/env python3
"""dc-22: one design command in the menu.

WHY. /design-chain is the one design command. The other design skills are engines the chain
calls, and design-engine-door.py refuses them outside a round (dc-18). A skill that ships INSIDE
this plugin and is listed as an engine must not also sit in the slash menu as a command of its
own, so every such skill carries `user-invocable: false` in its frontmatter. Skills installed
from elsewhere (the marketplace names in design-engines.json) are not this repo's to edit; the
door is what keeps them behind a round.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"


def frontmatter(p: Path) -> dict:
    text = p.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        k, sep, v = line.partition(":")
        if sep and not line.startswith(" "):
            # YAML says False, 'false' and a trailing comment are the same value
            v = v.split("#")[0].strip().strip("'\"").casefold()
            out[k.strip()] = v
    return out


def engines() -> set:
    names = {e["skill"] for e in json.loads((SCRIPTS / "design-engines.json").read_text())["engines"]}
    assert names, "the registry lists no engines"
    return names


def repo_skills() -> dict:
    out = {}
    for p in sorted(ROOT.glob("skills/*/SKILL.md")):
        name = frontmatter(p).get("name") or p.parent.name
        out[name] = p
    return out


class OneDoorMenu(unittest.TestCase):
    def test_every_listed_in_repo_engine_is_hidden_from_the_menu(self):
        listed = engines()
        ours = {n: p for n, p in repo_skills().items() if n in listed}
        shown = [str(p.relative_to(ROOT)) for p in ours.values()
                 if frontmatter(p).get("user-invocable") != "false"]
        self.assertEqual(shown, [], "a design engine shipped here is still a slash command of its own")

    def test_every_design_shaped_skill_shipped_here_is_a_listed_engine(self):
        # a skill whose name reads as design OUTPUT must be in the registry, or the door does not
        # know it. Unambiguous output words only: "brand" alone reads as content.
        words = ("design", "deck", "slide", "motion", "video", "ui", "ux", "logo", "art")
        shaped = {n for n in repo_skills() if any(w in n.casefold().split("-") for w in words)}
        self.assertEqual(shaped - engines(), set(), "a design-shaped skill the door does not know")

    def test_the_registry_has_the_documented_shape(self):
        data = json.loads((SCRIPTS / "design-engines.json").read_text())
        self.assertIn("_doc", data)
        for e in data["engines"]:
            self.assertEqual(set(e), {"skill", "lane", "stage"}, e)
            self.assertIn(e["lane"], ("site", "brand", "deck", "motion"), e)

    def test_the_command_doc_names_the_door(self):
        text = (ROOT / "commands" / "round.md").read_text()
        self.assertIn("design-engine-door.py", text)


if __name__ == "__main__":
    unittest.main()
