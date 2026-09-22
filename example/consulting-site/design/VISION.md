# askconsulting.io — Vision

Running notebook. Your words, dated, kept verbatim. This file is read by `design-chain-gate.py`
(`vision_problems()`) before any round can brief: needs 3+ blocks shaped like the ones below,
and the brief has to quote one of them.

---

<!-- Each entry: **Founder, YYYY-MM-DD:** "verbatim quote" then 1-2 lines of why it matters. -->

**Founder, 2026-09-15:** "we're not going to have people playing around on the site. They need to hit
the site and immediately understand how I can help them and be wowed by my capabilities and my
pedigree... These are professionals that are looking to alleviate some of their pain. It needs to
treat them that way, but at the same time be impressive."
Source: `decisions.md` RULE-2026-09-15-H. What the page is FOR: instant understanding + wow, no
interaction required to get it, professional tone not playful.

**Founder, 2026-09-15:** "The site is a manifestation of how good I am with AI... simple. Looks like
slop sloppy or just bad - that is my calling card and it makes me look bad."
Source: `design-dna.md` section 10. The page IS the proof, not a description of proof. Craft is not
optional restraint territory.

**Founder, 2026-09-18:** "decouple from the actual down in the weeds facts of each project and each
case. We are telling a story, we are not recounting facts... the concept of what the ICP wants and
what I can accomplish for them and how I can do it."
Source: `decisions.md` RULE-2026-09-18-B. The page is a STORY (one throughline: their want, his
capability, the mechanism), not an assembly of correct constraint-satisfying facts.

**Founder, 2026-09-15:** "these narrow down to a very specific customer that wants me to automate
their whole thing. Not all customers are that. Some customers are going to start with what is the
pain that they have."
Source: `decisions.md` RULE-2026-09-15-C. Starts from ONE pain, never the whole system.

---

**Note (this session, unconfirmed):** these four are pulled from `decisions.md` and `design-dna.md`
because the answer to "what is the page trying to BE" already existed there, dated and verbatim.
Three sealed rounds still went wrong with these on record — so the open question is not "what did
you say" but **which one of these is the single thing being missed when a round gets built.**

**Founder, 2026-09-18:** "I think the page is proof and the one story because we ended up having
two hero sections, and we weren't fully focused on the pain, which we just researched from all the
Reddit work."
His own diagnosis of the last sealed round: two components broke, not four. **Page-as-proof** and
**One story** failed together (two hero sections is one story told twice). **One pain first** failed
separately (the pain used wasn't the freshly-researched one). **Wow instantly** wasn't named as broken.

---

## Build reality check, 2026-09-18 (canon vs. current build, before components)

Checked against the live working tree at `site/design/2026-09-17g` (the sealed, deployed round —
161 uncommitted files right now, mid-rebuild) and today's decisions RULE-2026-09-18-A through G.
**Latest rule wins: C supersedes A's plan and part of B.**

1. **Home still has TWO drawings.** The hero's "8 hours / 2 hours judgment" comparison, plus a
   second "Pile" walkthrough below it (verbs: Reads, Retypes, Chases, Checks). RULE-2026-09-18-C:
   *"Home has ONE drawing... there is no second drawing under it."* This is the exact defect named
   above. **Fix: remove the second drawing entirely** — not replace it with Record 5, that plan
   (RULE-2026-09-18-A) is superseded by C.
2. **The section under the hero, once the second drawing is gone, becomes words and links** —
   what the $1,000 week actually is, and where the proof lives (links to Work/case pages). Not a
   drawing, not an inline client record. Unbuilt.
3. **Two named defects in the HERO drawing itself** (RULE-2026-09-18-C item 3): the "2 hours of
   judgment" box reads blank to readers (called out on its own, 23 ICP-persona gate runs); the
   system box's four verbs assert confident capability with no sign it refuses to invent an answer
   when it can't prove one — the one trait `the-business.md` calls uniquely his. Unbuilt.
4. **RESOLVED, 2026-09-18 (RULE-2026-09-18-H).** Founder: *"remove 'retype'."* The hero's system
   box drops to three verbs. The separate `segment-pain-model.json` conflict (RULE-2026-09-18-G)
   is untouched by this — that's the runtime pain model, not the hero drawing's copy.
5. **Record 5** (Client B, 441→388, 53 found) is publishable per today's permission grant
   (RULE-2026-09-18-A) but no longer belongs in the section-under-hero. Available for Work/case
   pages instead.

**What this means for "before we go into this":** items 1-3 are build fixes to the CURRENT sealed
round, decided today, not yet built. They come before any new component spec, because a spec
written against a page that still has the old two-drawing shape is specced against the wrong
target.

**Status, all three walked:**
1. Remove the Pile drawing — confirmed, nothing replaces it in drawing form.
2. Section under hero → words and links — confirmed, already what RULE-2026-09-18-C item 4 says.
3. Hero box content — picked: **"Checking it's actually true."** Logged `site-design.md` Decision
   log, 2026-09-18. Still needs the word/piece/line check against `design-chain.json`'s hero caps.

**Caught mid-walk:** RULE-2026-09-18-C item 3 named TWO hero defects. Only the first (blank
judgment box) got walked before jumping to a pick. The second — system box shows confident
capability with nothing saying it ever stops — is `site-design.md` section 11's beat 3, called
NOT OPTIONAL: *"where it cannot prove one it stops and says so rather than guessing."*
Shape decided: a small fifth element after the checklist (Reads/Chases/Checks), its own distinct
beat, not folded into the existing three. Label picked: **"Unsure? It stops."**

---

## Components (filled in once the vision has enough to break apart)

<!-- component name -> site/design/specs/<component>.md -->

---

## Hero picks, 2026-09-21 (design-chain round 2026-09-21)

**Founder, 2026-09-21:** "okay do it but you must run it through the design-chain workflow"
Why it matters: the Sep 18 hero was rejected as invented ("two boxes and a check mark") and as
motionless. This round builds D1 of `2026-09-18` again, from the site's own code, through the chain.

Four picks, made from options shown with their source (all four took the recommended option):
1. **The marks come from the seam** (`2026-09-17g/astro/src/components/Seam.astro`). Match: a flat
   line joins the pair. No match: a blue line drops into the gap and ends in a small circle, the
   seam's own mark. Unsure: the line starts, pauses, and stops halfway, "Unsure? It stops." The
   check, X and question mark in the Sep 18 specs are retired.
2. **Sub-line:** "I build the check that tells you, and it stops when it can't prove it".
3. **The drawing sits on a white sheet inside the blue panel**, so blue can mean "no match" only.
4. **The blue is `#3875be`**, the live one. The config's `#0066b3` is a separate mismatch for Sana.

Component spec: `site/design/specs/hero.md`.

**Founder, 2026-09-21:** "I really don't like this design. The former design was a lot clearer and also made a lot more sense about what we're doing. So, this specific design type doesn't fit with any of the exemplars that I provided, and also we have a large paragraph under it, and that we already said it doesn't work."
Verdict on round 2026-09-21 (all three directions). Two defects named: the drawing type matches no
exemplar, and the section under the hero is a paragraph block, which he had already ruled out.
Next reference he named: informationisbeautiful.net ("look at the examples on this site and evaluate
what we should use").

**Founder, 2026-09-21:** "16d is th eone I liked"
Asked which former design was "the one where the dots were moving across the page", shown both as
videos (`~/Downloads/former-design-16c.mp4`, `former-design-16d.mp4`). Round `2026-09-16d`: documents
flow along lines from Email / Calls / PDFs into "Retyped by hand", then the system, with the
unbilled units dripping below. Also: informationisbeautiful.net becomes an exemplar ("2. yes").

**Founder, 2026-09-21:** "I like 2 but we need to make sure that the idea of what you get from our 1000 audit actually. This was the whole point we started with"
Blue panel. The hero's flow must END on what the $1,000 week hands back (specs/hero-flow.md step 5).

**Founder, 2026-09-21:** "I like D2 but I want to change 2 things The headlines have periods - we decided to remove them. I dont like the headline words stacked up - for both headlines. Identif if 1 line would work nicer Instead of what you get back, we can just "put our audit""
Picked D2 of round 2026-09-21b. Applied: "Automated, but is it true?" on one line, the sub-line on one
line on a laptop, the sheet titled "Our audit".
