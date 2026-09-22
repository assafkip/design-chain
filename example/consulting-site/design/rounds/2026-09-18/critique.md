# Critique — nine questions, design-dna.md section 7

Answered per direction after personally viewing all three built pages (seeked GSAP timelines to
specific checkpoints, screenshotted, not relayed from a build log).

---

## D1 — Two cards, a symbol in the gap

1. **One thing this screen says, buyer's words:** "is the automation really working?" (cluster A)
   answered visually: here's the check.
2. **Reader, their week, what they feel:** someone paid to be accurate, whose system just claimed
   something is true. They feel the same doubt the headline names.
3. **Where are the two records:** unambiguous. Two labeled panels, side by side, on one baseline.
4. **Could this be anyone else's page:** partly. The claim/source panel pair is a comparison
   layout any consultancy could use. What makes it his: the third state (can't confirm) and its
   label, "Unsure? It stops."
5. **Decoration:** none found. Every mark (check, X, question glyph) carries a real outcome.
6. **What would he say is "pretending to work":** nothing currently — but the disagree mark uses
   white on the panel blue rather than the site's actual signal color, because the signal blue
   IS the panel background here. That's a real, named tension (see item 7), not hidden.
7. **Claim without its source:** the disagree-mark color choice has no source beyond this build's
   own necessity. Flagged in the code, not resolved.
8. **Would it hold up shown to who he answers to:** yes, the mechanism is legible and the "stops"
   state is the one nobody else's page has.
9. **Chosen because it was the default (3+):** the checkmark shape (a generic three-point tick,
   not derived from anything site-specific); the panel dimensions (220x130, matched to the old
   hero's expert box rather than derived fresh for this content); the gap width between panels
   (chosen for visual balance, not measured against anything).

**Weakest answer:** #4 and #6 together — the mark vocabulary (check/X/question) is the least
original part of the direction. The two-records IDEA is distinctive; the SYMBOLS resolving it are
not.

---

## D2 — Two cards, position instead of symbol

1. **One thing this screen says:** the same claim, argued through space instead of a symbol:
   agreement IS alignment.
2. **Reader, week, feeling:** same as D1.
3. **Where are the two records:** clear for "today" and "agree." Weaker for "disagree" (visible,
   confirmed live: source panel drops and shifts, a real offset) and **broken for "unsure"**
   (confirmed live: the panels sit essentially aligned, same as "agree," with only the question
   mark and the text label distinguishing the state — the "no added glyph" pitch fails on exactly
   the state `site-design.md` section 11 calls "the only part that is his").
4. **Could this be anyone else's page:** the alignment-as-meaning mechanic has no obvious analogue
   in the exemplar set — more original than D1, at the cost of #3's failure.
5. **Decoration:** the question mark IS decoration in this direction specifically, since the
   position mechanic was supposed to carry can't-confirm without it, and in practice can't.
6. **What would he say is "pretending to work":** the "unsure" state's wobble. It claims to be a
   distinct visual state and is not one, confirmed by looking at it, not assumed.
7. **Claim without source:** directions.md's own claim that "no added glyph for agree/disagree,
   only for can't-confirm" — the built page contradicts this for exactly the can't-confirm case.
8. **Would it hold up:** not as built. The core differentiator doesn't read.
9. **Chosen because default (3+):** the offset direction and distance (right and down, arbitrary);
   the wobble amount for unsure (too small to read, effectively arbitrary); reusing D1's checkmark
   shape unchanged for the "agree" case even though D2's whole pitch was to need fewer symbols.

**Weakest answer:** #3. This is the direction's central promise failing on direct observation, not
a matter of taste.

---

## D3 — One record, an annotation that resolves

1. **One thing this screen says:** narrower than D1/D2 — "here's a flag on a record," not visibly
   "two records disagree."
2. **Reader, week, feeling:** same buyer, but the screen argues a weaker version of the diagnosis:
   confirmed live, the built page shows ONE outlined panel labeled "THE RECORD" with a circled mark
   on it. Nothing on screen represents a second record or a source to check against.
3. **Where are the two records:** **not visibly present.** This is the direction's core weakness,
   named in directions.md before building and confirmed after: "it's really one record with a
   flag," not the two-records idea RULE-2026-09-18-D called FIELD-CONFIRMED.
4. **Could this be anyone else's page:** yes, more easily than D1 or D2 — a circled flag on a
   document is a generic error-marking pattern, not specific to "two records that should agree."
5. **Decoration:** the circle around the mark is closer to decoration than D1's gap-placement or
   D2's position, since it doesn't carry information beyond "here's the spot."
6. **What would he say is "pretending to work":** the label "THE RECORD" — singular — while the
   headline and section 2 both argue a claim-vs-source comparison. The label and the mechanic
   disagree with the page's own words, ironically the exact defect the whole redesign exists to
   catch.
7. **Claim without source:** none new; this direction just under-delivers on the one idea rather
   than making an unsourced claim.
8. **Would it hold up:** weakest of the three. It answers the "is it true" question about one
   thing, not the "does it match" question the headline poses.
9. **Chosen because default (3+):** the circle-annotation shape (the most conventional "flag this"
   UI pattern available, not derived from the site's own hand); the record's centered single
   position (no reason given beyond "there's only one now"); the label "THE RECORD" (a placeholder
   name that was never reconsidered once the mechanic dropped to one object).

**Weakest answer:** #3, same shape as D2's weakness but more fundamental — D2 fails to fully
deliver the idea in one state; D3 doesn't structurally carry the idea at all.

---

## Cross-direction summary

D1 delivers the one idea most reliably and has the least original mark vocabulary. D2 is the most
original mechanic and fails its own central claim on the state that matters most. D3 is the
cleanest single build and the weakest argument for "two records" specifically. Nothing here was
softened to make picking easier.
