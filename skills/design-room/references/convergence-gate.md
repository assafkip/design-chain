# Convergence Gate (Phase 6) — diagnostics + a regression alarm, never a verdict

There is no "the build passed, ship it" state here. The founder, 2026-06-25: "when you
have a floor, you are programmed to only pass the floor." So this phase NEVER
certifies the page good or done. It does two things: (1) run diagnostics that emit
a gap list, and (2) run a regression alarm that BLOCKS when the build dropped a
technique it declared it would steal. **Done is the founder's eye, and only the
founder's eye.**

## The reframe (read first)
- A green check is not done. It cannot see craft. Treating "gate clean" as "good"
  is the exact failure this phase exists to prevent (the post-mortem of 2026-06-25,
  distilled in `docs/LESSONS.md`: a defect-absence gate is a floor, not a finish line).
- The deterministic layers below catch FAILURES (slop present, a declared technique
  absent). They never certify success. When they are clean, the work is not over —
  it goes to the founder's eye, which is the only thing that can say "good."
- Aim at the reference, not at these checks. The target is "stand it next to the
  reference and it holds," not "clear the floor."

## Layer 0 — technique parity (the regression alarm against satisficing)
The teardown (Phase 2.0) emits a `grounding/steal-manifest.json`: every technique
the build declared it would steal from a reference, with a checkable fingerprint
(import + applied-to-role). Run:
```
python3 gtm/scripts/check_technique_parity.py <project>/design-room/grounding/steal-manifest.json <project>/design-room/build/index.html
```
It lists every DECLARED technique the build dropped and BLOCKS (exit 2) if any are
missing. This is the check that would have stopped the flat-page failure. It never
prints PASS/DONE — when nothing is missing it hands the present techniques to the
founder's eye to judge whether each LANDS the same way as the reference.

(v1 is a regex-over-source presence + coarse-role check. The computed-style /
precise-role fingerprint — "glass on THE console, not just any blur" — is the
planned deepening; until it exists, do not reference it as wired.)

## Layer 0.5 — design-decision diff (the art-direction LEAD lens, running LAST)
The technique-parity alarm above binds the STACK. The `art-direction` LEAD lens runs
LAST here as the design twin: it diffs the build's DESIGN DECISIONS against the bar
it set in Phase 2 (`grounding/design-decisions.json`). Run:
```
python3 gtm/scripts/check_design_diff.py <project>/design-room/build/design-decisions.json <project>/design-room/grounding/design-decisions.json
```
It emits the GAP LIST across the four axes — subject? composition? bespoke? finish? —
and BLOCKS (exit 2) when a structural design gap remains. Like the parity alarm it
NEVER prints PASS/DONE/GOOD; when no gap remains it hands the page to the founder's
eye, which is the only thing that can say the subject lands and the idea is ownable.
(v1 is a structured design-decision diff; a playwright rendered-screenshot diff is a
named fast-follow — until it exists, do not reference it as wired.)

## Layer 1 — dogfood / eyeball gate (slop diagnostic)
The repo's AI-slop detector. Run the real render:
```
node ~/projects/eyeball/web/scan.mjs <url-or-file>        # add --vision for the UX read
```
It surfaces slop tells + whether the primary action is in the first screen. Treat a
GATE: FAIL as a worklist, and a clean result as "not slop" — NOT as "good."

## Layer 2 — impeccable detectors (44 rules)
Run the impeccable skill's detectors (brand mode for a landing page). A worklist of
design tells the fast tripwire misses. Fix each flagged rule.

## Layer 3 — vercel web-interface-guidelines audit
Run `/web-interface-guidelines` (100+ UI/UX + a11y rules). Resolve violations.

## Cross-check against the spec
- Every token in `design.md` is actually used (no drift).
- The ONE signature moment exists and uses the build-palette tool(s) the
  steal-manifest names — not raw CSS standing in for it.
- The one-sentence + 8-second test still hold on the rendered page.

## Output
Write `build/gate-report.md`: each layer, the GAP LIST (not a pass/fail verdict),
what was fixed. Then hand the page to the founder. The report frames the build as
"best I have + what it pulled from each reference + where it is still thin," never
"done."

## Rule (non-negotiable)
Never tell the founder the page is "done", "good", or "passing". Report the gaps
and the present techniques and hand it to the founder's eye. The taste verdict, and
the word "done", belong only to the founder.
