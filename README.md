# design-chain

A design round for a product site, run as a gate. You say what the page is for, in your own
words. You name the buyer and quote what they said. You pick sites you admire, and the floors
are measured from those instead of argued about. Then a round is one brief, three directions,
a build, a set of measurements a browser takes, a critique that has to answer its own
weaknesses, and fresh model readers who role-play your buyer and say whether they would stay.
Nothing is shown to you before the seal, and the seal records what ran on which bytes.

It is a Claude Code plugin. Python and Node do the measuring; Claude does the asking and the
building; the hooks make the steps refusals instead of reminders.

## Install

```
/plugin marketplace add assafkip/design-chain
/plugin install design-chain@design-chain
```

Then, once per machine:

```bash
pip install playwright Pillow && playwright install chromium   # the measurements run a browser
node --version                                                  # 18+, for the anti-pattern detector
```

To try it from a local checkout instead: `claude --plugin-dir /path/to/design-chain`.

## Ten minutes to a project

```
/design-chain:init
```

Seven questions, one at a time, each with an example answer. It writes a file after each and
ends by checking what it wrote the way the gate reads it. `docs/GETTING-STARTED.md` has the
questions and why each exists.

## An hour to a first round

```
/design-chain:round
```

`docs/A-ROUND.md` is the ten steps for a first-timer, each naming the script that holds it.
When a step refuses, `docs/WHY-IT-REFUSES.md` has the message and the fix side by side.

## What it refuses, and why

- A brief that paraphrases an owner line. The anchors are read live and quoted verbatim, because
  a brief written from memory is how the generic layout comes back.
- A brief that is a byte-copy of an earlier one. Writing it is the act of reading.
- A round with no vision in the founder's quoted words. Three sealed directions were once all
  wrong; nothing had been skipped, and none said what the page was for.
- A craft manifest that declares nothing, or declares a technique the page does not carry.
- A measurement typed by hand. The seal runs the producers itself and records their exit codes.
- A weakness the critique named and nobody answered.
- A reader who would leave, or who thinks the page sells something else.
- A preview of an unsealed page.

`docs/LESSONS.md` is where each of those came from.

## What it does not do

It does not decide whether the design is good. Every check is a floor: it catches the wireframe,
the paraphrase, the uncited technique, the bland page that has no defects. A page can clear all
of it and still be wrong. The seal means the chain ran. Your eye and your buyers are the bar.

## The example

`example/consulting-site/` is a real consulting site's real inputs: its vision notebook, the
five owner documents the briefs quote, the exemplar captures and their narrative, and one
sealed round with three directions. Client names are replaced. It is the answer key: the test
suite checks that the gate still accepts it, so it cannot drift from what the chain wants.

## Layout

```
.claude-plugin/     plugin.json, marketplace.json
commands/           round.md, init.md            /design-chain:round, /design-chain:init
hooks/              hooks.json, dogfood_gate.py  the wiring, and the AI-default tripwire
scripts/            the chain: gate, door, checks, capture, reader gate, init
scripts/test/       the suite (python3 -m pytest scripts/test scripts/test_design_chain_gate.py)
vendor/impeccable/  the anti-pattern detector (pbakaus/impeccable, Apache-2.0, detector only)
docs/               getting started, a round, why it refuses, lessons
example/            consulting-site: inputs and one sealed round
```

## Tests

```bash
python3 -m pytest scripts/test scripts/test_design_chain_gate.py hooks/test_dogfood_gate.py -q
```

About ten minutes; the producers run a real browser. `DESIGN_CHAIN_RESEAL=1` additionally
reseals the example on a copy, which needs `claude` on the path for the readers.

## License

MIT. The vendored detector under `vendor/impeccable` is Apache-2.0; its LICENSE and NOTICE
are in that directory.
