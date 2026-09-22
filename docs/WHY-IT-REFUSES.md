# Why it refuses, and what to do

Every refusal the gate prints names a file. This lists them by family, with the fix beside
each. The messages are quoted as the gate prints them; the exact wording lives in
`scripts/design-chain-gate.py`, and that file wins where they differ.

## Before a round can start

| The gate says | What it means | The fix |
|---|---|---|
| `no design-chain.json found above <page>` | The page is not under a project init set up. | Run `/design-chain:init` in the project folder, or move the round under `design/`, beside `references/`. |
| `missing design/VISION.md: the chain declares a vision stage and the vision has not been written` | The config has a `vision` block and the file is gone. | Write it, or answer question 2 of init again. |
| `VISION.md carries N founder block(s); 3 required` | Fewer than three dated, quoted lines. | Add lines shaped `**Founder, YYYY-MM-DD:** "their words"`. |
| `owner anchor unreadable: <label> -> <line>` | An anchor regex in the config matches nothing in its owner file. The file changed. | Re-derive the anchor from the file as it is now, or restore the line. Never loosen the regex to `.*`. |

## The brief

| The gate says | What it means | The fix |
|---|---|---|
| `brief.md does not quote verbatim: <anchor>` | The brief paraphrased an owner line. | Paste the line from the owner file. Read live, so yesterday's wording may differ. |
| `brief.md quotes no line from VISION.md verbatim` | The round is near the vision, not built from it. | Quote one full founder line. |
| `brief.md is a byte-copy of round <x>` | The brief was copied, so the owners were never read. | Write it again, in this session. |
| a brief whose owners were not read in full | `brief-reads.json` shows an owner opened partially or not at all. | Open every owner file whole (a full Read, not a grep) before writing the brief. |

## Directions and the manifest

| The gate says | What it means | The fix |
|---|---|---|
| `directions.md names N direction heading(s); three are required` | Fewer than three `##` headings, and the round does not `implements` a sealed pick. | Add directions, or set `implements` to a sealed round that had three. |
| `directions.md cites N of the exemplars in design/exemplars; the floor is M` | Captures not named by file name. | Name them: `stripe-com-laptop.png`, as spelled in the folder. |
| `craft-manifest.json declares no techniques, so nothing was verified` | An empty manifest. | Declare what the page carries. Declaring nothing is the cheapest way to comply and is refused for that reason. |
| `technique '<id>' cites no reference` or cites a site the narrative does not cover | Provenance invented. | Cite a heading in `design/references/NARRATIVE.md`. Add the site to the roster and the narrative first if it is new. |
| `technique '<id>' is declared and absent from <page>` | `check_technique_parity.py` found none of its `applied` strings in the built page. | Build it, or delete the claim. |
| `craft-manifest.json declares component '<c>' and design/specs/<c>.md does not exist` | The round names a component with no spec. | Write the spec first. It needs a `REVIEWED BY FOUNDER: <date>` line. |

## Measuring

| The gate says | What it means | The fix |
|---|---|---|
| `<page> FAILS the standard` | `design-standard-check.py` found a floor broken: too many type sizes, words, large elements, signal-colour uses, a hero off centre. | The check prints the axis and the number. Fix the page; do not edit `standard.json`. |
| `<page> is below the exemplar floor. <axis>` | `design-gap-check.py`: the page is blander than the least of the exemplars on that axis. | Add what the axis names (imagery, distinct backgrounds, motion, controls). |
| `its negative control did not fire (design-impeccable-check.py exit 1), so a clean result proves nothing` | The detector ran but the known-slop control passed too, so the run is blind. | Node or the vendored detector is broken. `node vendor/impeccable/detector/detect-antipatterns.mjs --json <any html>` should print findings. |
| `a page raised an anti-pattern (exit 3)` | The detector found a tell: gradient text, a converged font, the default violet. | Fix it, or record a founder decision under `craft.allow_tells` with a reason. |
| `could not measure (exit N)` | Playwright or chromium is missing, or the page will not load. | `pip install playwright && playwright install chromium`; serve the page. |
| `the tripwire check FAILED this page` | The dogfood gate found AI-default tells or no primary action. | Its output lists each tell with the fix. `<!-- eyeball-gate-skip -->` exempts a deliberate parody only. |
| `the <name> check did not run on this page (exit 3). A check that skipped is not a pass` | The check could not run. | Fix the cause it prints. Skips are refusals on purpose. |

## Critique, proof, readers

| The gate says | What it means | The fix |
|---|---|---|
| `critique.md marks N finding(s) WEAK with no tag` | `WEAK` without `[tag]`. | Write `WEAK[some-tag]`. |
| `critique.md: weakness '<tag>' has no disposition` | Named and not answered. | Add `- tag: FIXED <what changed>` or `DEFERRED <why>` or `CARRIED <why>`. |
| `FOUNDER-FINDING[<tag>] has no disposition` | The founder raised it; nobody answered. | Same line shape. |
| `proof.md has no artifact block` / `names proof kind '<k>', not one of the closed list` | Proof shape. | One heading per artifact with `Proof kind:` from the list the message prints, citing a record the index holds. |
| `reader <id> said LEAVE, and that it sells '<label>'` | A fresh reader would leave, or misread what is sold. | Change the page. Or, if the reader is wrong, answer it by id in `gate/dispositions.md` as a founder decision. |
| `readers answered N of M for <page>` | A run came back short. | Re-run the reader gate; check `claude -p` works. |
| `re-roll past the cap` | Too many reader runs on one page in one round. | The cap is the record. Start a new round. |

## The seal itself

| The gate says | What it means | The fix |
|---|---|---|
| `a file in the round changed after the seal` | Bytes differ from the receipt. | Reseal. A sealed round is history; editing it re-opens it. |
| `design-chain.json changed after this round was sealed` | The config is an input; changing it unseals every round under it. | Reseal the rounds you still need. |
| `the receipt names a producer that is neither at its path now nor in this repo's history` | The scripts that sealed it are gone. | Reseal with the current scripts. |
| `the page asked for [files] and this round does not serve it` | A stylesheet or image referenced from outside the round. | Copy it into the round folder. A page measured against a missing file is not the page. |
| `design engine '<skill>' called outside a round` (from the door) | A listed design skill ran with no open round. | Start `/design-chain:round` first; the door records the engine run for the manifest. `DESIGN_CHAIN_ALLOW=1` in your own shell is the override. |

## When the message is not here

`grep -n "the sentence" scripts/design-chain-gate.py`. Every refusal is a literal in that file
with a comment above it saying which failure it came from.
