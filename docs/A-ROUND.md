# A round, for the first time

One round is one attempt at a page. It ends in a seal or a refusal. `/design-chain:round` runs
it; this is what each step is, in the order it happens, and which script decides whether it
happened. The gate's own rule, kept here: a step that names no script is prose.

## 0. The vision, before anything

`design/VISION.md` has to exist and carry the founder's quoted words (init wrote it). Held by
`vision_problems()` in `design-chain-gate.py`. Nothing else in the round can start until this
is true, and the brief you write next has to quote one of its lines verbatim. Why: three
fully specced, measured and sealed directions were once all wrong, because every brief was
built from constraints and none said what the page was for.

## 1. Read the owners, whole, this session

Every file `design-chain.json` lists under `owners`. Open each one in full, in THIS session.
Held by `brief_read_problems()`: the hook records what the session opened, and a brief whose
owners were not read, or a record copied from another round, is refused at seal. Why: five
consecutive rounds once carried a byte-identical brief. Four had "read the owners" by copying
a file.

## 2. brief.md

Write it fresh. Quote every anchor line verbatim (the config lists the regexes; the owner
files hold the lines). Quote one vision line verbatim. Held by `chain_problems()`, which reads
the owner files live and refuses a paraphrase.

## 3. directions.md

Three directions, each under its own heading. Cite the exemplars in `design/exemplars/` by
file name, at least the configured floor (all of them, up to three). When the round BUILDS a
pick from an earlier sealed round, one direction is enough and `craft-manifest.json` says
`implements` with that round's name. Held by `chain_problems()`.

## 3b. craft-manifest.json

The bar, where the standard is the floor. Every technique the page will carry: `id`,
`technique`, `role`, `reference` (a page in `design/references/NARRATIVE.md`), `import` and
`applied` (strings the built page must contain). Held three ways: `check_technique_parity.py`
blocks a declared technique the page does not carry; `citation_problems()` refuses a cited repo
file this session never opened; a technique citing a site the narrative does not cover is
refused as invention. A manifest with no techniques is itself a gap.

## 4. Build

One page per direction, `<Name>-laptop.html`, in the round folder. Design skills are engines:
call them inside the round and `design-engine-door.py` records each run in `engines.jsonl`.
Called outside a round, the door refuses and names this command.

## 5. Measure

Nothing here is typed by hand. The seal runs `design-standard-check.py` (the floors),
`design-gap-check.py` (distance from the exemplars), `design-impeccable-check.py` (the
anti-pattern detector, with a known-slop control in the same run) and records each exit code.
`receipt_problems()` reads them back. A `standard.json` or `gap.json` you wrote yourself is
never what seal reads.

## 6. critique.md

The nine DNA questions, answered per direction. Every weakness gets `WEAK[tag]` and a
disposition line: `- tag: FIXED|DEFERRED|CARRIED <why>`. A finding the founder raised gets
`FOUNDER-FINDING[tag]` and a disposition too. Held by `disposition_problems()` and
`founder_finding_problems()`. Why: 11 weaknesses were once named and shipped anyway, and two
were the exact defects caught next.

## 7. proof.md

One block per artifact, each with a `Proof kind:` line from the closed list and a record the
proof index holds. Held by `proof_problems()`. Opt-in: only when the config has a `proof` block.

## 8. checks/

The seal runs every check in the config's `checks` list per page (`tripwire` today, the
dogfood gate under `hooks/`) and writes the receipt. A check that skipped is a refusal, not a
pass. Held by `declared_checks()` and the receipt check.

## 9. gate/

The readers. `design-reader-gate.py` serves the round on a loopback port, screenshots each
page, and asks fresh model readers (`claude -p`) the persona questions plus two forced choices:
STAY or LEAVE, and which label is being sold. Rows land in `gate/reader-runs.jsonl`.
`reader_problems()` refuses a LEAVE, a wrong label below the floor, or a re-roll past the cap,
unless a founder disposition in `gate/dispositions.md` answers that reader by id.

## 10. Seal, then show

```bash
python3 <plugin>/scripts/design-chain-gate.py seal <round>
```

It holds a snapshot of the round and of every outside input (owners, narrative, persona,
config), runs the producers against the snapshot, checks the whole chain, compares every file
at the end, and writes `receipts.json`. Until then the PreToolUse hook blocks any preview,
artifact or file send of an unsealed page. `status <round>` reads a sealed round back.

## What none of it decides

Whether the page is good. Every step above is a floor or a record. The seal says the chain
ran on this exact set of bytes. The eye that reads the sealed page, and the buyers who see it,
decide the rest.
