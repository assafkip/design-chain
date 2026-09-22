#!/usr/bin/env python3
"""The session transcript reader the chain shares.

design-chain-gate.py loads this file by name (see its _read_first_gate) to read the
session transcript Claude Code hands a hook: which files were opened, by which tool,
and whether anything was written yet. The brief stage uses it to prove that every
owner file was opened in full THIS session before a brief was written (brief-reads.json).

It used to be a hook of its own in the repo this chain was extracted from: the first
write of a session waited until a methodology document and one lesson had been opened.
That gate depended on that repo's layout and is not part of this tool. Only the parser
travelled, and the filename stayed so the gate's loader did not change.

An open counts from ANY tool: Read, Grep, or a Bash `cat`/`sed`. The check is whether the
path appears in a tool_use input, not which tool was fashionable. stdlib only.
"""
from __future__ import annotations

import json
from pathlib import Path

WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}


def _records(transcript_path) -> list[dict]:
    p = Path(transcript_path) if transcript_path else None
    if not p or not p.exists():
        return []
    out = []
    for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        try:
            out.append(json.loads(line))
        except Exception:
            continue
    return out


def _tool_uses(records) -> list[tuple[str, str]]:
    """(tool_name, serialized input) for every tool call in the session."""
    uses = []
    for rec in records:
        msg = rec.get("message", {})
        if not isinstance(msg, dict):
            continue
        for item in msg.get("content", []) or []:
            if isinstance(item, dict) and item.get("type") == "tool_use":
                uses.append((item.get("name", ""),
                             json.dumps(item.get("input", {}))))
    return uses


def already_wrote(uses) -> bool:
    return any(name in WRITE_TOOLS for name, _ in uses)


def opened(uses, needle: str) -> bool:
    """Did any tool call this session reference this path? Tool-agnostic by design."""
    return any(needle in blob for _, blob in uses)


if __name__ == "__main__":
    import sys
    uses = _tool_uses(_records(sys.argv[1] if len(sys.argv) > 1 else ""))
    for name, blob in uses:
        print(name, blob[:120])
