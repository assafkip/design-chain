# Hero element: Record A, "the claim"

`REVIEWED BY FOUNDER:` <!-- date, only when actually reviewed -->

## What it is

One of two abstract records in the hero's two-records mechanic (RULE-2026-09-18-I/J). Stays
generic, no specific document type, so it reads the same across every segment (CPA, law, A&E).

## Shape

Hand-sketched rectangular panel, rough.js, fixed seed (matches `Sketch.astro`/`ink.js`'s
established hand). Two short interior lines suggesting content, not a specific document's fields.
No hachure fill on the panel body itself (the panels in the working scratch build use plain
outline + two content lines; hachure was tested and read as noisy at this scale, per the earlier
comparison render).

## Label

"THE CLAIM" — small caps, muted grey (`#8a97ab`, the site's established secondary-text color),
positioned above the panel.

## Position

Left of the two-panel pair, on one shared baseline with Record B (`one-baseline-composition`,
established technique).

## Motion

`svg-path-draw` (hyperframes-animation): outline strokes draw in via measured `getTotalLength()` /
`strokeDasharray` / `strokeDashoffset`, `power1.inOut` ease (matches `hours-motion.js`'s sheet-draw
ease), no bounce. Draws first in the sequence, starting at t≈0.1s in the working scratch timeline.

## Open

Whether this stays a plain outline+lines or needs the richer illustrative weight seen in the live
hero (icons, layered depth) is not resolved — this spec describes the current scratch-verified
version, not necessarily the final production version.
