<!-- voice-lint-skip -->
# The business

**Status:** CANONICAL as of 2026-08-05. This is the settled answer to who we
serve, what we sell, and what the practice is trying to become.

**The scorer WAS recompiled. This paragraph used to say it had not been, and
that was wrong from 2026-08-05 onward.** `config/icp.json` was recompiled from
this document the same day (commit `558881c`, ASK-382) and carries three
segments built on the customer definition below, not the six pre-2026-08-04 ones
this paragraph claimed. Its `_recompile_note_2026_08_05` reports the rank
movements. Corrected 2026-08-08 after the stale text sent a second agent to redo
finished work.

**`my-project/icp.md` (11 segments, last edited 2026-07-27) is still stale and
is dead prose: no code reads it** (grepped 2026-08-08; the only hits are
docstrings in `fit.py` and `test_fit.py` explaining that it was never read).
`config/icp.json` is the compiled authority for scoring.

**What actually blocks lane L is the input, not the segments.** Measured
2026-08-08 over all 15 candidates in `prospects.json`: `company` is empty on
15/15 and `position` holds warm-graph ledger prose ("RESTORED. Verified send Tue
16:48, CEO Ethos") rather than a job title. `fit.haystack` reads exactly those
fields, so no keyword set can score them. Recompiling the ICP again is a no-op
until the import is fixed.

Full derivation and the append-only decision log: `my-project/icp-working.md`.
The reusable method: `canonical/icp-discovery-method.md`.

---

## The customer

> **A business where somebody is paid to be accurate, and being wrong costs money
> that can be counted.**

Both halves are load-bearing.

- **Manual work alone is not enough.** A business owner who wants his calendar
  managed has manual work, but a mistake costs him five minutes.
- **Countable cost is what separates a $5,000 client from a $500 one.** Our buyer
  has manual work where an error costs an order, a payroll run, a compliance
  finding, or a customer.

**Not a size. Not an industry. "Small business" is retired as the label**, because
it describes the first half only.

Evidence: four clients in the book fit (Client A, Client B, Client C,
Client D). The two that clearly do not are the two already ruled out on separate
grounds, so the commercial judgement and the delivery record agree without having
been reconciled.

### Where they are found

**A business that already bought or built automation nobody now maintains.**
**CORRECTED 2026-09-18: this sentence used to call that a subset of the definition and the
best door into it, not the category itself. It is not a subset. It is the room they are
standing in.** Across two weeks of their own posts it is the largest single conversation in
the corpus: 18 posts and 197 of 634 comments, 31% of everything they argued about
(RULE-2026-09-18-F). The old wording is quoted here rather than deleted so the change is
visible. One client is both at once: inherited workflows on top of people still typing by
hand.

Surfaces observed: distribution and wholesale, freight and logistics, pharmacy
dispensing, auto dealers, field-sales operations. These are a search heuristic,
not the definition.

### Explicitly out

Pre-revenue startups. Enterprise (the compliance burden exceeds what two people
can carry). Investigations and OSINT as a thing we hunt, though it remains
revenue and delivery. Buyers whose only pain is manual work with no countable
cost of error.

---

## The diagnosis

**CORRECTED 2026-09-18, founder-directed.** The statement below replaces the Aug-24 one as the
practice's working diagnosis. The Aug-24 sentence is kept underneath, marked, because it is a
verbatim quote from a research document and a source is never edited to match newer data.

> **They already have the automation. It runs. They cannot tell whether what comes out of it is
> true, and the places where it quietly disagrees with reality are where the money goes.**

**What the correction is.** The Aug-24 belief ends "a human retypes it into the real system."
Across 83 posts in their own rooms over two weeks, that clause appears **zero** times. What
appears instead, and loudest, is people who bought the tool, watched it run, and still do not
trust the output.

**The four things they actually post about** (counts from RULE-2026-09-18-F; 634 ICP comments in
the corpus):

- **The tool runs and they still do not trust it.** 7 posts, 153 comments, including the
  fortnight's largest thread. *"If everything synced, does that mean your ecommerce books are
  actually right?"* · *"If you're still cleaning up the books every month, is the automation
  really working?"* · *"When the 'Automated' Dashboard Breaks: Back to VLOOKUP Hell."*
- **Two systems that should agree, and don't.** 11 posts. An ERP feed, a QuickBooks sync, one
  lump payment against three invoices, a marketplace total that will not tie.
- **Money moved on an instruction nobody verified.** 7 posts, led by *"Im trusting nothing in our
  AP inbox after a vendor changed their bank details"* at 38 comments.
- **Things they are responsible for falling out of view.** 9 posts: unpaid invoices, licences and
  expiries, documents nobody can find, the knowledge in one person's head.

**A fifth shape, found 2026-09-18 and not yet counted against the 83-post population: some of this
buyer's work is not automated at all, still fully manual.** r/Accounting, 2026-09-04: *"Please
don't tell me everyone else is also manually entering credit card statement transactions into their
ERP."* This does not replace the corrected diagnosis, the strongest finding is still "automated and
untrusted," but the population is not uniformly post-automation, and copy should not assume it is
(applied in `site/design/specs/home.md` RULE-2026-09-18-K). A parallel search for buyers who tried a
DIY AI build themselves and failed from lack of time or expertise found nothing across five keyword
searches in `#writing_ideas` and `#consulting-crm`; not claimed, not counted, not published.

The first two are one problem from two sides. Together, 18 posts and 197 of 634 comments: **31% of
everything they argued about in two weeks.**

**Why this diagnosis and the offer already match.** "Why a buyer chooses us", below, says *"Our
systems refuse to guess. Where a system cannot prove an answer it stops and tells a person."* That
is the answer to the complaint above, written before the complaint was measured.

**An open conflict, named rather than resolved quietly.** `config/segment-pain-model.json` is
declared the runtime owner of the pain and still carries the Aug-24 belief with the retyping
clause in it. This file and that file now disagree. The json is not edited here: its
`core_belief` is marked verbatim from the research doc, and pipelines read it. Resolving it is a
founder decision (RULE-2026-09-18-G).

### SUPERSEDED: the Aug-24 belief, kept as written


**Status: added 2026-09-02, founder-directed. `config/segment-pain-model.json`
`universal.core_belief` is the RUNTIME. This section documents it and loses to
the json wherever they disagree**, the same relationship `post-jobs.md` has with
`config/post-jobs.json`.

> **Work arrives through uncontrolled channels. A human retypes it into the real
> system. Follow-up is manual and endless. Money leaks at exactly those seams.**

Verbatim from `customer-pain-and-targeting-findings-2026-08-24.docx`, section 4.
It is not a slogan we wrote. The research reached it by finding the same wound in
four segments that share no vocabulary, then noticed it was already true of the
first two clients before the research started. That is n=4 segments plus n=2
delivered engagements.

### What they actually post about, observed 2026-09-14 to 2026-09-18

**This does not replace the belief above.** That sentence is a verbatim quote from the Aug-24
research and stays as written; a source is not edited to match newer data. This is a second,
dated layer beside it, with its own population and its own limits (RULE-2026-09-18-D).

Population: 25 posts in r/smallbusiness, r/Accounting, r/Bookkeeping, r/LawFirm and r/taxpros,
carried into #writing_ideas by the Consulting CRM bot over four days. Classified on the POSTER'S
OWN TITLE, because the bot's angle is our vocabulary and classifying on it would measure us.

| What the post is about | count of 25 |
|---|---|
| Two places that should agree, and don't | 7 |
| The state of something lives in one person's head | 5 |
| Chasing something upstream that is late or missing | 4 |
| An AI did something wrong and nobody caught it | 2 |
| Work arrives and a person re-enters it | 1 |

**Three things follow.**

1. **The retyping clause is the weakest part of the belief in the field.** One post in 25. Read
   that as a real pain they do not take to the internet, not as a refuted one. But any surface
   that LEADS with retyping is leading with the part they say least.
2. **"Two records that should agree, and don't" is confirmed by their own words.** A sync wiping a
   workbook, a Shopify-to-ERP feed, one lump payment covering three invoices, a website saying in
   stock while the shelf says otherwise, cash that will not reconcile. That is `design-dna.md`
   section 4's one idea, observed rather than reasoned.
3. **A shape this file did not carry: the state lives in one person's head.** The week's
   highest-engagement ICP thread, 32 comments, is "How do you stop your business knowledge from
   living in one person's head?" Small law's cause line already says a version of it for matters;
   the field says it is wider than matters and wider than law.

**And the fear is more specific than "AI lowers quality."** They describe a system doing something
wrong with nobody noticing: a voice agent that books the wrong date, a colleague in "AI psychosis".
RULE-2026-09-15-K is right about the direction and soft about the mechanism. The mechanism is the
missing catch.

**Limits.** n=25 over four days, and the feed is selected by a lane hunting threads worth replying
to, which tilts toward problems that have a systems answer. It grows daily; re-read this at n=150.

**The customer definition above answers WHO. This answers WHY.** A buyer who does
not accept the diagnosis will not accept the fix, so every surface argues for this
one thing and the offer is what follows from it. The `$1,000` week sells diagnosis
before prescription for the same reason.

### The three things it is NOT, and each one is a live failure mode

- **Not "AI saves you time."** The belief is about where money leaks.
  (Clarified 2026-09-15, RULE-2026-09-15-J: this bars the generic time-savings pitch
  as the belief. It does not bar the ROI stated in the buyer's own economics, the
  hours they work against the hours they bill, which the pain model records in
  their words; nor his own compression as capability proof about himself.)
  It is never about hours saved, and no audited figure for one exists here.
  `objections.md` was retired in full for resolving every response to ROI math
  the practice cannot back.
- **Not "your tools are bad."** The seams between tools are uncontrolled. The tools
  are frequently fine and expensive. The A&E buyer walks around software whose
  routing is worse than a printer; the CPA bought a portal the client refuses.
- **Not "you should replace people."** Standing rule: anchor on getting more from
  what they have. `segment-pain-model.json` `universal.forbidden` blocks the
  headcount, replacement and efficiency framings by regex in outbound copy.

### Why each segment's pain is a dialect of it

The per-segment `pain.cause` in the json is the segment's own version. In one line
each: the CPA does not control the channel work arrives through, so the human
becomes the portal; the law firm keeps matter state inside the documents, so
knowing anything means a person opening something; the A&E firm has the record of
the work made by the person that record is used to judge, so it is shaped to
survive review rather than to be true.

**Do not restate those three from memory.** Read them with
`python3 -m pipeline.segment_pain brief <segment>`. A session that had read the
Aug-24 research more closely than anything else still re-derived all three offer
lines from memory on 2026-08-28 and got all three wrong. That scar is why this
lives in data.

---

## What we sell

**Business 1, the services practice.** Assaf and partner.

| | |
|---|---|
| The audit | $1,000 fixed, one week, read only. Ends in written findings and priced options. |
| The retainer | $5,000 per month of continued building, decided after the client has seen the work. |

**We price builds, not hours.** The monthly is continued building, never a support
allowance and never a block of hours. $1,000 is the only price published
anywhere; everything else is gated behind the findings.

**Business 2, the publishing practice.** Assaf alone. He writes down what he
built, with the numbers in it, and readers become clients. Its output is free.
Deals it originates carry no partner split.

**The two feed each other.** One artifact crosses: a build note, written the day a
build works, carrying what was broken in the owner's words, the mechanism, one
measured number with the command that produced it, and what the system refused to
do. Business 1 makes the material. Business 2's writing originates deals that do
not depend on one introducer.

**The split is by origination.** A deal belongs to whoever brought it in,
recorded at lead creation and never edited afterwards. Ambiguity resolves in the
partnership's favour, because the partnership outlasts any single deal.

---

## Why a buyer chooses us

**Our systems refuse to guess.** Where a system cannot prove an answer it stops
and tells a person. That is an acceptance criterion, not a sales claim: missing
evidence cannot produce a verdict, an unverified source cannot be cited, an
outbound request carrying account numbers fails closed.

**The moat is publishing our own evaluation results, including the parts our
systems fail.** Deterministic checks passing, printed next to the language-model
judgements that missed. Anyone overselling their accuracy structurally cannot
publish the same thing. A decade of honest published refusals is an archive
nobody can build retroactively.

**The build itself will commoditize.** No-code tooling has a lower barrier than
any previous automation wave, so the arbitrage window closes faster than it did
for the last one. What does not commoditize is the discipline that makes a
probabilistic system safe to run against money and records.

---

## The shape we are building toward

The test is not this quarter's revenue. It is whether a thing **compounds**.

The model is a consulting practice that publishes, where the writing originates
the work and the work supplies the writing. Historically this outlasted every
firm that sold the capability alone, because the capability became free and the
reputation did not.

Assets that compound: the published method, honest failure numbers, the operating
rules encoded once per client and reused, domain reputation in one place, the
monthly relationship.

Assets that do not: per-case billing, work sold without a recurring line, an
audit sold alone.

---

## What is not yet proven

Stated plainly, because a plan that hides its assumptions cannot be tested.

- **No $1,000 audit has been sold and delivered.** The conversion rate from audit
  to retainer is unknown. It is the single most load-bearing number in the
  services plan.
- **No client has ever arrived through published writing.** All current clients
  came through a person. Whether writing originates a lead at all is the bet
  Business 2 makes.
- **Fifteen net-new retained clients** reach $1,000,000 per year at $5,000 per
  month, against $10,500 per month recurring today. The segment holds; the funnel
  estimate is optimistic, because buyers with manual work are far more numerous
  than buyers with manual work whose errors cost countable money.
- **No churn figure exists.** Multi-year client value is an assumption, not a
  measurement.
- **No audited hours-saved or dollars-recovered figure exists for any client.**
  The weekly value ledger is the mechanism intended to generate them going
  forward; until it runs, outcome claims stay estimates and are published as
  estimates.
- **Origination still runs through one introducer.** That is the structural risk
  Business 2 exists to fix, and it is unfixed today.

### The falsifying test on price

Three prospects who can state what being wrong costs them, and who still will not
pass $1,500 per month, means the price is wrong rather than the buyer. Until that
happens, the price stands.
