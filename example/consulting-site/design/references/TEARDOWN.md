<!-- voice-lint-skip -->
# Teardown: four reference pages, loaded and measured 2026-09-15

**Why this file exists.** The design chain had an enforcement half and no input half.
`craft-manifest.json` makes the build prove it used the techniques it declared, and
`check_technique_parity.py` blocks when it did not. But nothing filled the manifest from
anywhere except my own prior, so the chain faithfully verified that I built what I
imagined, and what I imagine is generic. Founder, on two rounds of it: "This is the most
generic stuff ever. How is this possible with all the MCPs? do you need an example to work
from?" Yes. This is the missing step.

cole-gtm's design-room had it and I ported only the back half:

    cole-gtm:  GROUND on real references -> teardown -> steal-manifest -> build -> parity
    what I built:            (nothing)           ->  craft-manifest  -> build -> parity

**What was actually done here.** Each page was loaded in a real browser at 1440x900,
screenshotted (the `.png` beside this file), and probed for the fonts, type sizes, colour
counts and element counts that are visible above the fold. Every number below came out of
that probe. Nothing here is recalled.

**On the tooling question.** The `ui-ux-pro-max` skill is real and substantial: 1,775
design rows, 1,924 Google fonts, 161 colours, 89 styles, 162 product profiles. It is a
catalogue of style NAMES (Glassmorphism, Neumorphism, Aurora UI) and landing PATTERNS
("Hero + Features + CTA", "3-5 key features", "CTA glow on hover"), and its recommendation
for SaaS is "Glassmorphism + Flat Design". Those are the AI-default vocabulary this site's
canon bans outright (`site-design.md` section 7, RULE-2026-09-15-C). Grepped all 14 of its
CSVs for a URL: the only hits are `fonts.google.com`. It contains zero real pages. Using it
to escape generic would have gone the wrong way. The capability that works is a browser,
and until this file nothing in the chain had ever opened one.

---

## trailofbits.com

Measured: fonts `FH Lecturis` (display), `Geist` + `Geist Mono` (text). Type sizes above
the fold `9, 11, 12, 14, 16, 22, 80`. 6 text colours, 9 background colours, 3 images,
**27 inline SVGs**, 1 animated element.

**What makes it not generic, concretely:**

1. **A persistent dark icon rail down the left edge**, full height, with the logo at the
   top and "Get in Touch" pinned at the bottom. The page is not a centred column; it has
   an architecture.
2. **A counter bar of real numbers as chrome**: `946 PUBLICATIONS · 620 AUDITS · 200+
   OPEN-SOURCE REPOS · Since 2012`, small, mono, with a tiny icon each, sitting in the
   header. The proof is furniture, not a section.
3. **Dithered bitmap illustrations** for each service (a bug, a microscope), drawn as
   1-bit pixel art. Nobody else's page looks like this and no generator defaults to it.
4. **A halftone dot-matrix mark** in red, top-left of the hero, purely as a graphic
   signature.
5. **Graph-paper texture** behind the featured-research diagram, so a technical drawing
   sits on technical paper.
6. **Mono uppercase labels** as a system: `FEATURED RESEARCH`, `SERVICES`, `LEARN MORE`,
   `VIEW ALL`, `TALK`, `AI/ML`. One register for labels, another for prose.
7. **Two buttons, each with its arrow in a separate bordered box** beside the label.

**Take for askconsulting:** the counter bar of real numbers as chrome (he has real ones),
the mono uppercase label system, graph-paper behind a technical artifact, and the arrow-box
button. **Leave:** the left rail (that is a publisher's architecture, not a one-week
offer's) and the service card row (RULE-2026-09-15-C bans it here).

## inkandswitch.com

Measured: fonts `Merriweather Sans`, `Geogrotesque`. Type sizes `13, 14, 16` and nothing
else. **1 text colour, 1 background colour.** 1 SVG, 1 `<canvas>`.

**What makes it not generic:** the entire first screen is one made thing. The ten letters
of I-N-K-&-S-W-I-T-C-H are each drawn as a different technical diagram: a wireframe
hyperboloid, a coil, an oscilloscope trace, a logic circuit, a pixel grid, a mushroom
plot, a terminal readout reading `PRESS C`. White line art on pure black, interactive,
built on a canvas with their own research tech. The only prose is a narrow column on the
right at 13 to 16px.

This is the most disciplined page of the four and the most extreme: three type sizes, one
colour, one background, and all of the effort in a single bespoke artifact.

**Take:** the principle that the first screen can BE the artifact rather than describe one,
and that a page can hold three type sizes and one colour and still be the least generic
page in the set. **Leave:** it is an anniversary art piece for a research lab, and it tells
a cold buyer nothing in the first seconds. RULE-2026-09-15-H is the opposite requirement.

## latacora.com

Measured: fonts `Poppins` (display), `Open Sans`. Type sizes `16, 20, 24, 80`. 2 text
colours, 3 background colours, 2 images, 0 SVG, 0 animation, 0 shadows.

**What makes it work:** one sentence, `We build security practices.`, set at **80px across
nearly the full 1440 measure**, with enormous air above and below and nothing else in the
first screen except a single mint button. Then a hard colour-band change to warm grey for
the next section, with a circular badge medallion straddling the boundary.

This is the closest of the four to what I have been building, and the gap is instructive:
their headline is 80px spanning the full width; mine was 60px inside a half-width column.
Same idea, a third of the conviction.

**Take:** one sentence at real display scale across the full measure, and the hard
colour-band section change instead of a hairline rule. **Leave:** Poppins, and a hero that
says what the firm does rather than what the visitor's week looks like (RULE-2026-09-15-C
puts the buyer's pain first).

## kellyshortridge.com

Measured: font `Source Sans Pro`, one family. Type sizes `15, 19, 33`. 2 text colours, 3
backgrounds, 0 images, 0 SVG, 1 shadow.

**What it proves:** the most restrained page of the four, one typeface and three sizes, and
it still reads as a person rather than a template because the content is specific and the
structure is a plain list. It is the control case for "is restraint enough": it works here
because the page is an author's index, not an offer.

**Take:** one typeface can carry a whole page. **Leave:** it has nothing for a cold buyer
in the first screen, which is what round 2026-09-15b's Print treatment already measured on
this site as reading "thin" and "incomplete" to 3 of 3 readers.

---

## What the four have in common, and what all my rounds were missing

Every one of them has **one ownable graphic idea**: the dithered bitmaps and dot matrix
(trailofbits), the drawn-diagram letterforms (inkandswitch), type at a scale nobody else
dares (latacora), the author's index (kellyshortridge).

My rounds had none. They had a layout, a texture and a blue circle. A texture is not an
idea, which is exactly why Paper, Screen and Print read as the same page three times.

**The three things worth stealing into the next round, ranked:**

1. **A real display scale.** 80px across the full measure, not 60px in a half column
   (latacora, measured).
2. **Proof as chrome, not as a section.** A mono counter bar of real numbers in the header
   (trailofbits, measured). He has real ones and they are currently nowhere.
3. **One ownable graphic idea, drawn.** The log is the obvious candidate: rendered as a
   real technical artifact on graph paper with a hand annotation, not as a bordered HTML
   box (trailofbits + inkandswitch).

Each of those becomes a `craft-manifest.json` entry citing the site it came from, so the
build cannot quietly drop it and the parity check can see if it did.
