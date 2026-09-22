# Hero element: connector state, Disagree

`REVIEWED BY FOUNDER:` <!-- date, only when actually reviewed -->

## What it is

The second of three outcomes (RULE-2026-09-18-I): the claim and the source disagree, the mismatch,
where the money leaks.

## Shape

A hand-drawn X, two crossing `linearPath` strokes (rough.js), same hand as the panels and the
checkmark.

## Color

**Open, inherited-unresolved, flagging rather than picking silently again.** `design-chain.json`
`standard.signal` says `#0066b3`. The site's actual shipped CSS (`system.css`, `Sketch.astro`)
uses `#3875be`, and has since at least round 2026-09-16e (site-design.md Decision log: "calendly's
inset rounded panel... #265994 / #3875be behind the words"). This spec uses `#3875be` because
that's what's actually live, not because the discrepancy is resolved. Whichever is right, one of
the two config sources needs fixing so they stop disagreeing, the same defect class the whole
redesign exists to catch.

## Position

Same as the checkmark: centered in the gap between the two panels, on their shared baseline.

## Motion

`svg-path-draw`, `power2.out`, two strokes staggered (~0.2s apart in the working scratch timeline)
so the X reads as two distinct pen strokes crossing, not one shape popping in.

## Open

The color source-of-truth conflict above. Otherwise matches the agree state's timing and technique.
