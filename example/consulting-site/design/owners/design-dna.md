<!-- voice-lint-skip -->
# Design DNA: how to reason about the askconsulting.io design

**What this file is.** The generative layer of the site design, founder-directed
2026-09-15: "how do we turn these ideas into things that the AI can reason on
instead of just creating block lists... it must work from the canonical files and
what we agreed the business does, who I am and who are the customers."

It does to design what `voice/identity.md` does to writing. It says who the
page is for, who is speaking, the one idea, why each choice is made, where the
tensions sit, and the questions to ask of a draft. It holds no facts of its own:
every fact is read from the file that owns it (section 1), so when an owner
changes, the design reasoning follows instead of drifting.

**How to use it.** Before designing anything (a page, a section, a style tile, a
404, an email): read the owner files in section 1, then this file, then
`site-design.md` for the decisions, specs and tools. Reason from the reader and
the idea; check against the questions in section 7; only then run the
mechanical checks. Section 10, the corrections, is read last and outweighs
everything above it.

---

## 1. The owners (read these; do not restate them)

| What | Owner file |
|---|---|
| What the business is, who the customer is, what is sold, why a buyer chooses us, what is not yet proven | `canonical/the-business.md` |
| The customer's pain, its cause per segment, their own words, the words we must not use | `config/segment-pain-model.json` (runtime; wins over prose) |
| How the ICP was found, what the evidence does and does not show | `my-project/icp-working.md` (START HERE plus the findings cited in `site-design.md`) |
| Who he is: register and the four moves | `voice/identity.md` |
| What he saw before the practice | `voice/scars.md` |
| What he built, with the numbers | `voice/built.md` |
| What he believes | `voice/pov.md` |
| Every design decision, spec, tool and the log | `canonical/site-design.md` |
| Standing rules (price, names, pain first, no card rows) | `canonical/decisions.md` (RULE-2026-08-04-F, -K; RULE-2026-09-15-A, -B, -C) |

If this file and an owner disagree, the owner wins and this file gets corrected.

---

## 2. The reader, and the moment they arrive in

Derived from `the-business.md` and `segment-pain-model.json`; read those for the
facts.

Picture the person, not the segment. Someone paid to be accurate: a tax
practice owner in February, a small firm's office manager, a sales operation's
ops lead. They did not come to learn about AI. They came because one thing keeps
going wrong and it costs money they can count: work arrives through channels
they do not control, a person retypes it into the real system, the follow-up
never ends, and the money leaks at exactly those seams.

What they carry in with them:
- **One pain, not a transformation plan.** They know the symptom in their own
  words ("dribble the data in", a report rebuilt every Monday). They may not
  know the cause.
- **A burn, often.** They tried a tool or a chat window and it gave wrong answers
  or "didn't already know their business". Some have automation a departed
  person built that nobody checks.
- **Contempt for AI marketing.** The one thing every researched industry shares.
  A page that looks machine-made is dismissed before it is read.
- **Accountability.** They answer for the result, to a client, a regulator, a
  principal. Anything they adopt has to be something they can stand behind.
- **Little patience.** They judge in seconds, on the look, and leave.

What they need to feel in the first screen: "this person understands the exact
thing that goes wrong in my week, and would not waste my time."

---

## 3. Who is speaking

Derived from `voice/identity.md`, `scars.md`, `built.md`, `pov.md`.

A practitioner, not a vendor. His job was making sure things were accurate:
data analysis and data integrity at platform scale, done by chasing scammers,
foreign influence and malicious actors (`config/biography.json` through_line).
That is the road to what he does now, building AI systems that can be trusted.
He was in the room when things broke, and he is irritated by systems that
pretend to work. He builds from what he ran and watched fail. His
own line, already published: "Trust moves from the model to the trail. The
trail is the product."

What that means for how the page looks and behaves:
- **The page is a working document, not a brochure.** It reads like something a
  serious practitioner made to be useful: plain, specific, confident, a little
  dry. It never performs enthusiasm.
- **Show, do not assert (THE WITNESS, THE TESTER).** A real record, a real
  number with where it came from, a real miss next to a real pass. Never an
  adjective where evidence could go.
- **Name the thing (THE NAMER).** The page gives the buyer's dysfunction a name
  they will repeat. Design makes room for one named idea to be large.
- **Who pays (THE ATTACKER-AWARE DEFENDER).** The seam where money leaks is shown
  from the side of the person paying for it.
- **Honesty is a style, not a disclaimer.** He believes "systems that pretend to
  work are worse than systems that fail loudly" (`pov.md`). The design should
  make the misses visible, the price visible, what the week does NOT do visible.
- **Background is scarcity, placed after the pain.** Nobody at the buyer's size
  could hire this person (RULE-2026-08-04-K); buyers never cite pedigree when
  choosing (icp-working.md), so it follows the pain, it does not open.

---

## 4. The one idea

**The hierarchy (adopted 2026-09-15 from the external review, RULE-2026-09-15-I).**
The idea below is the VISUAL GRAMMAR, not the literal definition of every
engagement. Not every problem he solves is two records: sometimes something
was never recorded, a follow-up was forgotten, information never reached the
system, or an AI answered without evidence. So:
- **Business problem:** important work falls out of sync with reality.
- **Method:** find the seam where that happens and establish what is actually
  true.
- **Visual grammar:** two things that should agree, and don't.
- **System philosophy:** build from evidence, preserve the trail, and stop
  rather than invent an answer.

**Two records that should agree, and don't.**

**FIELD-CONFIRMED 2026-09-18.** Until now this idea was reasoned from the owner files. It is
now also observed: across 25 ICP-room posts collected 14 to 18 September, "two places that should
agree, and don't" is the most common shape in the posters' own titles (7 of 25), while the
diagnosis's retyping clause is the least common (1 of 25). Counts and limits: `decisions.md`
RULE-2026-09-18-D; the observation layer lives in `the-business.md` under the diagnosis.

**One shape the owners did not carry, now observed:** the state of something lives in one person's
head rather than in a system (5 of 25, and the week's highest-engagement thread). It is a sibling
of this idea rather than a rival: a record everybody relies on and nobody can check.

Why this idea, traced to the owners:
- The diagnosis is literally about seams: a person retypes one record into
  another system and money leaks between them (`segment-pain-model.json`).
- It is what he reacts to most: in the Reddit lane, the threads marked "more
  like this" are an order list and the payment record reconciled late, "synced"
  books that do not match the bank, an AI that says it created a task that does
  not exist (`output/reddit-feedback.jsonl`).
- It is what he builds: evidence captured first, verdicts computed from data,
  a read-back after every write, the trail as the product (`built.md`).
- It carries the trust problem without saying "trust": the buyer sees the
  mismatch, and sees a system built to catch it.
- It is his career: data integrity is the work of finding where records that
  should agree don't, and he did it against scammers, foreign influence and
  malicious actors at platform scale before he built AI systems.

What the idea generates (reasoning, not rules; re-derive for anything new):
- **Layout.** Pairs and comparisons are native to this site: the record and the
  reality, the claim and the source, the pass and the miss. A comparison has a
  reason to exist; a row of equal boxes does not.
- **Type.** The feel of records: something a ledger, a report or a case file
  would be set in. Sturdy, readable, serious, with one face that can carry a
  very large line of the buyer's words.
- **Color.** Mostly ink on paper. One signal color, and it means one thing
  only: the mismatch, the place money leaks. If the signal color appears where
  nothing disagrees, it has lost its meaning.
- **Imagery.** Real records, recreated and anonymized, annotated at the point
  where they disagree. No stock, no illustration standing in for work.
- **Motion.** The moment the discrepancy becomes visible, and nothing else. If an
  animation does not reveal a mismatch or keep the reader oriented, it is not
  needed.
- **Copy.** The buyer's sentence first, then the seam, then the fix. The fix is
  shown as the two records agreeing, with the source visible.

### 4b. Proof comes in five kinds, and one cannot stand in for another

- **Problem proof:** the buyer's problem exists (their quotes, real seams, a
  retyped record).
- **Capability proof:** he can build serious systems (kipi, Chief, the
  investigation OS, the fraud pipeline).
- **Reliability proof:** his systems behave differently from generic AI (the
  source shown, verdicts from data, stopping when it cannot prove, misses
  published next to passes).
- **Outcome proof:** his work changed something for a client, before and after,
  from the records (the proof audit).
- **Pedigree proof:** he worked where accuracy, adversaries and evidence
  mattered (VMware, LinkedIn, Meta, Google, ElevenLabs).

Stars cannot prove outcomes, a logo cannot prove the system works, a graph
cannot prove a small business should hire him. Before any artifact goes on a
page, name the kind of proof it is and the claim it supports.

### 4c. The site is proof by behaving like his systems

Not by looking futuristic or being interactive. Every claim has evidence,
every number has a source, sample data is unmistakably sample, live data has a
fallback, scripts are optional, failures are published, nothing pretends to
work. Where a rule like this can be checked by a script, it is.

---

## 5. Principles, each with its reason for THIS reader

Sources for each are in `site-design.md` section 6.

1. **Understood without explanation.** The reader gives it seconds. If they have
   to work out what this is, they leave. Working: a stranger can say what it is
   and what to do next.
2. **Specific to this problem.** The reader has seen a hundred AI pages. A page
   that could belong to anyone confirms their contempt. Working: another
   consultant's name would not fit.
3. **Power from contrast, not effects.** Effects are what machine-made pages use.
   Scale and weight are what a practitioner uses. Working: one line dominates,
   and it does so by size and weight alone.
4. **Type carries the identity.** Most of what the reader meets is words, and
   his value is precision with words and records. Working: with images off, it
   still looks like him.
5. **Honest to the letter.** The reader answers for what they adopt; an
   exaggeration is a reason not to trust the rest. Working: every claim can
   point to its source.
6. **Less, but better.** One pain per screen, one idea per page, depth one click
   away. Working: remove any element and something real is lost.
7. **Thorough in the details.** The reader is paid to be accurate and notices
   sloppiness the way he does. Working: nothing on the page was left at a
   default.
8. **A system, not a collage.** Consistency is itself a proof of discipline.
   Working: every size, space and color traces to a declared scale.
9. **Built to last.** Fashion ages, and this reader distrusts whatever looks like
   this year's trend. Working: nothing was chosen because it is in style.

---

## 6. The tensions, and where we sit

- **Restraint vs. proof of craft (RULE-2026-09-15-E).** The site is the first
  thing people see with his name on it, and he sells AI expertise, so the page
  itself is evidence of how good he is. Restraint applies to noise, never to
  craft. The page has to visibly do what a template cannot: real records that
  react, the real graph of what he built, motion that carries meaning, a finish
  a buyer can feel. Simple and thin reads as "he could not do more".
- **Familiar structure, distinctive expression.** Where the price, the button
  and the next step are: never a surprise (low visual complexity and high
  prototypicality win first impressions, Tuch et al. 2012). What makes it his:
  the type, the voice, the one idea.
- **Calm page, one loud moment.** Mostly quiet. One place per screen is allowed
  to be large, and it is the buyer's words or the mismatch.
- **"Whoa, he built serious things" vs. overwhelm.** The founder wants the
  visitor pre-sold. The wow comes from the specificity of ONE real artifact per
  story, never from the quantity of things shown.
- **Grab them first vs. let them explore (RULE-2026-09-15-H).** The reader is a
  professional with a pain and little time. They must get it on landing, with
  nothing to click or play with: their pain, what he does, one capability that
  impresses, his pedigree, the action. Exploration (case studies, the graph,
  anything interactive) is a reward for those who stay, never the way in.
- **Proof vs. pedigree.** Proof leads. Pedigree follows the pain, as scarcity.
- **Rigor vs. warmth.** Rigor with dry humor, the way he talks. Never cold
  corporate, never cheerful software.
- **One pain vs. the whole system.** Start from one pain; the whole system
  (kipi, the bots) is proof of how far it can go, shown later to those who look.

---

## 7. Questions to ask of any draft

Generate first, then ask these. Revise until each has a good answer.

1. What is the one thing this screen says, in the buyer's words?
2. Who is reading this, what went wrong in their week, and what do they feel
   here?
3. Where are the two records, and does the reader see where they disagree?
4. Could this be anyone else's page? What makes it his?
5. What here is decoration? What does it tell the reader?
6. What would he say is "pretending to work" on this page?
7. Is there a claim without its source?
8. If the buyer showed this to the person they answer to, would it hold up?
9. What did I choose because it was the default?

---

## 8. How a piece of design gets made

1. Read the owners (section 1), this file, and `site-design.md`.
2. Write the brief for the piece in three lines: the reader, the pain, the one
   thing it says.
3. Produce THREE genuinely different directions, each argued from the one idea
   (section 4), not from a template.
4. Critique each against the questions (section 7). Say which answers are weak.
5. Run the mechanical checks from `site-design.md` (spec numbers, the
   fingerprint, the price test, voice-lint) after the creative step, never
   instead of it.
6. The founder picks. The reason he gives is recorded in section 10 or in
   `site-design.md`'s Decision log.

---

## 8b. Worked examples and references

**In-house worked examples (reasoning, NOT approved copy).** Produced by the
cold test of this file on 2026-09-15 (section 9), kept because they show the
reasoning working on things the canon never mentions:

- **A 404 page.** Nothing disagrees on a missing page, so there is no signal
  color and no motion; staging a fake "discrepancy" would be decoration posing
  as evidence. Plainness is the voice: say the page does not exist, say nothing
  broke on their end, give the real destinations as a plain list, and ask to be
  told if a link we sent was wrong. Cute error pages are a system pretending a
  failure is charming, which is what he calls pretending to work.
- **The invoice email for the $1,000 week.** The quoted price and the billed
  price ARE the two records, and the email's one job is to show them agree:
  one line item, the date it was quoted, the amount, and the fact that it
  counts toward the build if the client continues (RULE-2026-09-15-B). No
  banner, no button, no re-selling after money changed hands; a document, not a
  template.

**Real references, annotated (from the research lane of 2026-09-15; re-open
each page before borrowing from it).**

- **latacora.com** (security consultancy). Take: one plain offer line; services
  as a text list with arrows, not cards; confidence through whitespace. Leave:
  nothing specific to our reader's pain on screen one.
- **kellyshortridge.com** (security author and practitioner). Take: proof first
  (book, talks, a named framework) and an early, plain way to work with her.
  Leave: the author-brand frame; his offer is a week of work, not a platform
  of ideas.
- **trailofbits.com** (security firm). Take: trust from numbers and evidence,
  no hacker imagery. Leave: its own four-card service row.
- **simonwillison.net** and **danluu.com**. Take: the archive of real work is
  the credibility; a dated log of what was built and what broke. Leave: they
  are slow to say what a visitor should do, so the offer stays on top.
- **inkandswitch.com** (research lab). Take: grouping by meaning instead of a
  grid; one plain mission sentence.
- **Our own `site/solutions/index.html`.** Take: eight asks in the buyer's
  grammar ("Can AI answer my phones?"). That is the door for a one-pain buyer.

---

## 9. The test that shows this file works

Give a fresh session only the owner files and this file, then ask it to design
something none of them mention: a 404 page, an invoice email, a slide. It works
if the choices are consistent with the rest of the site and it explains them
from the reader and the idea, citing no rule. It fails if it can only recite
rules or produces a generic answer.

---

## 10. Corrections (read last; these outweigh everything above)

Founder corrections from the 2026-09-15 session, verbatim, and what each teaches.

- **"They all look extremely generic. So we should not rely on it."** (on the
  design-room generator) Teaches: a tool that checks for defects cannot produce
  quality. Generation needs the reader and the idea, not a filter.
- **"these narrow down to a very specific customer that wants me to automate
  their whole thing... Some customers are going to start with what is the pain
  that they have."** Teaches: design from the reader's single pain, never from
  the seller's whole system. Keep "the parts of your business", never widen it.
- **"the three boxes thing is an AI trope that I don't want."** Teaches: a
  layout must have a reason in the content. Three equal boxes say "menu", and
  this reader came with one problem.
- **"So we have all the no's, but we don't have any of the yes."** Teaches:
  prohibitions without a positive standard produce empty pages. Lead with what
  the page is for.
- **"I want to focus on Kipi system and... the automation of small businesses...
  investigations are good to have, but that's not where my customers are."**
  Teaches: show the capability the customer buys; the deepest work is depth, not
  the lead.
- **"how do we turn these ideas into things that the AI can reason on instead of
  just creating block lists"** Teaches: every rule carries its reason, and the
  reason is anchored in the reader, the speaker or the idea.
- **"I think I like B the most but it's so simplistic... If this was what the
  website looked like then no this is bad... I need a little bit more design to
  really understand the direction."** (on the three style tiles, 2026-09-15)
  Teaches: a sheet of ingredients cannot be judged as a site; show a direction
  as pages. Restraint is not the same as thin; the richness has to come from
  somewhere, and on this site it comes from real artifacts of his work.
- **"I don't want design that's so trying to do the path of the customer that it
  loses what it's actually putting across."** (same day) Teaches: the buyer's
  world (ledgers, reports, case files) is a way in, not the message. If the
  metaphor is louder than what he builds and how well, the design has failed
  even when every rule passes.
- **"Is there a reason that the site must only be HTML?? I don't think so."**
  (2026-09-15, after I ruled out a live video player because "the site is
  static HTML") Teaches: how something is built today is not a constraint. A
  constraint needs a recorded reason; if none exists, name it as an open choice
  and let him decide.
- **"The site is a manifestation of how good I am with AI... simple. Looks like
  slop sloppy or just bad - that is my calling card and it makes me look bad."**
  (2026-09-15) Teaches: for this seller, the medium is part of the proof. Judge
  every draft by whether it looks like the work of someone who builds serious
  AI systems, not only by whether it avoids the AI look.
- **"we should definitely have logos for VMware LinkedIn meta Google 11 Labs
  because I worked at all of those"** (2026-09-15) Teaches: pedigree is shown,
  not hidden; the reasoning is where and how, so it reads as his history and
  never as a client list (RULE-2026-09-15-F).
- **"You missed that I worked on data analysis data integrity... My whole job
  was making sure the things were accurate... chasing scammers on huge
  platforms, chasing foreign influence and identifying malicious actors at
  scale. And that all got me to where I am which I build trustworthy systems
  with a i."** (2026-09-15) Teaches: the background is not a list of employers,
  it is one line of work, accuracy, that leads straight to trustworthy AI. Tell
  it as that line (RULE-2026-09-15-G).
- **"we're not going to have people playing around on the site. They need to
  hit the site and immediately understand how I can help them and be wowed by
  my capabilities and my pedigree... These are professionals that are looking
  to alleviate some of their pain. It needs to treat them that way, but at the
  same time be impressive."** (2026-09-15, after I proposed a pain picker and a
  check that runs on the page) Teaches: interaction is not how a busy
  professional understands an offer. Impress with what is already on screen;
  let depth wait for the ones who stay.
- **"Yes. Follow this path"** (2026-09-15, on the external review and my
  response) Teaches: I had not searched the client work for proof and had not
  defined what the $1,000 week is, and I let a checklist shrink the type
  instead of setting priorities. Evidence and product come before layout.
  Refusal is shown as a capability further down the page, never as the hero,
  and pedigree is visible on landing but secondary (RULE-2026-09-15-I).
- **"You took it way too hard on the one reveal rule. That's not a hard rule. That's if
  the UI supports it, then great. Same thing with the playing around, it's just
  something I said, I didn't make it a hard rule."** (2026-09-15, on rejecting
  scroll-craft) Teaches: the motion line in section 4 and the "grab them first"
  tension in section 6 are preferences with a reason, not gates. A scroll-driven or
  interactive page is allowed when it serves the reader; it is judged by the nine
  questions like anything else. Do not turn a founder remark into a rule he did not
  make; when a tool collides with a preference, say so and let him weigh it.
