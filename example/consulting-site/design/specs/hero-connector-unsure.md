# Hero element: connector state, Unsure

`REVIEWED BY FOUNDER:` <!-- date, only when actually reviewed -->

## What it is

The third outcome (RULE-2026-09-18-I), and per `site-design.md` section 11 beat 3, the one that
matters most: the system can't confirm either way, and says so instead of guessing. "The only part
that no other consultant's page can claim."

## Shape

A hand-drawn hook-and-dot question mark, authored as a `rc.path()` curve plus a short tick for the
dot (same convention `hours-motion.js` uses for its document icon: a hand-authored path, not a
font glyph). Confirmed working in the scratch build: this fixed the earlier defect where the mark
popped in as text while everything else pen-drew.

## Color

Ink (`#071a31`). NOT the signal color, this isn't a mismatch, it's a refusal to guess, a different
meaning, and spending the signal color here would break the one-color-one-meaning rule
`design-dna.md` section 4 holds everywhere else on the site.

## Position

Same gap, same baseline as the other two connector states.

## Stands apart (decided, 2026-09-18)

This state gets its own visual weight, not the same size/row treatment as a plain checkmark or X.
Decided; the exact mechanism for "apart" (size, isolation, a distinct frame) is still open, the
scratch build currently just draws it larger (hook height ~26-19=7px more vertical travel than the
check/X's ~20-24px span) — a real founder look at the built version is needed to confirm this
alone reads as "stands apart" or needs more.

## Motion

`svg-path-draw`, `power2.out`. Hook draws first (~0.45s), dot follows (~0.15s), same pen-lift
logic as a real question mark being written by hand.

## Open

The exact "stands apart" mechanism beyond size. Whether it needs a beat of hesitation (a pause
before it resolves, unlike the instant agree/disagree draws) to read as "checking, then stopping,"
rather than just another outcome among three, is not decided.
