# Home — hero + section-under-hero, 2026-09-18 fixes

Spec for the build-fix items walked in the vision session (`site/design/VISION.md`) against
the currently sealed round `site/design/2026-09-17g`. Source rules: RULE-2026-09-18-A through K in
`decisions.md`, section 11 of `site-design.md` (beats + guardrail), `NARRATIVE.md` section 13
(technique reused for Record A/B).

`REVIEWED BY FOUNDER:` <!-- add the date here once this spec is actually reviewed, not before -->

---

## 1. Second drawing — removed

The "Pile" component (Reads/Retypes/Chases/Checks walkthrough, currently rendered below the hero)
comes out of Home entirely. RULE-2026-09-18-C: "Home has ONE drawing." Nothing replaces it in
drawing form — that space becomes section 2 below.

**Decided.** No open questions here.

---

## 2. Section under the hero — words and links — DECIDED, RULE-2026-09-18-K

Per RULE-2026-09-18-C item 4: answers what the $1,000 week actually is (122 of 327 ICP-persona
statements asked this) and where the proof lives (149 say there's no proof, 240 want a real
example). Links to `/start` and `/work`. Per RULE-2026-09-18-B item 2, still binding: no client, no
engagement, no number, no recreated record here, proof lives on Work/case pages, this section only
points there.

**Final copy:**

> Some of this is still done by hand. Some of it's automated, and you still don't trust it. Either
> way, when what your system says stops matching what's actually happening, that's where the money
> goes. When the automation breaks, it's busy work again.
>
> For one week, $1,000: you show me what your system says, and what's actually happening. I watch,
> I don't touch, until you say go. What you get back in writing: a count of what's actually
> slipping, what it's costing, and priced options for fixing each one.
>
> Every system I've shipped is on the Work page, including what it got wrong.

Links: "See the assessment" to `/start`, "See the work" to `/work` (both already-used phrases, not
new). No heading, continuous prose under the hero, per `NARRATIVE.md` section 7's body-copy
economy.

---

## 3. Hero — REBUILT, RULE-2026-09-18-I (supersedes the hours mechanic below)

The 8-hours/2-hours structure is gone. Found mid-spec: the hero's "Today" lane (work arrives by
email/calls/PDFs, a human types it in) is the shape of the SUPERSEDED Aug-24 belief, not the
corrected diagnosis. `working_belief`'s own `not_this`: *"Not 'they do too much by hand'. The
retyping clause... appears zero times in 83 posts."* Removing one verb (RULE-2026-09-18-H) fixed a
symptom; the premise itself needed to change.

**New mechanic — `design-dna.md` section 4's one idea, applied literally, technique reused from
`NARRATIVE.md` section 13 ("a recreated record, annotated," built once already for the now-retired
section-under-hero drawing, round 16k):**
- **Record A: "the claim."** What the system reports. Stays ABSTRACT, no specific document named
  (RULE-2026-09-18-J: founder, *"abstract because we dont know exactly who from the icp is going to
  read this"*, so it reads the same across CPA, law, A&E without widening to one vertical).
- **Record B: "the source."** What it should trace to. Also abstract, same reason.
- **Today:** the two sit side by side. Nothing shows whether they agree.
- **After the build, three states, not a binary:**
  - **Agree** — a plain ink checkmark, not the signal color.
  - **Disagree** — the signal blue (`#0066b3`), the one legitimate use of it here, since this IS the
    mismatch the color is reserved for.
  - **Can't confirm** — "Unsure? It stops." Its own distinct shape, not blue, not the plain check.
    Native to the mechanic as its third outcome, not a bolted-on fifth box.

**Headline:** *"Automated. But is it true?"* SUPERSEDES RULE-2026-09-16-F's "Your team works more
hours than it bills." Reached by weighing three candidates — two closer to the ICP's own
question-shaped words ("is the automation really working?"), one closer to the founder's own
declarative register — then picked a fourth combining both: declarative clause, then a question.

**Labels carried over, now native to the mechanic instead of add-ons:**
- **"Checking it's actually true."** — the verification action itself (was: the blank "2 hours of
  judgment" box).
- **"Unsure? It stops."** — the can't-confirm case. Stands apart visually from anything else in the
  drawing (decided), NOT via the signal blue (`#0066b3` means the mismatch only, per `design-dna.md`
  section 4 — beat 3 isn't a mismatch, it's a refusal to guess, a different meaning; spending the
  one signal color on it breaks the rule the site holds everywhere else).

**OPEN — the drawn form.** Content and mechanic are decided, pixels aren't:
- The abstract drawn shape for "the claim" and "the source" (two labelled panels? two simple marks
  joined by a line?) is not picked.
- "Can't confirm"'s specific shape is a candidate only (a dashed outline, a hand-drawn question
  mark), not picked.
- No sub-line drafted yet for the new headline (the old one, RULE-2026-09-16-F, had one with no end
  period; this headline doesn't have a replacement yet).
- Word/piece/line caps (`design-chain.json`: `max_hero_words: 18`, `max_hero_pieces: 2`,
  `max_hero_lines: 3`) not yet checked against the new headline + labels together.

---

## What's blocking a build right now

Sections 1 and 2 are ready. Section 3 has a mechanic and two labels but zero visual execution, this
is a from-scratch drawing, not a relabel of the existing one. A build today would only be sections 1
and 2; section 3's drawn shapes still need design work before anything gets built.
