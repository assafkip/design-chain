---
description: Check this machine for what a design round needs (playwright with chromium, node, the claude CLI, the vendored detector) and which design engines are installed, with where to get the missing ones.
allowed-tools: Bash, Read
---

Run the doctor and read its report to the person. Usage: `/design-chain:doctor`.

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/doctor.py"
```

Say three things, in this order:

1. **Runtime.** Each `NO` line, with the install line the report prints beside it. A round
   cannot be measured without playwright and chromium, cannot run the anti-pattern detector
   without node, and cannot run readers without `claude` on PATH.
2. **Engines.** Whether a site-lane engine is installed. If none is: `design-room` ships with
   this plugin and needs nothing, and `frontend-design` is Anthropic's, two commands away
   (`docs/ENGINES.md` has the table). Do not list all 27; name the ones missing for the lane
   the person is about to work in, and where each comes from.
3. **Whether a round can start.** The doctor exits 0 when the runtime is complete and at least
   one site-lane engine is installed. Exit 1 means fix the named line first.

Nothing here installs anything. Installing a plugin or a Python package is the person's action,
and the report gives the exact command for each.
