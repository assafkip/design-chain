<!-- voice-lint-skip -->
# Design narrative: what defines this group

Exemplars named by the founder 2026-09-15: squarespace.com, calendly.com, stripe.com,
notion.com, figma.com. Captured in a real browser at 1440x900 and 390x844;
every figure cited here is in `MEASUREMENTS.md`, which the capture script regenerates and
which is not hand-edited.

**Rewrite this whole file whenever an exemplar is added.** Founder, verbatim: "create a
design narrative of what are the style elements that define this group? What is what are
the similarities with regards to the design elements and usage of the tools in the design.
And you should do that every time I put in more exemplars." The point is the GROUP, so a
sixth site changes what the other five mean and the narrative is re-read rather than
appended to.

**canva.com is DROPPED from the set, founder-directed 2026-09-15: "Just drop canva."**
Every capture returned its bot-wall page ("We'll have you designing again soon", 28px, one
SVG, zero buttons, two type sizes). Those numbers describe an error page, not Canva's
design. Leaving it in was not neutral: `design-gap-check.py` derives its floors from the
least any exemplar reaches, so the canva row pulled the background-colour floor from 3 down
to 1 and would have pulled the rest with it. A failed capture that silently LOWERS a bar is
the same defect class as a skipped check reading as a pass. Its capture and screenshots are
in `_dropped/`, not deleted, so re-adding it with a real browser profile stays possible.

**The group is therefore five, and this narrative is the read of those five.**

**Six from 2026-09-21: informationisbeautiful.net joins, founder-directed** ("look at the examples
on this site and evaluate what we should use", then "yes" to making it an exemplar). It is read in
section 16 against the other five, and it changes the group in a specific way: the first five are
product landing pages, this one is a data-storytelling practice, so it is the group's only source
for HOW a claim is shown against its evidence. Where it breaks sections 1 to 3 it is named there.

---

## 1. The single strongest signal: nobody here uses a font you can download

Five for five:

| Site | Display family |
|---|---|
| Squarespace | Clarkson |
| Calendly | Calendly Sans |
| Stripe | sohne-var |
| Notion | NotionInter |
| Figma | figmaSans |

Every one is proprietary or licensed-and-renamed. Not one uses Inter, Roboto, Geist, Plus
Jakarta or any other Google default. (Calendly loads Geist as a secondary, but its display
is Calendly Sans.)

This is the clearest thing separating this group from a generated page, and it is the one
thing no amount of layout skill substitutes for. It is also the most expensive: a licensed
text family is real money, and a bespoke one is a commission.

**For askconsulting:** this is a founder decision with a price tag, not a design decision I
can make. The options are a licensed family from a real foundry (Commercial Type, Klim,
Grilli, Dinamo: hundreds to low thousands for web), a strong open family that is NOT on the
converged list (the impeccable detector flags Inter, Roboto, Fraunces, Geist, Plus Jakarta,
Space Grotesk; Literata and Public Sans, currently in use, are not flagged), or accepting
that the type will not be the thing that distinguishes the page.

## 2. The display line: big, light-to-medium, and tracked TIGHT

| Site | px | weight | tracking | % of viewport | words |
|---|---|---|---|---|---|
| Notion | 96 | 600 | -4.6px | 87% | 5 |
| Calendly | 72 | 500 | -2.0px | 44% | 6 |
| Squarespace | 64 | 300 | -3.84px | 100% | 3 |
| Figma | 56 | 400 | -1.25px | 23% | 6 |
| Stripe | 48 | 300 | -0.96px | 64% | 6 |

Three things are consistent and none of them were in any round I built:

- **Negative tracking on every single one**, from -0.96px to -4.6px. At 96px Notion pulls
  4.6px out of every gap. My rounds used -0.018em, which at 60px is about -1.1px: in range,
  but at the bottom of it and at two thirds the size.
- **Weight 300 to 600, never 700.** This group sets big type LIGHT. My display was 700.
  That single choice is a large part of why mine reads heavier and cheaper.
- **Three to six words.** Not a sentence with a subordinate clause. Mine was six ("By hand:
  74 rows over days"), which is in range.

**For askconsulting:** the cheapest real upgrade available. Take the display to 72 to 96px,
drop the weight to 400 to 500, and set tracking to about -0.05em. Costs nothing and is the
difference between latacora's conviction and my half-column 60px bold.

## 3. Almost no gradients on type, and almost no shadows anywhere

Gradients in the fold: Calendly 0, Stripe 0, Notion 0, Figma 0, Squarespace 9 (all video
overlay scrims). Shadows: Squarespace 0, Stripe 1, Figma 2, Calendly 2, Notion 4.

The group is essentially flat. Depth comes from colour fields and layering, not from
drop shadows, and never from gradient text. This agrees exactly with `site-design.md`
section 7, which bans gradient-on-type as the number one AI tell.

## 4. Vector, not photography

SVG counts in the fold: Calendly 64, Stripe 46, Figma 11, Squarespace 8, Notion 5.
Photographs: Squarespace 20 images and 5 videos (it sells websites, so it shows them),
Notion 15, everyone else close to zero.

The default illustration medium here is inline SVG, drawn. Not stock photography, not
generated scenes. `design-dna.md` section 4 already says imagery is real records recreated
and annotated, never stock, which puts askconsulting in the same family: draw the artifact,
do not photograph a desk.

## 5. Motion is interaction, not ambience

Transitioned elements against animated ones in the fold: Stripe 211 vs 1, Squarespace 146
vs 0, Calendly 41 vs 0, Notion 36 vs 1, Figma 18 vs 0.

The ratio is roughly 40:1. These pages barely animate on load; they respond richly to the
pointer. Nothing on them is moving while you read.

**For askconsulting:** my rounds had exactly one load animation and zero interaction
states. The group does the opposite. That also settles the one-reveal tension in
`design-dna.md` section 4 in a useful direction: a page can be very still and still feel
alive, if every control answers the pointer.

## 6. Two radius tiers, and small ones for controls

Controls sit at 4 to 8px (Stripe 4/6, Notion 4/8, Figma 2/8, Squarespace 4/6/8). Chips and
avatars go fully round (Notion 9999, Figma 9999, Calendly 33554400). Calendly is the
outlier with 16 to 20px on its panels, which is what gives it a softer, more consumer feel
than Stripe.

There is no middle. Nothing here uses the 12px "friendly SaaS card" radius.

## 7. Body text is 14 to 16px, and the measure is narrow

Size ramps: Stripe [14, 16, 32, 48]. Figma [16, 18, 30, 56]. Calendly [12, 14, 16, 18, 36,
72]. Notion [12, 14, 16, 20, 22, 72, 96]. Squarespace [10, 12, 14, 15, 16, 64].

Two patterns: a body of 14 to 16px (not 21px, which is what I used), and a HARD JUMP to
the display with little in between. Stripe goes 16 to 32 to 48 and has nothing else.
Notion goes 22 to 72. The gap is the drama.

This is where `site-design.md`'s own three-sizes-under-40px rule and this group agree:
Stripe uses exactly two sizes under 40px. My rounds used three and felt busier.

## 8. Where the group COLLIDES with your canon, and you have to decide

This is the part not to smooth over.

- **Stripe's brand colour is `rgb(83, 58, 253)`, a saturated violet.** `site-design.md`
  section 7 bans "violet or indigo accents" as an AI-default tell, and the kipi-design
  tripwire blocks on it. The best-regarded page in this set uses the exact hue our gate
  treats as slop.
- **Calendly's entire hero is a blue-to-violet-to-pink gradient field.** Same rule.
- **Calendly runs two CTAs side by side** ("Sign up with Google", "Sign up with
  Microsoft"). Section 7 lists two side-by-side CTAs as a tell.
- **Stripe's hero art is a soft chromatic ribbon**, which is decoration in the sense
  `design-dna.md` section 4 rejects: it depicts nothing and carries no information.

The honest reading: the AI-default fingerprint is a list of moves that became cheap because
great companies made them famous. Our gate cannot tell the difference between Stripe using
violet with a custom typeface, a licensed gradient render and a 1.7% live GDP counter, and
a generated page using violet because the model reached for it.

**This needs your call, and it is one line either way.** Either the canon's ban stands and
we take everything from this group EXCEPT the palette and the gradients, or the ban softens
to "not the default violet, and never with the other tells present", and the tripwire's
rule changes with it. I am not going to quietly build against a banned palette and I am
not going to quietly drop the reference either.

## 9. Two moves this group makes that askconsulting can take today

- **A live number as chrome.** Stripe puts `Global GDP running on Stripe: 1.71620584%`
  ABOVE the headline, small, in a lighter weight. It is proof as furniture, the same move
  trailofbits makes with its publication counters. You have real numbers and they are
  currently nowhere on the page.
- **Colour shifts inside the sentence.** Stripe's headline runs dark, then the second half
  drops to a lighter blue-grey. The sentence carries its own emphasis without bold, without
  a highlight box, without a second type size. That is one way to have a large line and
  still respect the three-sizes rule.

---

## 10. The drawing tool: the explainer-visuals skill (added 2026-09-16, round 16c)

Founder, 2026-09-16: "You need to use the design tools for the drawings." This is the tool,
torn down the same way as the exemplars.

- **What it takes from the idea.** Its format selection table maps the concept type to a
  format. A process maps to a stepped animation, a proportion to an animated unit chart.
  The core belief is both, so the hours become units that travel the process.
- **Readable at rest.** Its first principle: the settled state says the whole idea with no
  motion. That matches the group, where nothing needs to move to be understood.
- **Accessibility.** A labelled figure, a full text caption, reduced motion honoured, a
  keyboard control.

Where it COLLIDES with sections 4 and 5, stated rather than hidden:

- Section 4 says the group draws in inline SVG. The skill builds from HTML and CSS, so the
  round 16c drawing is bordered boxes, not SVG.
- Section 5 says the group responds to the pointer and barely animates on load. The skill's
  unit chart is a load animation. The founder asked for motion he can see (round 16b), and
  the Replay control is the only pointer-driven part.

## 11. The motion tool: the hyperframes-animation skill (added 2026-09-16, round 16d)

Founder, on round 16c: "We have really good animation tools with motion and I dont think
you used them. The design is very simply still." This is the tool, torn down.

- **What it is.** A library of atomic motion recipes composed on one GSAP timeline, plus
  scene blueprints. The recipes used in round 16d: svg-path-draw (outlines draw like a pen,
  no bounce), svg-icon-enrichment (dash flow, pulses), counting-dynamic-scale (numbers that
  pop and stay correct under seek), motion-blur-streak in its echo form (the drip), and
  ambient-glow-bloom (a bounded breathing glow).
- **What it answers in this file.** Section 10 said the explainer-visuals drawing was boxes,
  not SVG. This one is inline SVG, which is section 4's group default. Section 5 says the
  group answers the pointer; the scene now shifts in two depth layers under the pointer.
- **Where it still collides.** Section 5 also says the group barely animates on load. This
  scene tells its story on load and loops it with a rest. The founder asked for motion he
  can see twice (rounds 16b and 16c), so the collision is kept on purpose, and the loop
  pauses when the figure is off screen.
- **A rule it brings that matters for a site.** Everything is seek-safe: a count is derived
  from the playhead, not from a callback. Round 16d's first build broke that and its own
  test caught it.

## 12. The panel, the centre line and the hand: what round 16e takes (added 2026-09-16)

Founder on round 16d: "yeah its too polished and the text is again on lined on the left",
"I think the background is still not how it looks in the examples."

- **The panel, measured.** calendly's colour is not the page. It is a rounded panel inset on
  an off-white page (#fcfbf8), with the header above it on the page. Pixels sampled from
  `calendly-com-laptop.png`: #265994 and #3875be where the words are, #6f90dd and #9a99e7
  lower down. Rounds 16b to 16d painted a dark violet field edge to edge, which none of the
  five does. Four of the five are light pages.
- **The centre line.** squarespace, calendly and notion centre the headline and put the
  work under it, overlapping the fold. stripe and figma do not, so this is the majority
  move, and the founder has asked for it twice.
- **The hand: rough.js.** A library that redraws SVG shapes as if sketched, with a seed so
  the same drawing comes back every visit. It answers "too polished": the diagram reads as
  someone drawing the problem on paper, not a rendered product shot. It keeps section 4
  (vector) and section 11's motion; it removes the gloss.

## 13. The reveal: a recreated record, annotated (added 2026-09-16, round 16k)

Founder, on the section under the hero: "don't tell the visitor that this works. Let them
inspect something real enough to conclude that it works." Section 4 already names the move
(imagery is real records recreated and annotated); this is where it is applied first.

- **The record.** The research team's deliverable sheet, redrawn in the same hand as the
  hero (rough.js, fixed seeds): its real column headers and evidence numbers, every cell's
  content redacted with hatched bars, one row that failed struck through.
- **The notes.** Two or three hand notes in the accent blue, each pointing at the cell it
  explains: what the system did, what it flagged, where the analyst's judgment stayed. The
  notes carry the argument; the sheet carries the proof.
- **The motion.** Section 5 again: nothing loops. The sheet fills in once, row by row, the
  first time it scrolls into view, and reduced motion shows it finished.
- **Where it collides.** Stripe, Figma and Calendly show their own product under the
  headline. This page has no product screenshot to show, so the recreated record stands in
  for it, and it is labelled as a recreation in its accessible description.

## What this changes about the next round

1. Display goes to 72 to 96px at weight 400 to 500 with about -0.05em tracking, and body
   drops to 16px. Sections 2 and 7.
2. The type family becomes an explicit founder decision with a price, not a default.
   Section 1.
3. The artifact is drawn as inline SVG rather than built from bordered divs. Section 4.
4. Motion moves from one load reveal to interaction states on every control. Section 5.
5. A real number goes in the chrome above the headline. Section 9.
6. Palette and gradients wait on the section 8 decision.

Each of these becomes a `craft-manifest.json` technique citing this file, so the build
cannot drop it and `design-chain-gate.py` will say so if it does.

## 14. The hero drops to two abstract records, round 2026-09-18

Extends section 13's "a recreated record, annotated" rather than replacing it. RULE-2026-09-18-I
retires the hours drawing; RULE-2026-09-18-J keeps the record stays abstract, no specific document
type, no client engagement, because the reader could be any segment. Three techniques carried the
build:

- **The abstract claim and source records.** Two hand-sketched panels, "the claim" and "the
  source," on section 12's one-baseline-composition, instead of one recreated sheet. The
  hachure-and-outline hand is section 13's; the content inside is deliberately generic (two lines
  suggesting text, not a real document's fields), which is what "abstract" means here.
- **The panel gradient, carried forward.** The full-bleed dark panel from round 2026-09-16e
  onward (`#265994` to `#3875be` to `#9a99e7`, interpolated in oklab per the 2026-09-17 Decision
  log entry) is the ground the new drawing sits on, unchanged from the live hero.
- **White ink on the panel.** Since round 16h, drawn strokes are white against the blue panel, not
  the site's default ink. The new records keep that rule. It creates a real, named tension: the
  site's signal color for "the mismatch" cannot read against a blue background of nearly the same
  hue, so the disagree state is carried by motion (a faster, harsher double-strike) instead of
  color. Recorded, not hidden, in the round's own `critique.md`.

## 15. The seam's grammar on a white sheet, round 2026-09-21

Founder, 2026-09-21, four picks (`specs/hero.md`). Supersedes section 14's white ink on the panel
and its "carried by motion instead of color" workaround.

- **The seam's grammar.** Every outcome mark is `Seam.astro`'s (round 17g), not a new symbol: a
  flat faint line joins a matching pair; a blue line runs into the gap and stops at a small circle
  where the partner is missing; an ink line starts across and stops short where the check cannot
  tell. Rows keep Seam's row vocabulary (a box, a kind mark, a rule for content).
- **A white sheet inside the panel.** The drawing sits on white, inset in the blue panel, as round
  16e did, so ink is ink and the signal colour `#3875be` appears only on the mismatch.
- **Motion that holds.** Section 11's pen-draw and loop with a rest, plus one beat that is new: the
  unsure line visibly pauses before it stops, because the pause is the claim. Section 5's pointer
  half stays: hovering a row lights it on both sides.

## 16. informationisbeautiful.net: the evidence page, added 2026-09-21

Captured by `design-exemplar-capture.py` (1440x900 and 390x844, `informationisbeautiful-net.json`),
and three pieces read in the browser the same day: "Vaccines & Autism: what does the evidence say",
the plastics flow, and the home gallery.

**What it brings that the other five do not.** A way to put a claim next to its evidence so it reads
in seconds. The vaccines piece: the finding as a one-line headline with its key words coloured; one
row of the evidence underneath, each source a circle sized by its weight with a two-line label; one
"sources" line under the row; a line chart with a callout pinned to the moment that matters. No
paragraph anywhere above the fold. That is `design-dna.md` section 4's one idea, drawn by somebody
whose whole practice is this. Its gallery also shows the other moves for "how many" without a
sentence: a grid of repeated marks, a flow whose branches thin as things leak out of it.

**Where it breaks the group, measured, not smoothed over.**
- Section 1 (nobody uses a downloadable font): it does. Quicksand and IBM Plex Sans, both free.
- Section 2 (big, light, tracked tight): its display is 36px at weight 700, tracking normal.
- Section 3 and the one-signal-colour rule: its pieces run many colours each. The canon keeps one
  signal colour; what transfers is colour ON the key word, not the palette.
- Motion: 15 transitioned elements and 0 animated in the fold, so it agrees with section 5.
- It is the only exemplar whose fold carries 0 inline SVGs (its art is raster). Floors that
  `design-gap-check.py` derives from the least any exemplar reaches can move DOWN because of it;
  that is a real capture of a real site, unlike the dropped canva wall page, so the lower floor is
  recorded rather than refused.

**For askconsulting (founder picks of 2026-09-21, `specs/hero-flow.md`).** Round 16d's motion
carries the hero; this site supplies the shape of the section under it: a short row of labelled
marks instead of a paragraph, and colour on the one key word of the headline.
