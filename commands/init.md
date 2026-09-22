---
description: Set up a project for the design chain by asking, one question at a time, for everything a round needs (vision, buyer, the one idea, what not to look like, exemplars, narrative, labels) and writing each file as the answer lands.
allowed-tools: Bash, Read, Write, Glob
---

Set up the design chain for the project in the current directory. Usage: `/design-chain:init`.

This is a conversation, not a form. Ask ONE question at a time, in the order below, show the
example answer with it, and wait. Do not answer for the person: the vision is theirs in their
words, the buyer phrases are things a buyer actually said, and a phrase you invent is a phrase
the gate will hold a brief to forever. If an answer is thin, say so once and take what they give.

## Before the first question

```bash
test -f design-chain.json && echo "EXISTS: design-chain.json is already here. Edit the files under design/ instead." || echo "OK"
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/doctor.py"
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/init.py" --print-questions
```

EXISTS: stop and say so. Then read the doctor's report to the person before anything else: a
`NO` runtime line means a round cannot be measured, and no site-lane engine means the build
step has nothing to call. Name the missing item and where it comes from (the report says), then
go on with the questions; nothing in init needs them installed yet. The JSON printed last is
the question list: `key`, `ask`, `example`, and whether the answer is a list (`many`) with a
minimum. Ask them in that order.

## The questions, and why each exists

1. **project**: the product in one line. Names the config.
2. **vision**: three or more sentences in their words, verbatim. Becomes `design/VISION.md`; every
   brief must quote one line of it word for word (`vision_problems`).
3. **buyer**: who arrives, in a paragraph. Becomes the top of `design/owners/buyer.md`, which is both
   an owner and the persona the reader gate role-plays.
4. **buyer_words**: three or more phrases a buyer actually said. The first becomes a brief anchor
   the gate checks verbatim.
5. **idea**: the one sentence the page repeats. An owner with an anchor.
6. **not_this**: what it must not look like, with reasons. An owner with an anchor.
7. **exemplars**: three to six URLs. Captured and measured; the standard is derived from them.
8. **narrative_shared**, **narrative_each**, **narrative_ours**: the human read of the group. Becomes
   `design/references/NARRATIVE.md`, which every craft technique must cite. Ask these AFTER the
   person has looked at their exemplars; if they have not, tell them to open the sites now.
9. **labels**: what a stranger might think the page sells, the right answer first. The reader gate
   makes each reader pick one.
10. **signal**: one hex colour or blank.

## Then

Write the answers to `design/init-answers.json` (create the directory) as one JSON object keyed by
`key`, list answers as JSON arrays. Then:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/init.py" . --answers design/init-answers.json --capture
```

`--capture` needs playwright with chromium (`pip install playwright && playwright install chromium`).
If it is not installed, run without `--capture`, show the two commands init prints, and say that
the first round cannot cite exemplars until they run.

Read init's last block aloud: either "every input the chain needs is in place" or the list of what
is still missing, each line naming the file. Do not fix a missing item by writing the file yourself;
ask the question again.

## What this does not do

It does not judge the answers, and neither does the gate. A vision that is aimed at nothing passes
init and seals a wrong page. The check that catches that is a person reading `VISION.md` and
disagreeing with it, which is what the notebook is for.
