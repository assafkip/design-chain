# Brief — Home hero redesign, 2026-09-18

## 1. The reader

Who: someone paid to be accurate (CPA, small law, A&E), whose expert time is billed against work
that arrives raw or unverified. What went wrong in their week: something they rely on, a report, a
sync, a status, stopped matching reality, and money leaked at exactly that seam. What they need to
feel in the first screen: this page understands the exact thing that goes wrong, and would not
waste their time proving it with a sales pitch.

## 2. The pain family this round leads with

`segment-pain-model.json` `universal.working_belief` (RULE-2026-09-18-G, today's corrected
diagnosis): "They already have the automation. It runs. They cannot tell whether what comes out of
it is true, and the places where it quietly disagrees with reality are where the money goes."

## 3. The one thing this screen says

Automated doesn't mean true, and this practice is built to catch the difference.

## 4. The anchors, verbatim, copied exactly from the live owner files

From `q-consult/canonical/the-business.md`:
> **A business where somebody is paid to be accurate, and being wrong costs money
> that can be counted.**

From `q-consult/canonical/design-dna.md`:
> **Two records that should agree, and don't.**

> 1. What is the one thing this screen says, in the buyer's words?

> 3. Where are the two records, and does the reader see where they disagree?

> 4. Could this be anyone else's page? What makes it his?

> 9. What did I choose because it was the default?

From `q-consult/canonical/site-design.md`:
> Craft specs a page is checked against: body 15 to 25 px, line spacing 120 to

> is built once per candidate stack and he compares them working; no stack is

From `q-consult/canonical/decisions.md`:
- RULE-2026-09-15-C: **The public site starts from the visitor's one pain, not from the system; and no three-box card rows.**
- RULE-2026-09-15-I: **The site redesign follows the external review's path: evidence and product before layout.**
- RULE-2026-09-15-J: **The ROI is the gap between the hours the buyer works and the hours they bill; his own compression is capability proof, not a client savings claim.**
- RULE-2026-09-15-K: **The buyer's fear is that automating, and automating with AI, lowers quality; the record says his builds raise it, and that is the expertise being sold.**

From `q-consult/config/segment-pain-model.json`:
- `"statement": "Work arrives through uncontrolled channels. A human retypes it into the real system. Follow-up is manual and endless. Money leaks at exactly those seams.",`
- `"word": "dribble the data in"`
- `"word": "donating time"`
- `"word": "entitlements"`

## 5. Anchors from the vision notebook (`site/design/VISION.md`), the process's own extra requirement

**Founder, 2026-09-18:** "I think the page is proof and the one story because we ended up having
two hero sections, and we weren't fully focused on the pain, which we just researched from all the
Reddit work."

**Founder, 2026-09-18:** "abstract because we dont know exactly who from the icp is going to read
this."

## 6. What this round is

Three DIRECTIONS for the hero's redrawn mechanic (`directions.md`), per `decisions.md`
RULE-2026-09-18-I and -J. Full element-level specs for the picked direction (D1) in
`site/design/specs/hero-*.md`, each pending a real `REVIEWED BY FOUNDER` line. Built as working
pages at real production fidelity (matching the live hero's scale, not a scratch sketch), measured,
critiqued, and sealed before the pick counts, per this project's own round-history precedent
(`site-design.md`, the 2026-09-17e entry on what an "implements" round requires).
