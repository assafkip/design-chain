# Art-direction canon — the visual-design principles the LEAD lens reads

This is the codified visual-design literature the **`art-direction` LEAD lens**
reasons from. It is the craft-and-concept twin of `attention-canon.md`: that canon
is the usability floor (a page that works); this one is the art-direction ceiling-
reach (a page that has a subject, a composition, and an idea). The lens reads THIS,
not a live web search.

Each principle carries: a name (the `id` in backticks, referenced by
`lens-registry.json` and checked by `verify_design_room.py`), a real named source,
what it says, and the one **testable question** it implies for a page. Questions,
not pass/fail rules — this canon raises gaps and hands up; it never scores beauty.
(The floors in `attention-canon.md` are CONSTRAINTS on the vision this canon sets,
not the other way around.)

The canon is organized by the three layers the LEAD lens runs:
**L1 CRAFT** (is there a subject? is it composed? bespoke or default?),
**L2 CONCEPT** (is there ONE distinctive, ownable idea?), and
**L3 TRUTH** (right for THIS product, ownable by THIS brand, resonant with THIS
buyer — which the tool REFUSES to score and hands to the founder + a real buyer).

---

## L1 — CRAFT (subject, composition, finish)

## `figure-ground` — is there a subject, separated from its ground?
- **Source:** Koffka (1935), *Principles of Gestalt Psychology*; the figure-ground
  organization of perception.
- **Says:** Perception first splits a scene into a **figure** (the subject the eye
  locks onto) and its **ground** (everything behind it). An image reads only when one
  thing is clearly the figure. A page that is all evenly-weighted UI chrome on one
  flat plane has no figure — nothing to look at.
- **Testable question:** What is the figure (the hero subject) of this page, and is it
  clearly separated from its ground? If you cannot point at the subject, there isn't one.

## `visual-literacy-elements` — is it composed, or defaulted?
- **Source:** Dondis (1973), *A Primer of Visual Literacy*.
- **Says:** Every visual message is built from basic elements (dot, line, shape,
  direction, tone, color, texture, scale, dimension, movement) arranged with
  deliberate techniques (contrast, balance, tension, emphasis). Composition is that
  deliberate arrangement; its absence is not neutral — it reads as accidental.
- **Testable question:** Which visual elements carry this composition, and is their
  arrangement deliberate (contrast, balance, tension) or did the elements just land
  where a default layout put them?

## `universal-principles` — is there a focal point and a hierarchy?
- **Source:** Lidwell, Holden & Butler (2003/2010), *Universal Principles of Design*
  (focal point; hierarchy; figure-ground; alignment; similarity).
- **Says:** Cross-domain design principles govern whether a layout reads as composed:
  a single focal point pulls the eye; hierarchy orders what comes next; alignment and
  similarity bind the parts. Equal-weight blocks with no focal point flatten into a
  list.
- **Testable question:** Name the focal point and the hierarchy after it. Is there one
  clear focal point, or do equal-weight blocks flatten the page into a stack?

## `bespoke-vs-default` — does this look made, or assembled from a kit?
- **Source:** Internal scar `design-room-blind-to-art-direction` (2026-06-25): pages
  passed every gate yet shipped a **library-default look** — an untouched component
  kit with no art direction. (Craft-floor; no academic claim needed — it is the
  failure this rebuild exists to catch.)
- **Says:** A page assembled from default components, default type, and default
  spacing signals that no one art-directed it. Bespoke choices (a custom subject, a
  considered type pairing, an owned motion moment) are the difference between "made"
  and "assembled."
- **Testable question:** What on this page is bespoke — made for THIS page — versus
  lifted untouched from a component library? If the answer is "nothing," it is default.

## L2 — CONCEPT (one distinctive, ownable idea)

## `the-big-idea` — is there ONE idea, or a pile of features?
- **Source:** Sullivan (1998), *Hey Whipple, Squeeze This* — "the big idea."
- **Says:** Memorable work rests on a single big idea, not a list of features or
  benefits. The idea is the thing remembered after the page is closed; without it the
  page is forgettable even when every feature is present.
- **Testable question:** What is the ONE idea of this page, stated in a sentence that
  is not a feature list? If you can only list features, there is no idea.

## `have-something-to-say` — is there a point of view?
- **Source:** Arden (2003), *It's Not How Good You Are, It's How Good You Want to Be*.
- **Says:** A design with nothing to say defaults to decoration. Ambition and a point
  of view come before craft; the work has to believe something. Polish on top of no
  point of view is still empty.
- **Testable question:** What does this page believe that a competitor's page does
  not? If it has no point of view, craft will only decorate the emptiness.

## `concept-as-sketch` — were divergent concepts generated, or was the first idea taken?
- **Source:** Buxton (2007), *Sketching User Experiences* — sketch to widen the design
  space before choosing.
- **Says:** The right design emerges from generating many divergent alternatives early
  (cheap sketches) and only then choosing. Taking the first idea collapses the design
  space before it was explored; getting the design right requires first getting the
  right design.
- **Testable question:** Were at least three distinct concepts generated as forks for
  the founder to choose from, or did the build take the first idea and style it?

## L3 — TRUTH (right for this product, this brand, this buyer)

## `reflective-design` — does it work at the reflective level, not just the behavioral?
- **Source:** Norman (2004), *Emotional Design* — the visceral / behavioral /
  reflective levels.
- **Says:** Design works at three levels: visceral (the gut 50ms look), behavioral
  (usability), and reflective (meaning, identity, "is this me?"). The usability floors
  cover only the behavioral level; the visceral and reflective levels are a separate
  axis (Kurosu & Kashimura's apparent usability) the floors never measure.
- **Testable question:** At the reflective level — identity and meaning — is this page
  ownable by THIS brand and resonant with THIS buyer? The tool does not answer this; it
  hands the question to the founder's eye and a real buyer.

## `quality-without-a-name` — the part no checklist can score
- **Source:** Alexander (1979), *The Timeless Way of Building* — "the quality without a
  name."
- **Says:** The deepest rightness of a made thing cannot be captured by a checklist or
  a score; it is recognized, not measured. Any tool that claims to score it is
  substituting a proxy for the thing.
- **Testable question:** REFUSED. The tool does not score resonance or "quality." It
  emits the gap-list from L1 and L2, surfaces the L3 question, and hands the page to
  the founder's eye and the market. The founder's eye + the market are the only ceiling.

---

## How the LEAD lens uses this canon
- The lens runs **first** to set the bar from the reference's design decisions (read
  through these principles), and **last** as a visual-diff critic (does the build have
  a figure, a composition, a focal point, an idea?).
- It emits the same shapes the other lenses do: a **cited** gap ("principle `<id>`
  implies question Q; the page does / does not answer it"), or a **fork** (concept
  forks the founder resolves). It NEVER resolves its own fork and NEVER scores beauty.
- L3 (`reflective-design`, `quality-without-a-name`) is a **refusal**, not a score:
  the tool hands resonance to the founder + a real buyer. A tool that scores resonance
  is the failure mode this canon exists to prevent.
