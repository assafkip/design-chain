#!/usr/bin/env python3
"""dc-24: the wiring ships with the plugin, and it is run the way the harness runs it.

WHY. The gate and the door are only enforcement if the harness calls them. This test reads
hooks/hooks.json, the one file Claude Code loads for this plugin, and RUNS each wired command
the way Claude Code does: payload on stdin, CLAUDE_PLUGIN_ROOT and CLAUDE_PROJECT_DIR set,
against a temp project. A grep for the command string proves a string, not a hook that runs.

A plugin has one hooks file, so test_every_role_is_wired_once checks that file for the six
roles (gate before a show, gate after a write, door before and after a Skill call, gate at
Stop and at SubagentStop) and runs each command it finds.
"""
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HOOKS = ROOT / "hooks" / "hooks.json"
GATE = "scripts/design-chain-gate.py"
DOOR = "scripts/design-engine-door.py"
SHIPPED = ("design-chain-gate.py", "design-engine-door.py", "design-engines.json",
           "read-first-gate.py", "design-reader-gate.py")


def wired(path: Path = HOOKS) -> dict:
    """{(event, matcher, command): command} for every chain hook in hooks.json."""
    out = {}
    for ev, arr in (json.loads(path.read_text()).get("hooks") or {}).items():
        for m in arr:
            for h in m.get("hooks", []):
                cmd = h.get("command", "")
                if GATE in cmd or DOOR in cmd:
                    out[(ev, m.get("matcher"), cmd)] = cmd
    return out


class Wiring(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="dc24-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        # the plugin as installed: a copy, so a test that breaks a script breaks the copy
        self.plug = self.tmp / "plugin"
        (self.plug / "scripts").mkdir(parents=True)
        for name in SHIPPED:
            shutil.copy(ROOT / "scripts" / name, self.plug / "scripts" / name)
        # the project the person is designing in
        self.inst = self.tmp / "inst"
        self.inst.mkdir()
        (self.inst / "design-chain.json").write_text(json.dumps({"project": "dc24", "owners": []}))
        self.round = self.inst / "site" / "design" / "r1"
        self.round.mkdir(parents=True)
        self.page = self.round / "Home-laptop.html"
        self.page.write_text("<html><body><p>x</p></body></html>")

    def run_hook(self, cmd: str, payload: dict, project: Path | None = None):
        env = {k: v for k, v in os.environ.items() if k != "DESIGN_CHAIN_ALLOW"}
        env.update({"CLAUDE_PLUGIN_ROOT": str(self.plug), "CLAUDE_PROJECT_DIR": str(project or self.inst),
                    "DESIGN_CHAIN_STATE": str(self.tmp / "state")})
        r = subprocess.run(["bash", "-c", cmd], input=json.dumps(payload), capture_output=True,
                           text=True, env=env, timeout=300, cwd=str(project or self.inst))
        return r.returncode, r.stdout + r.stderr

    def pick(self, ev: str, which: str = GATE) -> str:
        return next(c for (e, _m, _c), c in wired().items() if e == ev and which in c)

    def test_every_role_is_wired_once(self):
        roles = {}
        for (ev, matcher, cmd) in wired():
            roles.setdefault((ev, DOOR in cmd), []).append(matcher)
        for want in (("PreToolUse", False), ("PostToolUse", False), ("PreToolUse", True),
                     ("PostToolUse", True), ("Stop", False), ("SubagentStop", False)):
            self.assertIn(want, roles, f"{want} is not wired")
            self.assertEqual(len(roles[want]), 1, f"{want} is wired more than once: {roles[want]}")
        wide = roles[("PreToolUse", False)][0]
        for tool in ("SendUserFile", "Artifact", "Bash"):
            self.assertIn(tool, wide, f"the show gate does not cover {tool}")
        self.assertTrue(any(m.endswith("mcp__plugin_chrome-devtools.*") for m in roles[("PreToolUse", False)]),
                        "a browser preview is a show")
        for m in roles[("PreToolUse", True)] + roles[("PostToolUse", True)]:
            self.assertEqual(m, "Skill", "the door fires on Skill and nothing else")

    def test_every_chain_command_runs_python_isolated(self):
        for (ev, matcher, _c), cmd in sorted(wired().items()):
            self.assertIn("python3 -I ", cmd, f"{ev}/{matcher} is not isolated")
            self.assertIn("${CLAUDE_PLUGIN_ROOT}", cmd, f"{ev}/{matcher} does not resolve from the plugin root")

    def test_a_missing_script_is_a_silent_no_op(self):
        # the Pre/Post form exits 1 with no output and the tool proceeds; the Stop form exits 0
        for (ev, matcher, _c), cmd in sorted(wired().items()):
            broken = cmd.replace("design-chain-gate.py", "design-chain-gate-absent.py").replace(
                "design-engine-door.py", "design-engine-door-absent.py")
            rc, out = self.run_hook(broken, {"hook_event_name": ev, "tool_name": "Read", "session_id": "s-gone",
                                             "tool_input": {}})
            self.assertEqual(out.strip(), "", f"{ev}/{matcher} said something when its script was missing")
            self.assertIn(rc, (0, 1), f"{ev}/{matcher} exited {rc} with its script missing")

    def test_every_wired_command_runs_and_passes_a_benign_payload(self):
        for (ev, matcher, _c), cmd in sorted(wired().items()):
            rc, out = self.run_hook(cmd, {"hook_event_name": ev, "tool_name": "Read", "session_id": "s-dc24",
                                          "tool_input": {"file_path": str(self.inst / "design-chain.json")}})
            self.assertEqual(rc, 0, f"{ev}/{matcher}: {out}")

    def test_the_wired_gate_blocks_showing_an_unsealed_page(self):
        self.run_hook(self.pick("PostToolUse"),
                      {"hook_event_name": "PostToolUse", "tool_name": "Write", "session_id": "s-dc24",
                       "tool_input": {"file_path": str(self.page)}})
        rc, out = self.run_hook(self.pick("PreToolUse"),
                                {"hook_event_name": "PreToolUse", "tool_name": "SendUserFile",
                                 "session_id": "s-dc24", "tool_input": {"files": [str(self.page)]}})
        self.assertEqual(rc, 2, out)
        self.assertIn("design chain", out.lower())

    def test_the_wired_door_refuses_an_engine_outside_a_round(self):
        listed = json.loads((ROOT / "scripts" / "design-engines.json").read_text())["engines"][0]["skill"]
        rc, out = self.run_hook(self.pick("PreToolUse", DOOR),
                                {"hook_event_name": "PreToolUse", "tool_name": "Skill", "session_id": "s-dc24",
                                 "cwd": str(self.inst), "tool_input": {"skill": listed}})
        self.assertEqual(rc, 2, out)
        self.assertIn("design-chain", out)

    def test_a_project_that_never_opted_in_is_untouched(self):
        plain = self.tmp / "plain"
        plain.mkdir()
        page = plain / "index.html"
        page.write_text("<html><body><p>x</p></body></html>")
        self.run_hook(self.pick("PostToolUse"), {"hook_event_name": "PostToolUse", "tool_name": "Write",
                                                 "session_id": "s-plain", "tool_input": {"file_path": str(page)}},
                      project=plain)
        for ev in ("Stop", "SubagentStop"):
            rc, out = self.run_hook(self.pick(ev), {"hook_event_name": ev, "session_id": "s-plain",
                                                    "stop_hook_active": False}, project=plain)
            self.assertEqual(rc, 0, f"{ev} blocked a project that never opted in: {out}")
        rc, out = self.run_hook(self.pick("PreToolUse"),
                                {"hook_event_name": "PreToolUse", "tool_name": "SendUserFile",
                                 "session_id": "s-plain", "tool_input": {"files": [str(page)]}}, project=plain)
        self.assertEqual(rc, 0, out)
        listed = json.loads((ROOT / "scripts" / "design-engines.json").read_text())["engines"][0]["skill"]
        rc, out = self.run_hook(self.pick("PreToolUse", DOOR),
                                {"hook_event_name": "PreToolUse", "tool_name": "Skill", "session_id": "s-plain",
                                 "cwd": str(plain), "tool_input": {"skill": listed}}, project=plain)
        self.assertEqual(rc, 0, "the door refused an engine in a project with no design-chain.json")

    def test_the_command_has_one_home(self):
        self.assertFalse((ROOT / ".claude" / "commands" / "design-chain.md").exists(),
                         "the command has one home: commands/design-chain.md")
        self.assertTrue((ROOT / "commands" / "design-chain.md").is_file())
        manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
        self.assertEqual(manifest.get("hooks"), "./hooks/hooks.json")
        self.assertEqual(manifest.get("commands"), "./commands/")


if __name__ == "__main__":
    unittest.main()
