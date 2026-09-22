# Hero element: connector state, Agree

`REVIEWED BY FOUNDER:` <!-- date, only when actually reviewed -->

## What it is

One of three outcomes the hero's mechanic can resolve to (RULE-2026-09-18-I): the claim and the
source agree.

## Shape

A single hand-drawn checkmark, three-point `linearPath` (rough.js), same hand as the panels. Not a
UI checkmark icon, an authored stroke path, so it draws with the same pen-draw technique as
everything else on the page.

## Color

Ink (`#071a31`), the site's default stroke color. Deliberately NOT the signal color, agreement is
not the mismatch, so it stays neutral.

## Position

In the gap between Record A and Record B, centered on their shared baseline.

## Motion

`svg-path-draw`, `power2.out` ease (matches `hours-motion.js`'s small-element draws, distinct from
the `power1.inOut` used for the larger panel sheet). Draws after both panels and their labels
settle, at roughly t≈1.4s in the working scratch timeline, ~0.3s duration.

## Open

None specific to this state. Its visual weight relative to the "unsure" state's larger treatment
is set by that state's spec (`hero-connector-unsure.md`), not by anything here.
