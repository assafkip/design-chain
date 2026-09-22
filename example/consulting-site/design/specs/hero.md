# Hero: two records that should agree, drawn in the seam's grammar

REVIEWED BY FOUNDER: 2026-09-21 (four picks, via the design-chain round 2026-09-21 questions)

Supersedes the drawn-form parts of `hero-record-claim.md`, `hero-record-source.md` and the three
`hero-connector-*.md` specs. Their labels, the abstraction rule (RULE-2026-09-18-J) and the
headline spec stand.

## What it says

"Automated. But is it true?" Then what he does: "I build the check that tells you, and it stops
when it can't prove it". Then the drawing shows it happening, once, then rests.

## The drawing

- **Where:** a white sheet inset in the blue hero panel (founder pick 3). Ink `#071a31`, faint
  structure `rgba(7,26,49,.30)`, the one signal `#3875be` (founder pick 4), used ONLY for no match.
- **Two records, one pair (RULE-2026-09-18-J):** "The claim" on the left, "The source" on the
  right. Each is one hand-drawn record with three content rows. No document type, no number.
- **The gap between them** is labelled "Checking it's actually true." (the 2026-09-18 pick for the
  old judgment box, now the drawing's verb).
- **Three rows, three outcomes, all in `Seam.astro`'s grammar (founder pick 1):**
  - Row 1, match: a flat faint line crosses the gap to its partner row.
  - Row 2, no match: a blue line runs into the gap and ends in a small blue circle. The source's
    row 2 is missing, the seam's "hole".
  - Row 3, unsure: an ink line starts into the gap, pauses, and stops halfway. The label
    "Unsure? It stops." sits at the stop. Not blue: it is a refusal, not a mismatch.
- **Labels:** one rule (RULE-2026-09-17-B): each label above the thing it names, left-aligned to
  it, at its width, record labels on one shared baseline.

## Motion (the live hero's, carried over)

From `hours-motion.js` and `ink.js`: rough.js with fixed seeds; outlines pen in via
`strokeDashoffset`, `power1.inOut`; small marks `power2.out`; one paused GSAP timeline, played by
an IntersectionObserver, paused off screen; repeats after a rest like the live hero; reduced motion
lands on the settled frame. The rows resolve one at a time, the unsure line holds a visible pause
before it stops. Pointer: hovering a row lights it on both sides (the seam's `is-lit`).

## Phone

Both compositions ship and CSS picks (`Seam.astro`, DEPLOY.md scar 2026-09-17). On a phone the
records sit closer; the three outcomes and labels stay.
