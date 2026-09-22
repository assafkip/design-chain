<!-- voice-lint-skip -->
# Site design: the canon for askconsulting.io

**Status:** CANONICAL as of 2026-09-15, founder-directed. Verbatim: "design has
to be with all of the tools that we identified... So you need canonical
documentation. So you need to continue compounding on that and continuously read
through it so you're always on the same page."

**Read `canonical/design-dna.md` first.** It is the generative layer (the
reader, the speaker, the one idea, the reasons, the tensions, the questions).
This file holds the decisions, specs, tools and the log that the DNA reasons
within.

**How to use this file.** Read it in full before any design, copy or build step
on `site/`. Every new decision is appended to the Decision log at the bottom,
dated, with its origin tag and source. A superseded line is marked superseded,
never deleted. The full research trail (every quote, every source) lives in
`kipi-system/q-system/output/research/site-brief-2026-09-15.md` and
`design-bot-2026-09-15.md`; this file holds the conclusions and the rules.

**Order of work, founder-set 2026-09-15:** research, then THIS canon, then a
style guide agreed with the founder (type, color, imagery, motion), then build.
Nothing is built before the style guide is agreed and recorded here.

---

## 1. What the site has to do

The visitor arrives at the call already sold, without being shown everything.
Founder: "I'm not looking to show everything I did, I'm looking to show how I am
so much better than everybody else"; "if we show everything at one time, people
are going to get overwhelmed."

It starts from the visitor's ONE pain, never from the system
(RULE-2026-09-15-C). Order a visitor meets the practice: one pain, the $1,000
week, one build, then the whole system for those who want it.

**The first screen, as a hierarchy (RULE-2026-09-15-H, rewritten by
RULE-2026-09-15-I).** SUPERSEDED form: "five things, all visible in the first
viewport" became a packing exercise that shrank phone labels to 13 px. The
question is now: what must the visitor understand before deciding to
continue? In order of weight:
1. A failure they recognize (failure first; the invoice example is not
   locked, and sample data does not go in a hero).
2. What he does about it, in one clear sentence.
3. Why to believe it: the strongest real proof found by the proof audit.
4. His pedigree, visible on landing but secondary, labeled as where he worked.
5. The action. Its details (read only, the credit) may sit below the fold.

Never solve a priority problem with smaller type: body text stays within the
section 6 specs on every screen. Case studies, the graph and anything
interactive are depth. Checked by the naive comprehension gate (section 8),
not by pixel-packing.

## 2. Who it speaks to, and in whose words

The customer (`the-business.md`): somebody paid to be accurate, where being wrong
costs countable money. The diagnosis (`config/segment-pain-model.json`
`universal.core_belief`): work arrives through uncontrolled channels, a human
retypes it, follow-up is manual and endless, money leaks at those seams.

Copy uses the buyer's own words, never ours. Verified lines to draw from, with
sources, are in the brief section 1e. Two carry the whole argument:
"a few weeks later they're frustrated because it's giving wrong answers or
making things up" (the trust problem) and "they expected the AI to already know
their business. It doesn't." (the memory problem).

Vocabulary rules from `my-project/icp-working.md`: "double-check" is STRUCK
(means scam-checking); "AI" is buyer language only as an object of confusion or
possession ("Can AI answer my phones?"), never as our expertise;
`site/solutions/index.html` already uses that grammar and should be promoted.

## 3. The narrative order of the homepage

Their pain in their words, then the seam where money leaks, then the person
they could never hire (the background is a SCARCITY argument, RULE-2026-08-04-K,
placed after the pain because buyers never cite pedigree, icp-working.md n=0 in
889 posts), then why his systems can be believed (they work from the business's
own records and show where each answer came from), then proof, then the week.

The person they could never hire is told as ONE line of work
(RULE-2026-09-15-G): his job was making sure things were accurate, data
analysis and data integrity, done by chasing scammers, foreign influence and
malicious actors at scale on huge platforms; that is how he came to build AI
systems that can be trusted. The logos (RULE-2026-09-15-F) sit inside that
line as where it happened. This is also why "two records that should agree,
and don't" is his idea and nobody else's: it was his job.

Trust leads only for the buyer who already tried AI and got burned; for
everyone else it is the reason the fix holds (icp-working.md: reliability is
real at n=5, "not the opening line").

## 4. Proof

Permission recorded (RULE-2026-09-15-A): every client story may be told
anonymized; the investigation case-043 may be published without names.
Each story shows the specific tooling built for it. Kipi and the Chief bots
are proof of how far the method goes, never the screen-one offer. Investigations
are depth (one line, one deeper page), not a lead (founder, 2026-09-15:
"that's not where my customers are. My customers want automation").
The moat to show: publishing our own evaluation results, the misses next to the
passes (`the-business.md`; icp-working.md 2026-08-05).

Former employers (RULE-2026-09-15-F): logos of VMware, LinkedIn, Meta, Google
and ElevenLabs. Placement AMENDED by RULE-2026-09-15-H: pedigree is in the
first screen, below the pain line, labeled plainly as where he worked (for
example inside the line about his accuracy work), set in one tone so they sit
in the page's type and color. Never a bare unlabeled logo row, because that
conventionally means clients and would be a false claim. Any sentence next to them passes `bio_gate.py`
(worked there: yes; built AI there: no). Not yet checked against each
company's own logo-use rules {{UNVALIDATED}}.

The site itself is proof (RULE-2026-09-15-E): its craft is judged as evidence
of his AI skill, not only as the absence of the AI look.

## 5. The offer on the page

$1,000, one week, read only; the only public price (RULE-2026-08-04-F,
`test_site.py`). Credited toward the build if the client continues
(RULE-2026-09-15-B). The page names what the week looks at. (CORRECTED
2026-09-15: this line said "Red Oak declined because it did not". The records
say the deal was lost to no budget, not positioning (`q-consult/memory/graph.jsonl`
line 38); his objection on the call was that the look "could be like a
15-minute screen share" (`canonical/objections.md` line 84). That objection
still argues for saying exactly what the week does, which is why the week is
being designed as a product, RULE-2026-09-15-I.) Monday a thirty-minute call, midweek we look at the actual
work, Friday findings and priced options in writing, nothing installed or
changed, and the disqualifier said out loud.

## 6. The positive standard (what quality IS)

From primary sources read 2026-09-15 (full list in the brief, section 8d):

1. Understood without explanation (Vignelli, pragmatics; Rams #4).
2. The specific answer to THIS problem (Vignelli, appropriateness). Test: swap
   in another consultant's name; if it still works, it failed.
3. Power from contrast of scale and weight, not effects (Vignelli, visual power;
   NN/g visual hierarchy).
4. Typography is most of the design (iA: 95% of the web is text).
5. Honest: every claim can point to its source (Rams #6; our own canon).
6. Less, but better (Rams #10); "complexities, not complications" (Vignelli).
7. Thorough to the last detail, including states (Rams #8; Vignelli, discipline).
8. A system: every size, space and color from a declared scale (Vignelli;
   Refactoring UI).
9. Lasting, not fashionable (Rams #7; Vignelli, timelessness).
10. Motion only when it carries information (Chimero; Rauno Freiberg).
11. Distinctive inside a familiar structure (Tuch et al. 2012, full text read:
    low visual complexity plus high prototypicality scored most beautiful, low
    prototypicality scored unattractive at every complexity level, effects
    present within 17 to 50 ms; Hekkert et al. 2003, cited there: novelty helps
    only while typicality holds). Limits of that study: company websites only,
    young Swiss non-designers, passive viewing of screenshots.

Craft specs a page is checked against: body 15 to 25 px, line spacing 120 to
145%, 45 to 90 characters per line with about 66 ideal for a single column
(Butterick; Bringhurst via webtypography.net); a professional typeface; one
typeface can be enough and two is usually plenty (Jason Santa Maria, "On Web
Typography"); body faces with high x-height and strong character; pair by
contrast; a serious message wants sturdy faces; no more than 3 type sizes and 2
large elements in a view (NN/g); bold or italic sparingly and never together;
all caps under one line with 5 to 12% letterspacing (Butterick); no emdashes
anywhere (founder rule).

## 7. What it must not look like

**AMENDED 2026-09-16, founder-directed: "remove the old cannon bans if they and make sense
anymore".** The original list was written before the exemplars were captured, and some of it
banned moves that the sites he named as the target actually make. A rule the target set
breaks is not a standard; it is a reason the build can never resemble the target, and it cost
seven rounds. Every clause below was TESTED against all five, live, by
`site/design/references/ban-audit.py`. The verdicts are measurements.

**STRUCK. Two side-by-side CTAs. 4 of 5 do this.** calendly ("Talk to sales", "Log In",
"Get started for free"), figma ("Contact sales", "Get started for free"), notion ("Get Notion
free", "Request a demo"), stripe ("Get started", "Sign up with Google"). A primary and a
secondary action next to each other is the ordinary shape of a software landing page. It is
no longer a tell here.

*(That audit's first run reported 5 of 5 and was WRONG: the detector matched any two adjacent
links, so it read navigation menus as CTA pairs. Fixed to require a real control outside the
nav. Recorded because a canon change made on a broken measurement is worse than none.)*

**NARROWED, not struck. Three moves exactly one exemplar makes, each earning it:**

- *Violet or indigo accents.* stripe's brand is `#533afd`, measured. Already allowed on trial
  here (`craft.allow_tells`, founder 2026-09-15). The tell is violet reached for as a default,
  not violet chosen as a brand.
- *Gradient surfaces.* squarespace runs 9, the largest at 95% of the fold. A gradient as a
  FIELD is not the tell. Gradient painted into TYPE still is: 0 of 5 do that.
- *A dark hero.* squarespace's is black over 95% of the fold, carrying a photograph. Dark is
  not the tell; dark plus a glow plus nothing on it is.

**KEPT, and costing nothing, because 0 of 5 do any of them:** gradient text on a headline,
emoji as icons, monospace body, serif italics. Also kept: Inter or Geist as the ONLY choice.
calendly loads Geist, but as a secondary to Calendly Sans, so the clause as written already
permits what calendly does.

**KEPT AS A FOUNDER PREFERENCE, against the evidence: rows of three or more equal boxes.**
2 of 5 do this (notion 3, squarespace 6), so the AI-tell argument does not hold. It stays
because the founder said so directly, verbatim 2026-09-15: "the three boxes thing is an AI
trope that I don't want", and `design-dna.md` section 10 carries the reason that survives the
measurement: three equal boxes say "menu", and this reader arrives with one problem. A stated
preference is a better reason than a fingerprint that does not hold.

**What the list is actually for.** A pattern is a tell when it is imposed without reason
(Frank Chimero). The fingerprint is a set of moves that became cheap BECAUSE great companies
made them famous, which `references/NARRATIVE.md` section 8 said and nothing acted on for
seven rounds. Contempt for AI-made marketing is the one finding all eleven researched
industries share (icp-working.md, n=16), and that contempt is earned by pages with nothing on
them, not by pages that use colour.

The executable half is `kipi-system/plugins/kipi-design/hooks/dogfood_gate.py`, and it is
narrower than this section: read its silence as "no fingerprint matched", never as approval.

## 8. Tools for the design (the set identified 2026-09-15)

- **References, real design systems:** styles.refero.design (DESIGN.md files
  per product, radar ledger WORTH_LOOK); LandingFolio MCP (real landing pages).
  Neither is installed yet.
- **Craft rules as skills:** refactoring-ui-skill and taste-skill (radar drops,
  never tried, not installed); the installed `frontend-design` skill.
- **Visual editing for agreement:** the installed `design` skill (Claude Design
  canvas: artboards the founder can click and edit).
- **Video:** the installed HyperFrames skills, for recreated, anonymized Slack
  and investigation clips (60 s or less for the bots; under 5 min for the
  investigation page).
- **Verified inventory, read from code 2026-09-15** (founder: "not from their
  readme from their actual code"; ASK-1735 filed for the gap found):
  - impeccable, `cole-gtm/.agents/skills/impeccable/scripts/detector/`: a real
    static analyzer that resolves computed styles and runs about 35 checks,
    including WCAG contrast from resolved colors and a type-hierarchy ratio.
    Our tripwire has neither. Use it as a check on every mockup.
  - refactoring-ui-skill (github.com/s0xDk/refactoring-ui-skill): prose plus
    `assets/tokens.css`; take its non-linear scale (4, 8, 12, 16, 24, 32, 48,
    64, 96, 128) and contrast ratio noted on every color token.
  - taste-skill, vendored at `cole-gtm/gtm/design-room/vendor/taste-skill/`:
    prose only; its tell list (SKILL.md 635-701) is NOT in `dogfood_gate.py`
    although the July PRD says it shipped (ASK-1735).
  - Imagery: `nano-banana-batch` in `consulting/.claude/skills`, backed by the
    nano-banana MCP registered in consulting's `.mcp.json` (Gemini image).
    Higgsfield: hosted MCP at `https://mcp.higgsfield.ai/mcp` (OAuth, credits,
    not connected yet) and the `higgsfield` CLI (compiled Go binary, login
    based, image, video, 3D, audio models). The local
    `cole-gtm/gtm/scripts/higgsfield_gen.py` is image only, archived, unwired,
    and reads the API key from `HIGGSFIELD_KEY` or `~/.higgsfield-key`.
  - Video: HyperFrames (proven renders in `cole-gtm/gtm/video/*/renders/`),
    `claude-video-editor` (footage cut and captions, needs ffmpeg and an
    ElevenLabs key), anything2explainer (Remotion template, radar drop).
  - On-page motion: `explainer-visuals` style inline JS or a single GSAP
    trigger. `cinematic-web-build` and `gsap-master-timeline` are built for
    continuous scroll animation, the opposite of the one-reveal rule.
  - Remotion: installed 2026-09-15 at `~/.agents/skills/remotion-best-practices`
    (repairs the broken `~/.claude/skills` link; 12 official skills from
    github.com/remotion-dev/skills, commit in `SOURCE.txt`). Videos written as
    React code, every frame drawn from data. Use for the bot and investigation
    clips, recreated from an anonymized transcript instead of a screen
    recording, in the site's own type and color. Its `@remotion/player` plays a
    composition live in a page (React). Whether that is on the table depends on
    the stack decision in section 10, not on the site being HTML today.
    Overlaps HyperFrames (`remotion-to-hyperframes` exists to move off it); pick
    one per clip. `remotion-maps` (Mapbox, Cesium) is the one thing HyperFrames
    lacks, relevant only if the investigation clip shows a map. Free for a
    company of up to 3 employees (LICENSE.md).
- **scroll-craft (installed 2026-09-15, plugin `nateherk-design@nateherk` v0.3.0, user
  scope; code read before adding):** a scroll-driven runtime (`engine/scrollcraft.js`,
  acts, parallax planes, count-ups, a worldflight camera mode, reduced-motion
  handled), an asset pipeline on kie.ai (`scripts/kie.mjs`: photoreal stills and
  image-to-video, needs `KIE_AI_API_KEY`, real Chrome and ffmpeg), a contact-sheet
  verifier (`scripts/shoot.mjs`, every scroll position at desktop, mobile and
  reduced motion, a dead-scroll detector) and a `FINGERPRINTS.md` registry (a new
  build must differ from every prior build on 4 of 6 dimensions). Founder: the
  one-reveal and "no playing around" lines are preferences, not gates, so this is
  a legitimate build path when the UI supports it. Pages it produces still go
  through the design-chain gate and the real-imagery rule.
- **Naive comprehension gate (RULE-2026-09-15-I):** a rendered first screen is
  shown to several fresh, no-context model instances (Haiku), each asked
  separately: what does this person sell, who is it for, what problem does he
  solve, what happens if I hire him, why believe him, what does the $1,000 buy,
  what confused me, what did he do at Google or Meta. Answers are saved to a
  file, never paraphrased. A machine check, not buyer research; five real buyer
  conversations follow it.
- **Gates:** `dogfood_gate.py` (tripwire), `test_site.py` (price), voice-lint
  (copy), the design-room lenses as a REVIEWER only (founder verdict 2026-09-15:
  not the generator).
- **Copy sources:** this file, `the-business.md`, `segment-pain-model.json`,
  `icp-working.md`, the voice corpus.

## 9. Style guide

**STATUS: NOT YET AGREED.** To decide with the founder, in this order: display
and text typefaces and the type scale; the color palette; imagery rules (real
screens only, recreated and anonymized; annotated graphs; no stock or
"AI brain" art); motion rules; how the buyer's words sit on the page. Options
are shown as style tiles the founder can react to; the agreed guide is recorded
here and nothing is built before it is.

**Proposed 2026-09-15, awaiting the founder's pick:** three directions as style
tiles on an editable canvas, https://claude.ai/artifact/JtgQBL1mDHwjuVUyQaeAi1
(working files and plan: `kipi-system/q-system/output/plans/site-style-guide-2026-09-15.md`).
A, Ledger: Public Sans, signal red. B, Report: Literata upright, signal blue.
C, Case file: Archivo condensed plus normal, signal highlighter yellow. Type and
signal color are independent choices. Recommended: A with red. None of this is
agreed until the founder picks and gives a reason.

**AGREED 2026-09-15: the typeface is General Sans** (Indian Type Foundry, free for
commercial use, served from the Fontshare CDN). Founder, on a five-face specimen set in his
own headline, his own body line and the 441/388/53 figures at the sizes the build uses: "I
love general sans." The alternatives shown were Satoshi, Switzer, Archivo and Public Sans,
with Söhne named as the paid reference. All five were verified as actually loaded in the
browser before the specimen was screenshotted, because a type comparison where one face
silently falls back to Helvetica is worse than none. Specimen and the reasoning:
`site/design/references/type-specimen.html`, decision recorded in
`site/design/OPEN-DECISIONS.md` under `typeface`.

Still NOT agreed in section 9: the colour palette, the imagery rules, the motion rules and
how the buyer's words sit on the page. The type pick is one of five items in that list.

## 10. Not yet read or resolved

- Jason Santa Maria's own essay on web art direction: every copy tried returned
  403 (v4, v5, the 2008 "A New Day" post). His typography guidance was read.
- Which Slack bot moment carries the 60-second clip.
- Whether C, "Tools swap out easy. The plumbing under them doesn't.", sits under
  the headline or in "how the work works".
- The headline itself (brief section 1d options, pain first).
- RESOLVED 2026-09-15 (RULE-2026-09-15-D): the $1,000 week is invoiced before
  the week starts; if the client continues it is "$1,000 off the additional
  build".
- Whether the "credited toward the build" line appears on the invoice itself or
  only on the offer page (RULE-2026-09-15-B names the offer page).
- **The site's stack. OPEN, founder to decide before the build.** Founder
  2026-09-15: "Is there a reason that the site must only be HTML?? I don't
  think so." Checked: no decision requires hand-written HTML. The site is plain
  HTML only because it was recovered from the live deployment as one
  self-contained file on 2026-08-03 (`site/DEPLOY.md`). What actually depends on
  the output: `q-consult/pipeline/tests/test_site.py` walks `site/` for `.html`
  files (the price and JSON-LD checks, RULE-2026-08-04-A and -F);
  `q-consult/pipeline/case_study.py` writes `site/work/<slug>.html` from
  `render/work-page.html`; the SEO set (sitemap, robots, llms.txt, JSON-LD) and
  crawlers need real HTML with the text in it; Vercel serves it. So the real
  requirement is that the BUILT output is crawlable HTML that reads with
  scripts off, not that the source is HTML. Options: (1) plain HTML, simplest,
  video as files; (2) Astro, which builds to plain HTML and adds React only in
  the pieces that need it (a Remotion Player, the live graph), tests re-pointed
  at the build folder; (3) Next.js, full React on Vercel, most power, most
  weight. Recommended: (2). **DECIDED 2026-09-16: Astro (see Decision log).** **Founder 2026-09-15: "I don't want to choose the
  design engine yet. I want mockups when we get there for each design engine
  to see what works better for me."** So at the build step, the agreed design
  is built once per candidate stack and he compares them working; no stack is
  picked before that.

---

## Decision log

- **2026-09-15 [USER-DIRECTED]** This canon exists and is read before every
  design step. Founder, verbatim in the header.
- **2026-09-15 [USER-DIRECTED]** design-room is not the generator ("They all look
  extremely generic. So we should not rely on it").
- **2026-09-15 [USER-DIRECTED]** Kipi and small-business automation lead;
  investigations are depth.
- **2026-09-15 [USER-DIRECTED]** RULE-2026-09-15-A, -B, -C in `decisions.md`:
  stories anonymized, case-043 without names, fee credited, pain first, no
  three-box rows.
- **2026-09-15 [USER-DIRECTED]** Research first, then the style guide agreed,
  then build.
- **2026-09-15 [CLAUDE-RECOMMENDED -> APPROVED]** The rules become reasoning:
  `design-dna.md` is written as the generative layer, derived from the owner
  files (the business, the customer, who he is), modelled on how the voice loop
  works (identity, examples, corrections, then a lint). Founder: "Yes. But it
  must work from the canonical files and what we agreed the business does, who I
  am and who are the customers." Next, per the DNA's own section 9: test it on
  something the canon never mentions, then produce the style guide from it.
- **2026-09-15 [SYSTEM-INFERRED]** The DNA passed its cold test in part. A
  fresh session given only the canonical files designed a 404 page and the
  invoice email and derived its core moves from the reader and the idea, not
  from rules (the invoice as the quote and the bill agreeing; the 404 with no
  signal color because nothing disagrees). It could not produce any visual
  token (typeface, color value, spacing) because no style guide exists yet, and
  it had to guess two operational facts, now listed in section 10. Fixed in the
  DNA the same day: the annotated references section, which had been proposed
  and left out, plus the two test outputs as worked examples.
- **2026-09-15 [USER-DIRECTED]** Invoice timing settled (RULE-2026-09-15-D) and
  the style guide path approved: real design systems as references first, then
  style tiles the founder can edit in the Claude Design canvas.
- **2026-09-15 [USER-DIRECTED]** On the three tiles: leaning B (Report), NOT
  agreed. Too simple to judge as a site; he needs more design to understand the
  direction, using the tools in section 8, without the design chasing the
  customer's path so hard it loses what it puts across. Both lines are in
  `design-dna.md` section 10.
- **2026-09-15 [USER-DIRECTED]** The tools get judged from their code, not their
  READMEs. Result in section 8. Found along the way: the July taste-skill port
  into `dogfood_gate.py` never shipped (ASK-1735); Higgsfield has a hosted MCP
  (not connected) and a CLI; Remotion's skill was a broken link and is now
  installed. Imagery defaults to nano-banana (already wired); video after the
  look is picked.
- **2026-09-15 [USER-DIRECTED]** The "site is only HTML" premise is withdrawn; it
  was history, not a decision. The stack is an open founder decision (section
  10), recommendation Astro. Founder also asked that everything discussed keeps
  compounding here: every decision, correction and finding from a session
  lands in this file or `design-dna.md` in the same session it is said.
- **2026-09-15 [USER-DIRECTED]** RULE-2026-09-15-E: the site is his calling card
  as an AI expert; simple or sloppy makes him look bad. RULE-2026-09-15-F:
  logos for VMware, LinkedIn, Meta, Google, ElevenLabs. VMware added to
  `config/biography.json` after checking his own post. Both change the B
  mockups: they have to show craft, not only restraint.
- **2026-09-15 [USER-DIRECTED]** Stack not chosen now. At the build step, one
  working mockup per candidate stack (plain HTML, Astro, Next.js), founder
  compares and picks (section 10). "B quiet" dropped per RULE-2026-09-15-E; the
  design mockups are B rich and B bold.
- **2026-09-15 [USER-DIRECTED]** RULE-2026-09-15-G: the background is data
  analysis and data integrity (making sure things were accurate) through scam,
  foreign influence and malicious-actor work at scale, leading to trustworthy
  AI systems. Written into the owners (biography, voice identity, DNA) and
  section 3 here.
- **2026-09-15 [USER-DIRECTED]** RULE-2026-09-15-H: grab them first. The first
  screen contract is in section 1. Pedigree moves into the first screen,
  labeled. Interaction is depth only. Consequence for the mockups: the first
  screen is designed and compared on its own (three variants), then the page
  below it; B bold's pain picker is no longer a first-screen mechanic.
- **2026-09-15 [USER-DIRECTED]** Full design thesis written for an outside
  review (the founder is taking it to ChatGPT):
  `q-consult/output/site-design-thesis-2026-09-15.md`. Client names removed;
  it includes the three first-screen candidates with exact draft copy, the
  measured fit, my own list of weaknesses and ten questions. Whatever comes
  back gets weighed here, not adopted wholesale.
- **2026-09-15 [SYSTEM-INFERRED]** First-screen candidates published for the
  founder to compare: https://claude.ai/artifact/LxSUkLQMNb2zGBXsKMzGfQ (The
  person, The catch, The system; laptop 1440 x 900 and phone 390 x 844 each).
  All six meet the section 1 contract by measurement, pass `dogfood_gate.py`
  and have zero Impeccable tells. Nothing is agreed until the founder picks.
- **2026-09-15 [USER-DIRECTED]** External review received from ChatGPT and saved:
  `q-consult/output/site-design-review-chatgpt-2026-09-15.md`. Founder: "It has a
  lot of feedback that we should follow." Claude's assessment and proposed path:
  `q-consult/output/site-design-review-response-2026-09-15.md`. Headline
  findings accepted as true: no proof audit was done, the $1,000 week is not
  yet a product, the first screen became a packing exercise. First-screen
  picking is ON HOLD until the proof audit and the week are done. Two conflicts
  go to the founder: refusal as the lead differentiator (versus the 2026-09-11
  voice correction that guards mean nothing to people) and how prominent
  pedigree is on landing.
- **2026-09-15 [SYSTEM-INFERRED]** Naive comprehension gate, baseline on the three
  laptop first screens (3 fresh Haiku instances each, `--safe-mode`, control
  question answered "unknown" by all 9, so none had outside context). Verbatim
  answers: `q-consult/output/comprehension/baseline-2026-09-15.md`; script
  `gate.py` beside it. What they show: all 9 understood what he sells and that
  the $1,000 week is read only and credited; asked why to believe him, all 9
  cited only the employers, none cited the artifact or any result (outcome
  proof is missing, as the review said); "The system" confused 3 of 3 (is it
  consulting or bot software?); "The catch" read him narrowly as a billing
  reconciliation shop; several could not say what the week delivers. None
  thought he built AI at those employers.
- **2026-09-15 [SYSTEM-INFERRED]** Proof audit done (step 2 of RULE-2026-09-15-I):
  five files in `q-consult/output/proof-audit/` plus `INDEX.md`, which sorts every
  record by the five proof kinds and ranks the homepage candidates (top: a sheet
  row cutoff that hid 53 sales; an AI's invented number caught before the client
  saw it; the follow-up tracker that counted drafts as sent). Corrections made on
  the way: the Client A JA3 record is a miss, not a rigor win (section 6 of
  that file); the fused "369 files, zero conflicts" line added to ASK-1719; the
  Red Oak line in section 5 here corrected. First draft of the week as a product:
  `q-consult/output/offer/the-week-draft-2026-09-15.md`, with the founder's open
  questions in its section 5. Nothing in either file is approved copy.
- **2026-09-15 [USER-DIRECTED]** Value-hypothesis audit run at the founder's direction
  after the ChatGPT discussion ("more expert work, in less time, without degrading the
  work product"): six audit files under `q-consult/output/proof-audit/compression/`,
  decision document `q-consult/output/value-hypothesis-decision-2026-09-15.md`. Verdict
  PARTIALLY SUPPORTED: volume and standard measured, before-state hours absent in every
  engagement. Text comprehension gate: a discrepancy-led framing read as "finds errors"
  3 of 3; a compression-led one "both" 2 of 3. Proposed positioning D (the work only
  your expert can do, done by a system, with the evidence next to every answer) and a
  week whose deliverable is the measured baseline. NOTHING ADOPTED; the founder decides.
  `design-dna.md` section 4 unchanged until then. Found and filed: Client F sweep jobs not
  loaded while the live case study says "runs every morning" (ASK-1737).
- **2026-09-15 [USER-DIRECTED]** Correction to the entry above: the founder's stated
  manual durations ("weeks", "days", "40 hours a week") are reliable approximations and
  are the BEFORE column, labelled founder-estimated; the audit measures the AFTER and
  never re-litigates the before. Second run of the decision document: verdict SUPPORTED
  with one qualifier (the PI bought the standard, not speed). Ratios by script
  (`compression/scripts/founder_baseline_ratios.py`): investigation 8.7x to 13.1x, PI
  casework 3.2x to 4.0x, Client F research 18.5x on machine time. Baselines still open for
  Client A, Client B and the founder's own operation. Positioning pick still his.
- **2026-09-15 [USER-DIRECTED]** Third run of the value-hypothesis decision document,
  after the founder sent the session back to the canon ("refocus"). The two entries
  above are SUPERSEDED: the first read a missing before-figure as the verdict, the
  second turned the founder's estimates into ratios and public claims, which
  `the-business.md` ("never about hours saved") and the pain model's forbidden list
  do not allow. Corrected finding: the pattern (seam, then the work moves to a system
  at volume, then a standard that did not exist) is SUPPORTED in every engagement;
  three of the hypothesis's four layers are already canon; the fourth (speed said out
  loud) is one open founder decision: keep the rule and show compression by artifact,
  or amend the belief with a council check. Proof is ranked under the buyer's pain
  family (RULE-C), not as 53 sales versus compression. The founder's duration
  estimates are inputs to the week's design, never site copy.
- **2026-09-15 [USER-DIRECTED]** Correction to the entry above, founder verbatim:
  "You're conflating between the hours I'm selling and the measurement of my
  capability because what I'm saying is that without AI without the systems I built,
  everything I am doing for any of my clients would have taken me exponentially
  longer." Settles it: "never about hours saved" (`the-business.md`) is about the
  BUYER's hours; the compression claim is about HIS capability and is capability
  proof (design-dna 4b), the scarcity argument of RULE-2026-08-04-K with teeth. His
  first-person counterfactual ("this took me a day; by hand it would have taken me
  weeks") may be said on the site, labelled as his estimate, next to the artifact
  with its clock. The client-side form ("saves you 40 hours") stays blocked. No canon
  belief changes; the "one decision" in the entry above is withdrawn. The artifact of
  his own compressed work becomes the "why believe him" element the gate showed was
  missing (all 15 readers to date cited only the employers).
- **2026-09-15 [USER-DIRECTED]** RULE-2026-09-15-J: the ROI is the buyer's hours
  worked against hours billed, flipped by the build; his own compression is
  capability proof about him, sayable in his first person with the artifact. The
  pain model already carries the buyer-side numbers (CPA, law, A&E). The week's
  Friday baseline measures that gap for one process. `the-business.md` "never about
  hours saved" clarified in place, not changed.
- **2026-09-15 [USER-DIRECTED]** RULE-2026-09-15-K: the buyer's fear is that
  automation with AI lowers quality; the audited record shows his builds raise it
  (Client F, Client B, Client A, 4_points), and the reason is how he builds,
  which is the accuracy career turned into build discipline. Shown on the site as a
  fact with its artifact and explained as his background; never a guard list. J and
  K together are the finished hierarchy for the page.
- **2026-09-15 [USER-DIRECTED]** Founder answers, all for the website: (1) the
  finished hierarchy (RULE-J plus RULE-K) IS the idea the site is built on: "yes it
  is". (2) The Client F sweep jobs are old, unrelated to this project, and should not be
  running; no restart. The only website consequence: the live case study's
  present-tense "runs every morning" becomes a dated, past-tense artifact in the
  redesign (ASK-1737 re-scoped to that). (3) The week: Friday is a target, not a hard
  deadline; there is an initial kickoff call (what they need, how he can help),
  format still to iron out; findings are provided without confirmed / not-confirmed
  labels; day-one exclusions still to discuss. Recorded in
  `output/offer/the-week-draft-2026-09-15.md` section 6.
- **2026-09-15 [SYSTEM-INFERRED]** First screens, round 2, built after RULE-J and
  RULE-K: three variants by pain family, each with a real dated artifact of his own
  compressed work and his first-person line, pedigree secondary, action last.
  Files `q-consult/output/firstscreen/round2/` (build2.py, shoot.py, six PNGs).
  Tripwire passes all three; bio_gate clean; laptop action at 572 to 617 px of 900;
  phone action just below the fold (allowed by RULE-I, body text never under 15 px).
  Gate (`comprehension/round2-2026-09-15.md`, 9 of 9 controls unknown): the
  artifact answered "why believe him" 2 of 9 times (Hours i1, Seam i3) against 0 of
  15 in every earlier run; the rest still cited employers only. Defects found:
  Seam's ROI line read as the client overbilling (2 of 3); Hours' research log not
  connected to the timesheet pain (1 of 3); "the build" undefined, confused 4 of 9;
  Wrong read as a repair shop for broken AI (3 of 3), so it is a depth section, not
  a hero. Nothing picked; founder to compare.
- **2026-09-15 [CLAUDE-RECOMMENDED -> REJECTED]** (superseded by the next entry) scroll-craft
  (github.com/nateherkai/scroll-craft) judged from its code: a scroll-as-timeline
  runtime (1,211-line engine, pinned acts, parallax, worldflight camera), a kie.ai
  generated-asset pipeline, a contact-sheet verifier, and a FINGERPRINTS.md
  self-uniqueness registry. NOT adopted as a build tool: it collides with the
  one-reveal motion rule (section 8 already names continuous scroll animation as
  the opposite), RULE-H (no playing around on the site) and the real-imagery rule.
  Taken as mechanisms: (1) the fingerprint registry, adapted as
  `site/design/FINGERPRINTS.md` (pain family, headline shape, artifact type,
  composition, close, signature; a new round must differ on 4 of 6 from every row)
  and read by the design-chain gate next to the exemplars; (2) verification as a
  walk over states (rest, reveal, reduced motion), three frames per screen.
- **2026-09-15 [USER-DIRECTED]** scroll-craft ADDED to the tools. Founder, verbatim, on
  the entry above: "You took it way too hard on the one reveal rule. That's not a hard
  rule. That's if the UI supports it, then great. Same thing with the playing around,
  it's just something I said, I didn't make it a hard rule." Consequences: (1) the
  one-reveal motion line (design-dna section 4, this file section 6 rule 10) is a
  preference, applied when the UI supports it, not a gate; (2) RULE-2026-09-15-H's "no
  playing around" is a remark about the first screen's job (understood at once), not a
  ban on interaction; (3) scroll-craft is installed as the `nateherk-design` plugin at
  user scope (marketplace `nateherk`, v0.3.0): its runtime, its kie.ai asset pipeline,
  its contact-sheet verifier and its FINGERPRINTS registry are available; the
  design-chain gate still applies to any page it produces. The real-imagery rule
  (design-dna section 4) stands unless the founder says otherwise.
- **2026-09-15 [SYSTEM-INFERRED]** FIRST CHAINED ROUND, `site/design/2026-09-15/`, committed
  on `ci/wire-validate-2026-09-10` (`01d77a89`, `9cb69b07`). Three directions, all leading
  with pain family 1 ("someone retypes it, and money leaks there", the family section 5 of
  the value-hypothesis decision doc says the canon already leads with), each carrying a
  different artifact and a different proof kind. **Seam:** the pasted header and the names
  written into Column 14 (problem proof, Client B Record 7); the buyer's sentence is
  the large element. **Clock:** his own run log with the refused capture left in
  (capability plus reliability, Client F case-001 2026-08-09); type is quiet, the record is
  the evidence. **Record:** 441 marked missing, 388 after one run, 53 found (reliability
  plus outcome, Client B Record 5, ranked first of five in `proof-audit/INDEX.md`); the
  record is physically larger than the claim. Six pages, laptop 1440x900 and phone 390x844,
  PLAIN HTML ONLY: section 10 says the agreed design is built once per candidate stack, so
  Astro and Next.js come after the founder picks a direction, not before. 6 of 6 PASS
  `design-standard-check.py` at both viewports (round 3 failed the same check at 91 words
  and 5 text sizes). Nothing here is agreed until he picks.
- **2026-09-15 [SYSTEM-INFERRED]** What the round removed rather than softened, recorded
  because both are the class of error this canon exists to stop. (1) The first Clock build
  showed a refusal line with an invented timestamp. The real log has no per-line clock, and
  a fabricated timestamp on the one screen whose argument is that his records are honest is
  the worst thing the round could have shipped; the three rows are now transcribed from
  `projects/Client F/scripts/daily-sweep/logs/2026-08-09.log` in its own line order and the
  "31 times" is a scripted count over that file. (2) The founder's "40 hours a week" is not
  on any page: `proof-audit/compression/client-f.md` reads it against the record and returns
  UNSUPPORTED as stated (it is his own freelance contract ceiling, not a measurement of the
  manual work), so the before state is "74 rows over days", which the records do support.
  RULE-2026-09-15-J permits a first-person compression line, but there is no audited
  before-duration to attach one to, so the round carries none.
- **2026-09-15 [SYSTEM-INFERRED]** The design-chain gate blocked every step of the command
  it enforces, found on the first end-to-end run and fixed in kipi-system `9c7293c3`.
  `BASH_SHOW_RE` matched the gate's own filename and a second clause matched any command
  naming an open page, so `design-standard-check.py` (step 5), the serve, the shoot, the
  ICP gate (step 9) and `seal` itself (step 10) were all unreachable; the block message
  named `seal` as the remedy while blocking it. Now narrowed to the Bash paths that
  actually put a page in front of a person; the publish tools, the browser tools and the
  Stop hook are unchanged. Two new tests walk the chain steps through the hook, both seen
  red before the patch. RCA in kipi-system `q-system/output/rca/`. Fleet propagation and a
  sweep for other gates that block their own remedy: ASK-1745. Separately, `dogfood_gate.py`
  returns exit 0 both for "passed" and for "skipped because the path looked internal", so
  every tripwire run over a `/output/` path has been a skip reading as a pass: ASK-1746.
- **2026-09-15 [SYSTEM-INFERRED] WHERE TO PICK UP.** The design chain is the process
  (`/design-chain askconsulting`, gate `design-chain-gate.py`, config
  `consulting/design-chain.json`, rounds under `consulting/site/design/<date>/`).
  Before the chain existed, three rounds of first screens were built under
  `q-consult/output/firstscreen/` (round 1 in the earlier session's canvases,
  round2, round3); none has a chain, and round 3 fails the standard check (91
  words, 5 text sizes). They are history and reference, not a starting point.
  The first chained round starts fresh. What it inherits from today: the finished
  hierarchy (RULE-J, RULE-K), proof ranked under the buyer's pain family (decision
  doc section 5), the ICP-persona gate (`comprehension/gate_icp.py`), the standard
  numbers in `design-chain.json`, and the founder's verdicts on rounds 2 and 3:
  too many words, a block of words, not the research. Exemplars folder is empty;
  the first screen the founder calls closest goes in.
- **2026-09-16 [CLAUDE-RECOMMENDED -> APPROVED] The stack is Astro.** Round 2026-09-16d
  built one design three ways from one source (plain HTML, Astro, Next.js static export).
  Measured in `site/design/2026-09-16d/checks/stack-weight.txt`: HTML ships no own
  script but pulls GSAP from a CDN; Astro ships 3 own requests and 95,790 bytes of script,
  bundled from npm; Next.js ships 8 own requests and 548,872 bytes, mostly the React
  runtime for one animated island (uncompressed figures). Recommended Astro: components,
  npm packages bundled, output stays crawlable HTML that reads with scripts off, React only
  where a piece needs it. Founder, verbatim: *"Im okay with your choice for the design
  engine."* From round 2026-09-16e on, rounds build in Astro only; section 10 option (2).
- **2026-09-16 [USER-DIRECTED] The headline is centred.** Founder, on round 2026-09-16d:
  *"the text is again on lined on the left"*, the second time after 2026-09-15 (left-aligned
  everything reads as slop). Now measured, not remembered: `design-chain.json`
  `standard.hero_align = center`, held by `design-standard-check.py`. Three of the five
  exemplars centre the headline with the work below it (squarespace, calendly, notion).
- **2026-09-16 [USER-DIRECTED] Round 16d is too polished, and the background is not the
  exemplars'.** Founder, verbatim: *"yeah its too polished"*; *"I think the background is
  still not how it looks in the examples."* Measured against the captures: four of five
  exemplars are light pages; calendly's colour is a rounded panel inset on an off-white
  page (#fcfbf8), running #265994, #3875be, #6f90dd to #9a99e7 (pixels sampled from
  `references/calendly-com-laptop.png`); none is a dark full-bleed violet field, which is
  what rounds 16b to 16d used. One reader of three on 16d said the same unprompted: "The
  design is too polished. It feels like the AI marketing you hate."
- **2026-09-16 [USER-DIRECTED] Round 2026-09-16e is the picked first screen.** Founder,
  verbatim, on seeing it live: *"I like this"*. What it settles for later rounds: Astro;
  the headline centred with the work below it; calendly's inset rounded panel on an
  off-white page (#fcfbf8; #265994 / #3875be behind the words, #6f90dd / #9a99e7 below);
  the hours story as a rough.js hand sketch on a white sheet with GSAP motion that tells the
  story and nothing ambient; General Sans. Saved as
  `site/design/exemplars/2026-09-16e-picked-{laptop,phone}.png`. What it does NOT settle:
  the copy. The 16e reader gate had two of three readers call the line under the quote
  AI-written and vague, and all three asked for price and what the week delivers; that is
  the next round, and it waits on `OPEN-DECISIONS.md` first-screen-detail.
- **2026-09-16 [USER-DIRECTED] No price on the site; the first screen says what the week
  delivers.** RULE-2026-09-16-A. Founder: *"Dont show the $1000 at all."* and *"I want a
  high level of what the week delivers - it needs to be a representation of my expertise
  and mwhat they actually need"*. `test_site.py`'s four price tests are inverted when the
  rebuilt site ships. The machine-readable price stays (JSON-LD offer, llms.txt; founder:
  *"keep is there"*).
- **2026-09-16 [CLAUDE-RECOMMENDED -> APPROVED] The week is shown, not told.** Round
  2026-09-16f put the week in one line three ways and no variant moved the readers' question
  (what happens in the week, what do I get); the 80-word screen leaves the line about 13
  words. Recommended: the sketch continues into a drawn report of what the week hands
  back, four parts from the week draft section 3 (where the hours leak, the records behind
  it, what it costs, the build that stops it), each marked on the sketch where it applies.
  Founder: *"yes"*. Round 2026-09-16g builds it.
- **2026-09-16 [USER-DIRECTED, forwarded external review] The positioning moves from billing
  leak to expertise-preserving builds; the design stays.** The founder shared a review of
  round 16e without comment. Its verdict: the visual language is right ("clean, premium,
  restrained ... does not look like a generic AI consulting site"); the positioning is wrong:
  "The current hero makes the business look like billing/time-leak consulting." Its
  proposition, recorded as the reviewer wrote it: "take an expensive manual process
  performed by skilled people, understand how the work actually gets done, preserve the
  expertise/judgment inside it, and build a system that dramatically reduces the human labor
  required." Changes it asks for: keep "Eight hours, billed as two."; pivot at once to "Why
  does this work require eight hours in the first place?"; the diagram shows 8 hours of
  manual work, a system that handles the repeatable work, and about 2 hours of expert
  judgment, not "6 hours leaked"; make the build explicit (not an audit); name the problem
  type (expensive processes that resisted automation because they need judgment); show what
  changes in "Your system"; less vertical whitespace; employers as credibility, not the
  proposition; no generic AI language ("AI-powered", "agents", "automate/optimize/scale");
  keep the differentiator: separate expertise from busywork, encode the repeatable parts,
  keep humans where judgment is required. Desired takeaway: "My experts spend all week doing
  a process that shouldn't require all of their time. This person will understand how it
  actually works and build a system that does most of it without losing their expertise."
  Applied in round 2026-09-16g. **Two collisions, held rather than overridden, pending the
  founder:** (1) RULE-2026-09-15-J item 3 blocks a client-side "saves you N hours" number;
  the 8-to-2 drawing uses the quoted engineer's own numbers as the SHAPE of the target and
  is labelled as that, never as a measured result. (2) `segment-pain-model.json`
  `universal.forbidden` blocks headcount and replacement framing; the copy says the expert
  keeps the judgment, never that people are replaced. This review also supersedes the 16g
  headline variants drafted minutes earlier (who-he-is headlines): the headline stays.
- **2026-09-16 [USER-DIRECTED] The first-screen baseline is round 2026-09-16h, and its verbs
  stay.** Founder, after round 16i's broader verbs ("Collects / Reads / Cross-checks / Drafts")
  read as vague to test readers: "the diagram needs to describe recognizable work, not abstract
  system capabilities ... 'Reads / Retypes / Chases / Checks' worked because people can
  immediately picture humans doing those things." Retypes and Chases stay as the obviously
  wasteful half of the expert's day, Reads and Checks as the preparation half. The only
  one-verb alternative with a clear case (Checks to Cross-checks, round 16j) showed no gain
  against 16h in the same reader batch, so it was withdrawn. The phone icon stays (the CPA
  segment's pain is "emailing and calling for paperwork"). **Measured about the instrument:**
  the same 16h page kept 3 of 3 clean readers in one run and 0 of 2 in the next, so a 3-reader
  gate cannot resolve one-word changes; it is evidence, not a scoreboard. The signal that holds
  in every run from 16e to 16j is below the headline: readers want proof, what the system is,
  and whether 8 to 2 is realistic.
- **2026-09-16 [CLAUDE-RECOMMENDED -> APPROVED]** The reveal section (round 2026-09-16k)
  keeps its drawn process columns and its note wording. Founder answered "A" to both:
  (1) the recreated sheet keeps the Evidence and Reviewed columns, the ticks and the struck
  blank-capture row, although only the other six headers exist in the real sheet; the
  evidence numbers are real (2026-08-04 run log) and no specific failed row is claimed
  (round proof.md). (2) The note "Searched, de-duplicated and captured before anyone logged
  in" stays; one reader's confusion is not enough to change copy.
- **2026-09-16 [USER-DIRECTED] Round 2026-09-16k is the approved baseline, hero and reveal.**
  Founder: "Yes, approve the spreadsheet section as it stands." The reveal section (heading,
  one sentence, the recreated sheet, three hand notes, one closing line) is the baseline for
  the next rounds, which iterate on it and do not redo it. Screens saved as
  `site/design/exemplars/2026-09-16k-picked-*.png`. Next: 4 Points as supporting evidence and
  the links to other transformations, placed further down the page.
- **2026-09-16 [CLAUDE-RECOMMENDED -> MODIFIED] Every page has one job; no long scroll.**
  Founder: "I don't want that first page should have a job. The second page should have a job
  and so on." Picked option A (the Client F artifact stays on Home), with his modification: the
  reveal is not a second job. **Home's job:** "make the visitor recognize the problem and
  believe enough of the proposition to want more. The hero creates the question 'Does this
  actually work?' The single Client F artifact immediately underneath is the answer, not a
  separate case-study section." Home is hero, one real artifact, one call to action ("See the
  work"); the quotes block and everything else below it go. **Work's job:** the deeper proof:
  the full Client F story, 4 Points and its trust mechanism, the other real transformations; it
  ends with "How the week works". The full spreadsheet story is not duplicated: Home gets the
  minimal reveal, Work the complete evidence. **The journey:** recognition, glimpse of proof,
  deeper proof, what I buy, booking (Home, Work, The week, booking). **Later:** the live
  site's other pages (research and publications, the use cases from real work: `work/*.html`,
  `research/*.html`, `solutions/`, `about/`) are ported into the same format, one job each.
  This supersedes "further down the page" in the entry above.
- **2026-09-16 [CLAUDE-RECOMMENDED -> MODIFIED] The Home headline changes** (RULE-2026-09-16-F).
  A first-time reader (the founder's wife) found "8 hours of expert time / Only 2 need their
  judgment" awkward and unclear. The founder picked "Your team works more hours than it bills"
  from four options (recommended was "Your experts work 8 hours. Only 2 need an expert."), and
  had the end periods removed from the headline and the line under it. The drawing keeps the 8
  and 2 hours as the picture of why. Round 2026-09-16p. This supersedes "the headline stays" in
  the 2026-09-16 external-review entry above.
- **2026-09-16 [USER-DIRECTED] The redesign is live.** All eleven pages, from sealed round
  2026-09-16o, deployed to askconsulting.io on the founder's instruction. Every button books a
  30-minute call; the menu names the assessment (RULE-2026-09-16-D); no price anywhere
  (RULE-2026-09-16-C). Deploy path in `site/DEPLOY.md`.
- **2026-09-16 [USER-DIRECTED] Search and AI-search pass** (founder: "Research how to optimize
  the seo and aio for the site and apply it"). Round 2026-09-16q. Research: Google's guide says
  AI Overviews and AI Mode run on ordinary Search ranking, with no special markup, llms.txt or
  rewriting required; citation research finds relevance and dated, extractable facts help and
  formatting tricks do not. Applied: one linked JSON-LD graph per page from the site's own
  records (`tools/seo.py`, run by `deploy_build.py`), real sitemap dates, robots.txt naming the
  AI search and user-fetch crawlers, Home's search title and description on the approved
  headline, llms.txt corrected (price, call, podcasts), a favicon, the glued headline text
  fixed, link contrast raised, fingerprinted assets cached. Lighthouse on the deploy build: 100
  for accessibility, best practices and SEO on four pages. Not done: self-hosting the font
  (render-blocking), and Google Search Console, which needs the founder's login to verify the
  domain and submit the sitemap.
- **2026-09-16 [CLAUDE-RECOMMENDED -> MODIFIED] Footer, his face, official widgets** (RULE-2026-09-16-I).
  Round 2026-09-16s. A light three-column footer on every page (one column on a phone), a 36 px
  photo in Home's signature line, a photo card at the top of About, X's follow button in the
  footer and About's X card, LinkedIn's profile badge in the footer, more space between sections
  on phones. Not built: a dark footer on the hero field (LinkedIn's badge has no theme for it), a
  Contact page instead. The reader gate on About had two of three readers leaving on its
  unchanged first screen; open. LinkedIn serves no badge for his profile (a public profile gets
  one), so the footer shows the badge's plain link until his profile is public.

- **2026-09-17 [USER-DIRECTED] The seven-change review is approved in full; the Client F artifact becomes concept A; the two panel differences are brought into line.** The founder proposed seven changes and asked for an evaluation before any implementation (his brief: "someone should understand enough in a few seconds to want to keep looking. Do not solve problems by adding explanation ... I specifically want the site to remain restrained"). The review measured the live site: all 11 pages at 390, 768, 1024, 1280, 1440 and 1920 px (script `scratchpad/audit/measure.py`, results in `measurements.json`; no page scrolls sideways at any width). His answers, verbatim: **"One all"**, **"2 a"**, **"3 fix to match the rest of the site from a design perspective"**.

  **The approved set, in build order (each round is 16t plus its delta list, never a rebuild):**
  1. **The layout system.** Measured accidental variation: 31 distinct padding values and 22 margin values in the round's CSS; nine content widths (1180, 1060, 980, 780, 760, 720, 700, 640, 460) plus the 1300 px Home sheet; 13 border radii; the footer's content edge at 190 px against the header's at 170 px at 1440; section headings at 34 px (Home), 28 px (Work) and 26 px (everywhere else), plus fractional 18.48 px and 16.3 px from a scaled component; a second button size on About; the phone layout switching at 720 px in script and 760 px in the CSS, and only with JavaScript on. Rules to adopt: one spacing scale (4, 8, 12, 16, 24, 32, 48, 64, 96) with two section rhythms; three widths (frame 1180, figure 980, text 680); four radii (6, 12, 24, full); one size per type level; one button spec; one breakpoint shared by CSS and script. The hand-drawn irregularity is NOT touched (founder: "Do not sanitize the handmade aesthetic").
  2. **Navigation.** Writing moves to the footer (at 390 px the menu wraps "About" onto a second line on every page; /research is one threat-intel article and investigations are depth, not the buyer path). "What we do" is renamed "The work" to match the page it opens.
  3. **Home's artifact becomes concept A, "the loop with the person stepped out":** one drawn loop of four recognizable actions (search, screenshot, paste, check) with the figure inside it and tally marks piling up, then the same loop turning on its own with the figure outside holding the rules card, a sheet filling with rows, and one capture dropping out, "blank page: flagged, not filed". NOT a second before-and-after: the hero directly above already draws 8 hours against 2 hours of judgment. Numbers: the "40 hours a week" may appear only as his own estimate in his first person and never as the client's saving (RULE-2026-09-15-J); "roughly a day" is refused because the record is the measured run, 07:00:01 to file at 07:26, about 26 minutes unattended (`proof-audit/compression/client-f.md`). The full redacted sheet moves to the Client F case page, which today carries the pipeline drawing and not the sheet.
  4. **Work ends into the assessment:** the assessment's own five drawn day boxes, small, as the link, with "See the assessment" as the primary action and booking second. Today that transition is a small underlined link under a booking button.
  5. **About loses "The offer" (repeats the assessment page) and "Who you would be working with" (a third statement of the 12 years on one page).** The employer list is made consistent (Home names VMware; About and the assessment do not) and the GitHub counts (531 stars, 48 repos) get a date or a live source.
  6. **The hub page is grown from "What we build" (/solutions), not added.** That page is in no menu and no footer today; its eight jobs, each with what it replaces and what it will not do, are already the hub topic the founder confirmed ("What to hand to a system, and what to keep with your experts"). The nine LinkedIn and Substack spoke links, which point at the homepage since 2026-09-17, are repointed at it.
  7. **Unchanged:** the Home hero (headline, line, button, the 8-to-2 drawing and its verbs) and no video.

  **The two panel differences are FIXED, not kept** (founder answer 3): inner pages' screen-filling blue panel and Home's content-height panel become one rule, and the case pages' inset drawing card and Home's drawing on bare blue become one treatment.

  **Also found, queued with the rounds:** "What we build" is unreachable from the menu and footer; case labels disagree ("Research operations" against "Case study · intelligence, research ops", and "work ·sales operations" with the space on the wrong side of the dot); the Work list's text stops at about 490 px inside a 980 px column; the assessment's "We spend the week inside your business" reads as on-site although there is no in-person work; 721 to 1023 px is undesigned laptop layout.

- **2026-09-17 [USER-DIRECTED] Direction A is the layout system.** Founder, on the three sealed
  directions of round `site/design/2026-09-17`: **"A"**. A keeps the 1180 frame his approved
  screens (16e, 16k) were picked at and derives everything else from it: figure 980, reading text
  680, one spacing scale (4, 8, 12, 16, 24, 32, 48, 64, 96) with two section steps, four radii, one
  size per type level (28/24 headings, 18/17 body, 15 small), one button spec, one breakpoint.
  Measured against the live site before and after: heading levels 3 sizes -> 1; footer 1060 at
  x=190 against a 1180 header -> both 1180, first word under the logo; radii up to 8 per page -> 4
  on Home, 5 on inner pages; 31 padding values -> two section steps. All 24 pages pass
  `design-standard-check.py` and sit at or above the exemplar floor (`checks/gap.json`).
  **Two findings the gate forced, both kept as measurements rather than opinions:** (1) making
  every panel content-height broke the 80-word first-screen standard (work 92, case 123, the week
  154 words in view), so the inner pages keep the screen-filling panel and Home keeps its
  content-height one; the difference is now measured, not accidental, and direction C tested the
  opposite. (2) Direction B's narrower figure column scaled a drawn label to 16.48 px, which rounds
  onto the caption's 16 px and left 3 type sizes in the fold where the floor is 4; B was corrected
  to narrow only the reading column. Copy, drawings and the hero are byte-identical to 16t;
  `checks/` carries bio_gate (10 employer sentences, 0 failures), the tripwire (one allowed tell),
  impeccable (findings identical to 16t, none introduced) and the ICP reader gate (no reader left,
  none called him a repair shop). Exemplars: `2026-09-17a-picked-{laptop,phone}.png`.
  NEXT in the approved seven: the Home artifact, concept A (the loop with the person stepped out).

- **2026-09-17 [USER-DIRECTED] Home's artifact is the ring.** Founder, on the three sealed
  drawings of round `site/design/2026-09-17b`: **"Ring"**. The redacted research sheet under the
  hero is replaced by one drawing: four steps a visitor can picture (search, capture, file, check)
  drawn as a loop with a person inside it and tally marks beside it, then the same loop turning on
  its own with the person outside holding the rules, the deliverable filling, and one capture set
  aside with a cross. Three labels, all already-approved copy carried from the sheet it replaces:
  "Searched, de-duplicated and captured before anyone logged in", "Rules set by the team", "Blank
  page: flagged, not filed", plus "Every morning at 7". The phone build is its own stacked layout,
  not the laptop drawing squeezed. Component `components/Loop.astro`, ink by the shared
  `scripts/ink.js` hand (rough.js, fixed seeds, pens itself in once).
  **Deliberately absent, and why:** no hours and no ratio. "About 40 hours a week" is his own
  estimate and the Client F audit reads it as his freelance contract ceiling, so it may appear only in
  his first person and never as the client's saving (RULE-2026-09-15-J item 3); "roughly a day" is
  refused because the record is the measured run, 07:00:01 to the file written at 07:26
  (`proof-audit/compression/client-f.md`). The clock was reserved for the morning direction, which he
  did not pick, so this round prints no number at all. The full redacted sheet moves to the Client F
  case page in a later round.
  **Named for him rather than hidden:** this is the first drawing on the site with a person in it,
  and a stick figure is a new element in the hand. Checks: 6/6 pages pass the standard check, every
  page at or above the exemplar floor, bio_gate 3 sentences 0 failures, tripwire one allowed tell,
  impeccable control fired. The reader gate's one "would leave" is the standing hero finding from
  16e onward, not this artifact, which sits below the fold the gate reads (`gate/notes.md`).
  Exemplars: `2026-09-17b-picked-{laptop,phone}.png`.

- **2026-09-17 [USER-DIRECTED] The menu, the About cuts, and three ways to end Work** (round
  `site/design/2026-09-17c`). Writing leaves the primary navigation for the footer and "What we
  do" becomes "The work" (at 390 px the live menu wrapped "About" onto a second line on every
  page; /research holds one article). About loses "The offer" (every sentence restates the
  assessment page) and "Who you would be working with" (the third statement of the 12 years on
  one page), and the GitHub counts are dated "as of September 2026". Three page endings were
  built and sealed: the week strip, a plain hand-off, and the assessment as a fifth row.
  **A gate change came out of this round, not a workaround.** `site/about/index.html` is a COPY
  SOURCE: the served pages are built by the newest sealed round, which reads it at build time and
  carries its markup into the article, so a structural edit to it is a design change and the gate
  was right to block it. What the gate could not see was that the chain covering it had already
  run in the round that rendered it. A round now declares `sources.json`, the live pages it
  renders with a written reason each, and `seal` records the sha it sealed; the next edit to that
  source is red again (kipi-system `097043d2`).

- **2026-09-17 [USER-DIRECTED] The Work page ends in the visitor's own operation, drawn as an
  open row.** Founder, on the three endings of 17c: **"Choose the fifth-row direction, but don't
  make it look like a fifth completed engagement."** And: *"The visitor sees four pieces of work,
  then their own operation occupies the next position. That makes the Assessment the mechanism by
  which they become the next piece of work, without us explaining that in a paragraph."* Two
  instructions came with it and both hold: the five-day week strip does NOT appear on Work
  (*"Save that reveal for the Assessment page itself"*), and the copy is tested downward rather
  than treated as final.
  **Measured, and it corrected the previous round:** the four delivered rows carry NO drawn mark
  (`WorkHub.astro` renders vert, h2 and body; the 150 px column is empty on all four), so the open
  state cannot be carried by contrast with them. 17c's critique had said the opposite.
  Round `2026-09-17d` built three answers: their loop before, a frame with the pen lifted, and a
  reserved dashed space. Founder: **"Drawing 1 + D1."** His reason: *"The four rows above show
  work after I've changed it; the fifth shows the visitor's operation before I've touched it.
  Reusing the Home loop is okay here because it becomes a recurring visual language: Home teaches
  the problem, Work applies that problem to 'Your operation.'"* He refused the other two: the
  unclosed frame is *"clever once someone explains it, but a visitor shouldn't have to understand
  the designer's metaphor"*, and the dashed outline *"feels like a portfolio placeholder"*.

- **2026-09-17 [USER-DIRECTED] The row's line is the assessment's deliverable, not its purpose**
  (round `site/design/2026-09-17e`, the built pick). The row reads: "Your operation" / **"What to
  automate first, and what each costs"** / "See the assessment". The founder withdrew his own
  first draft of the middle line: *"'Find what shouldn't need your experts' is essentially another
  articulation of the Home proposition. It tells me why I'd do the assessment, not necessarily
  what comes out of it."* He asked for the line to be derived from what the week genuinely hands
  back, and it is: `/start`, verbatim, *"Friday, you get findings and priced options. What is
  worth automating, in what order, what each would take, and what each costs."* Of three options
  he picked the decision over the diagnostic and over the page's own "findings and priced
  options": *"#1 is a decision. A CEO immediately understands what they walk away knowing."*
  **What the line deliberately omits, each with its rule:** no dollar amount (RULE-2026-09-16-G
  puts the one price on /start), no "Friday" (his own answer: a target, not a hard deadline), and
  nothing running (RULE-2026-09-16-E: the week ends with a plan).
  **The page ending is now:** four delivered cases, the visitor's operation as the fifth row with
  the row itself as the only assessment link, and one quiet calendar link. The duplicate "See the
  assessment" button is gone, and so is the close sentence it replaced. Founder: *"four completed
  transformations, your untransformed operation, Assessment, quiet option to book. That's
  substantially better than four cases, explanation, CTA, another CTA."*
  Exemplars: `2026-09-17e-picked-{laptop,phone}.png`.
  **Second gate change of the day, same shape as the first.** The chain had no form for a round
  that BUILDS a pick: one direction was held to three headings and 27 critique answers, so the
  only ways to comply were to invent two directions the founder had just refused or to copy 18
  answers forward. A round may now declare `implements` in its craft manifest (the round, the
  direction, and the reason in the words it was picked in) and is held to one direction and nine
  answers. It cannot skip the fan-out: the named round must exist, be sealed, and carry three
  directions (kipi-system `d5f49445`, five mutations, five refusals).
  **Still open and deliberately separate:** the hub page grown from /solutions with the nine
  spoke links repointed, and the site-wide width, padding and rhythm audit the founder asked to
  keep out of this decision.

- **2026-09-17 [USER-DIRECTED] One rule for where a word sits in a drawing, and the research
  case gets a headline that is not a riddle** (round `site/design/2026-09-17f`, LIVE). Founder,
  within an hour of the deploy: *"I don't like the what it looks like for one research team
  diagram and the headline I don't think it's very clear and it's the boxes are kinda all over
  the place."*
  **Measured, and it moved the problem:** the boxes were never wrong (four process boxes, all
  110 x 90, one baseline). The WORDS had no rule. On that diagram, 3 labels sat above their box
  and 4 below, 3 were misaligned with the box's left edge by 10 to 14 px, and 6 were wider than
  the box they named. Across all five diagrams with boxes the mix repeats (investigations 4 above
  / 2 below, review 3 / 2, trail 2 / 3), and 18 labels site-wide are wider than their box.
  Three rules were built, measured and sealed. Founder: **"F1"**, every label the same width,
  centred under its box, all sharing one top edge. **F2** (the word inside the box, so geometry
  enforces the rule) FAILED ON ITS OWN RENDER, words landing across the icons, and is kept in the
  round as a measurement rather than an option. **F3** (numbers plus a key) works and costs the
  reader a second look; its key line was refused by `design-standard-check.py` at 104 characters
  against the canon's 90, and is two lines because the check said so.
  **RULE-2026-09-17-B: a label in a drawing sits in one declared relation to the shape it names,
  at one width, on one shared edge.** Applied to the research diagram only. The other four are
  the craft audit, which stays separate by his instruction.
  **The headline** is his pick of three derived from what `/start` says the week hands back:
  "The report that is finished before anyone arrives" becomes **"A research team's morning,
  already done at 7"**, changed in the title, the og:title, the h1 and the Work hub row together.
  His reason for rejecting the old one: it makes the reader work out which report, and arrives
  where. `site/work/daily-intel-sweep.html` and `site/work/index.html` are declared in the
  round's `sources.json`.

- **2026-09-17 [SYSTEM-INFERRED] A drawing with a phone composition ships BOTH and lets CSS pick.**
  Founder: *"It also cuts off on a pixel 8."* `Loop.astro` (round 17b, the ring) branched on a
  build-time `phone` PROP, but `deploy_build.py` ships the `-laptop` build of every page and the
  phone layout is switched at RUNTIME by the `.vp-phone` body class. So the phone ring written in
  17b was never in the deployed page at all. Measured live at 412 x 915: a 1160 x 560 drawing
  rendered 372 x 180 with two labels outside the figure, by 84 px and 47 px. `Art.astro` has
  always rendered `still-wide` and `still-narrow` together; the ring now does the same, and two
  collisions inside the phone composition, never visible because it had never rendered anywhere,
  were fixed with it. Written into `site/DEPLOY.md` alongside the second trap found the same day:
  re-copy `_astro/` AFTER the last build, because a content-hashed bundle copied early 404s the
  layout script, and the symptom is a phone rendering the laptop grid rather than a missing style.
  Exemplars: `2026-09-17f-picked-{laptop,phone}.png`.

- **2026-09-17 [USER-DIRECTED] Home's artifact is the morning pile, and the research team is gone**
  (round `site/design/2026-09-17g`, LIVE). Founder: **"Pile."**
  **What the pile is, and why it is not invented.** He rejected "daily collection" as a word that
  means nothing to his buyer and asked the right question: what sentence describes what they walk
  into? His own answer: *"these customers probably open their computer in the morning and get
  overwhelmed with emails and documents and slack messages and to-do's and things like that. Not a
  collection."* That is `config/segment-pain-model.json` in his words: the CPA's document chase
  where clients dribble paperwork in; small law's phone tag and follow-up rounds; and that
  segment's cause line, **"the state of a matter lives inside the documents, not in a system, so
  knowing anything requires a person to open something."** A heap of unopened things IS that
  sentence. The drawing carries no number, no clock, no client and no outcome.
  **RULE-2026-09-17-C: no mascot, and no generated illustration.** He asked about a cute robot and
  doubted it himself. Refused on the canon: `design-dna.md` section 4 allows real records
  recreated and bans an illustration standing in for work; `site-design.md` section 9 names "AI
  brain" art; contempt for AI-made marketing is the one finding all eleven researched industries
  share (`icp-working.md`); and a mascot makes it a toy exactly where RULE-2026-09-15-K says the
  buyer's fear is that AI lowers quality. The sorter stays what the hero already calls it: the
  system, drawn as a box. **Also corrected: `site-design.md` section 8 said nano-banana is backed
  by an MCP registered in consulting's `.mcp.json`. It is not** (that file registers apify, miyo,
  notion_api, perplexity-ask, reddit). `GEMINI_API_KEY` is set and the SKILL.md is on disk, but
  the server the skill calls is not wired here.
  **The four verbs are the hero's**, read live from `data/copy.js` SYSTEM_DOES: Reads, Retypes,
  Chases, Checks. The loop's old Search / Capture / File / Check were one engagement's pipeline
  steps, not the buyer's morning. Both drawings on Home now describe the same morning.
  **Every mention of a research team and of 7 is removed**, founder-directed: *"That's not my
  client. Stop talking about a research team. Stop talking about 7."* Title, og:title,
  og:description, h1, eyebrow, body, the Work hub row and its tag. The headline he had picked an
  hour earlier carried both.
  **This retires the ring on Home**, which he had asked to protect an hour before choosing the
  pile over it. Surfaced before building, not after.

- **2026-09-17 [USER-DIRECTED] The drawing flows on the page and fades at its edges; the footer's
  social links become one thing.** Founder on the blue version: *"It's two different colors of the
  blue background ... I actually really liked it on the white background before it just needs to
  be organized."* And: *"there wasn't really a defined box. It kind of faded in and faded out, and
  I want to try that."* And: *"I want the drawing to be more dramatic of the stack. Have it flow
  on the page."*
  **RULE-2026-09-17-D: one blue ground per page.** The hero's panel is the page's blue. A second
  panel for a second drawing is a second ground, and the drawing loses the page it belongs to. A
  drawing that needs presence gets it from scale and from an edge mask, never from its own box:
  the Home drawing spans the viewport with both edges masked, so the ink fades out instead of
  stopping at a line. No border, no panel, no card.
  **RULE-2026-09-17-E SUPERSEDES the widget half of RULE-2026-09-16-I: the footer's links are the
  site's own, never third-party widgets.** Founder: *"the bottom bar is a mess ... The links are
  weird. You have to fix them to make them more a part of the website, not just floating things."*
  Measured before changing anything: four social items in four different treatments. LinkedIn's
  official profile badge never renders as a badge, because their script serves nothing for a
  non-public profile, so it always showed as a bare blue link; X's follow button does render; the
  other two were plain text. Now one "Elsewhere" label over four links in the footer navigation's
  own style, and both third-party scripts are removed with the widgets they were loading. That
  also removes the only third-party cookies on a site whose own analytics is cookieless. His
  earlier instruction ("official widgets ... It looks a lot more professional") is reversed by him
  after seeing them live, and is recorded as a reversal rather than quietly dropped.
  Exemplars: `2026-09-17h-picked-{laptop,phone}.png`. Commits `a168b990`, `3186fa9c`.
  **STILL OPEN and named so it is not lost:** the case page's headline is "The morning collection
  nobody does by hand" and its row tag is "daily collection". Both still carry the word he
  questioned. He was offered three replacements and picked none, because the conversation moved to
  the drawing. His candidates are in that exchange; the strongest is "The morning pile, sorted
  before anyone opens it".

- **2026-09-17 [USER-DIRECTED] The tools are not optional, and a diagram gets three concepts like
  everything else** (round `site/design/2026-09-17g`, commit `d0f975e7`, nothing picked, nothing
  deployed). Founder, on pass 10 of the morning pile: *"This diagram is bad. You didn't use any of
  your tools on this. You have tools for motion, design etc. You also didn't use them on the blue
  box fading."*
  **What the tools returned, each a named gap rather than an opinion.** `concept-as-sketch`
  (Buxton, via design-room's art-direction canon): passes 1 to 10 took the first idea and restyled
  it ten times, which collapses the design space before it is explored. `design-dna.md` section 8
  step 3 already says produce THREE directions; skipping it at pass 1 is what the ten passes paid
  for. `figure-ground` (Koffka) and `universal-principles` (Lidwell): the drawing had no figure and
  no focal point, four equal-weight subjects on one flat plane. `artifact-diagramming`: nine labels
  in four different relations, and two unlabeled arrows, which say "related somehow".
  `hyperframes-animation`'s `depth-scatter-assemble`: the pile-to-stack travel was twelve
  independent tweens with a `Math.floor(i / 8)` lane hack, so the arrivals had no shared clock.
  **Three compositions, not a pass 11.** The CONTENT stays exactly as he settled it (a heap of the
  four kinds, the system titled and distinct from the words under it, a stack built from the same
  papers, two set apart in their own tray). What differs is the arrangement, which is what "it
  looks weird, it took me a second to figure out what that means" is about. **A, the gate:** the
  system spans the drawing's full height and the paper passes THROUGH it. **B, the desk:** top to
  bottom, ONE composition at both sizes. **C, the fork:** one drawn line leaves the system and
  splits, and the height difference between a tall stack and a two-item tray is the claim.
  **Two craft rules came out of it.** Every label sits BELOW the shape it names, left-aligned to
  it, at that shape's width (RULE-2026-09-17-B extended from the research diagram to this one,
  which takes the drawing from nine labels to four). And a sheet in the stack carries ONE mark
  rather than its whole face: at 300x48 with a 44px overlap the envelope chevrons crossed into the
  sheet above, so the tidiest thing on the page rendered as the busiest.
  **A and C have real phone compositions**, not the landscape drawing scaled: at 390 the scaled
  version ran C's fork off the right edge and turned A's gate into a 1000px corridor. Worth knowing
  when picking: A's gate and B's band are near-identical on a phone, because a vertical gate has
  nowhere to go in 390px except across.
  Measured across all six renders: no label lands on a box it does not name, no verb overflows the
  system box, nothing runs off an edge. Preview: `pile{a,b,c}-{laptop,phone}.html` in the round's
  astro build.

- **2026-09-17 [CLAUDE-RECOMMENDED -> APPROVED] The panel fade is interpolated, not typed.** The
  46 hand-written sRGB stops recorded in the pass-7 note existed to defeat the banding a naive
  two-stop sRGB ramp produces. That is the browser's job and a hand ramp is the wrong tool for it:
  the gradient is now SIX anchors interpolated `in oklab`, which is perceptually even by
  construction, with the plain-sRGB line kept above it as the fallback. The anchors are the same
  measured ones the pass-7 note names and are unchanged: `#fcfbf8` the page, `#265994` the
  exemplar's darkest sampled blue, `#3875be` the floor the 16h rule holds behind every white word,
  `#9a99e7` calendly's periwinkle in the tail where nothing is written. Verified after the change,
  not assumed: sampling one column down the whole panel gives ZERO rows with an adjacent-row
  channel jump of 3 or more, and `tools/text_contrast.py` still returns 0 lines below threshold at
  1440x900. The pass-7 reasoning about masks is unchanged and still correct (a mask fades alpha,
  which is not perceptually linear); this replaces the hand ramp, not the decision to fade in
  colour.

- **2026-09-17 [USER-DIRECTED] Home's artifact is the seam, and the idea is the second touch**
  (commits `1c4eaf2d` the sketch sheet, `83fa8ca3` the build; nothing deployed). Founder, on
  pass 10 of the pile: *"Scrap this entire sketch and make a new sketch of the idea of what you
  want to make. Scrap this one completely. And do it with all your tools."* Then, off the sheet:
  **"the seam"**. And on motion: **"go"**.
  **THE IDEA, and it was read rather than invented.** `config/segment-pain-model.json` is the
  runtime owner of the pain and beats prose. Its `universal.core_belief`, verbatim from the
  Aug-24 research: *"Work arrives through uncontrolled channels. A human retypes it into the real
  system. Follow-up is manual and endless. Money leaks at exactly those seams."* Its forbidden
  list states the offer in the negative: *"We sell a count of what is falling through, not
  savings."* And the thing that had never been read: **two of the three GO segments carry the
  same `countable_noun`, word for word** — CPA and tax, and small law, both "documents that
  needed a second touch". Their deliverables repeat it. Architecture's is the same shape against
  a fee. So the site's drawing and the week's deliverable are the same object.
  **THE SEAM.** Two columns, what arrived and what the system has, on SHARED BASELINES so a pair
  is a flat line and costs the reader nothing; the rows that never crossed run a short way into
  the channel between the columns and stop. The system's column therefore has HOLES in it, which
  is the fact being drawn. One figure, the channel, and it is the only place colour appears.
  Three labels on one shared baseline, each above the thing it names at its width
  (RULE-2026-09-17-B). **No number anywhere:** the count is what the week returns, and a figure
  invented for a drawing is what `no-mental-arithmetic` exists to stop.
  **MOTION IS NOW TWO THINGS, and the second is new to this site.** The reveal pens the columns
  in and drops the misses into the channel LAST, so the claim lands last, then it stops. The
  POINTER half is the one every round so far has been missing: `references/NARRATIVE.md` s5
  measured the five target sites at roughly 40 transitioned elements per 1 animated one, with its
  own verdict on my rounds, *"exactly one load animation and zero interaction states. The group
  does the opposite."* Hovering a row lights it on both sides, or lights its drop if it never
  crossed.
  **Three defects this found, all of them in shared code rather than in the drawing.** (1)
  `faint` existed only for the blue ground; on paper it silently returned full ink, so lines meant
  to recede were drawn at the weight of the records they connect and the whole thing read as a
  grid. (2) `data-pair` did not survive the re-ink: rough.js REPLACES the authored element with
  its own group, so any attribute the page reads afterwards has to be copied in `sketch()` or the
  hover silently does nothing. (3) The component shipped without its viewport switch, so BOTH
  compositions rendered at once and the one below the fold never played; three CSS lines, the
  same ones `lp-wide` / `lp-narrow` and `Art.astro`'s `still-wide` / `still-narrow` already had.
  **Also corrected, about my own verification:** `__inkSettled` means NOTHING IS MOVING, not that
  a drawing has played, which ink.js says in its own comment. A figure that has not started yet
  reads settled, so a screenshot gated on it catches a half-drawn frame. Waits now go on the
  timeline's own `progress() === 1`.
  Checks at both viewports: one drawing shown, reveal at progress 1 with 0 undrawn paths, 0
  groups outside the canvas, the three labels on one shared baseline, 0 page errors, and
  `text_contrast.py` 0 lines below threshold on Home at 1440x900.
  **Open, and named so it is not lost:** on a phone the two column headings wrap to two lines
  while "What arrived" stays on one. They are bottom-aligned so the label rule holds, but shorter
  phone wording would read better and that is a copy decision, not a layout one.
- **2026-09-18 [USER-DIRECTED]** The hero's "2 hours of judgment" box, blank per RULE-2026-09-18-C
  item 3, gets its content: **"Checking it's actually true."** Picked from three candidates pulled
  in the vision session (`site/design/VISION.md`), sourced from `segment-pain-model.json`
  `working_belief` (today's corrected diagnosis, RULE-2026-09-18-G) over the design-dna "two
  records" framing and the verbatim A&E buyer quote. Not yet checked against the hero word/piece/
  line caps in `design-chain.json` (`max_hero_words: 18`, `max_hero_pieces: 2`, `max_hero_lines: 3`)
  alongside whatever else lands in the box.
- **2026-09-18 [USER-DIRECTED]** RULE-2026-09-18-C item 3's SECOND hero defect (the system box's
  verbs show nothing saying it ever stops) shapes as **a small fifth element after the checklist**,
  a distinct beat rather than folded into Reads/Chases/Checks. Section 11's beat 3 is the source:
  *"where it cannot prove one it stops and says so rather than guessing... Beat 3 is the only part
  that is his."* Label picked: **"Unsure? It stops"** This was the item skipped in the first pass
  through the hero walkthrough — caught when the founder asked for it back.

---

## 11. The story the section under the hero tells (RULE-2026-09-18-B)

Added 2026-09-18, founder-directed. This is the SOURCE for that section's copy and its drawing.
Anything built there is built from this, not from an engagement.

### The three beats

**1. Their week now.** Work reaches them through channels they do not control: email, a phone
call, a PDF, a message. Someone on the team opens each one and types it into the system that
actually matters. Then chases what is missing. Then checks it landed. None of that is the work
they are paid for, and all of it happens before the work they are paid for can start.

**2. What it becomes.** The arriving and the typing stop being a person's job. When they sit
down, that part is already done. What is in front of them is the part that needed them: the
handful of things a system should not decide on its own.

**3. How.** He watches how the work actually gets done, finds the parts that do not need their
expertise, and builds a system for exactly those parts, around the tools they already use. The
system shows where each answer came from, and where it cannot prove one it stops and says so
rather than guessing.

### Why beat 3 is not optional

Beats 1 and 2 on their own are every automation pitch on the internet, and this buyer has read
them. Beat 3 is the only part that is his: *"Our systems refuse to guess. Where a system cannot
prove an answer it stops and tells a person. That is an acceptance criterion, not a sales claim"*
(`the-business.md`). It is also the answer to RULE-2026-09-15-K, the fear that automating with AI
lowers the standard. Told without beat 3 the section is generic; told with it, no other
consultant's page fits.

### What this section is NOT

- **Not proof.** It describes what the work is like, never that it happened. Proof lives on the
  Work pages and the case pages.
- **Not a client.** No engagement, no industry, no setting. RULE-2026-09-18-A keeps publication
  anonymized and this section goes further: it names nobody at all.
- **Not a number.** No count, no hours, no ratio, no clock. A number here would be a proof claim
  in a section that carries no proof, which is the exact failure `no-mental-arithmetic` exists to
  stop.
- **Not the hero repeated.** The hero states the pain in words. This section shows the week and
  the change; it does not restate the headline in a second language, which is what the pile and
  the seam did.

### What the drawing has to do

**SUPERSEDED 2026-09-18 by RULE-2026-09-18-C, hours after it was written. Kept, not deleted.**
This part asked for a second drawing under the hero. Reading the hero's own component and render
showed it already draws all three beats above, so a second drawing was the hero's second lane
repeated. Home now has ONE drawing and the three beats are the HERO's specification. The section
under the hero becomes words and links. Everything above this heading in section 11 stands: the
beats, why beat 3 is not optional, and what the section is NOT.

The two defects the hero has to fix, both measured: its "2 hours of judgment" box is mostly empty
and readers called it blank unprompted in both 17i gate rounds; and its system box reads, retypes,
chases and checks with nothing saying it ever stops, which is beat 3's missing half.

#### The superseded text

One drawing, under the three beats, carrying beat 2 and beat 3 together: what is already handled
and what is deliberately set aside for the person. The set-aside items are the figure, because
beat 3 is the only part that is his. Everything already handled is quiet.

The measured reason the drawing stays at all: `site/design/2026-09-17i/is-the-second-drawing-necessary.md`
found that across 23 gate runs, 101 reader statements naming the second drawing produced 51
negatives and 1 "it helped". That analysis recommended removing it. The founder chose the third
option: the emptiness was the defect, not the form. A drawing carrying this story has never been
tried; every drawing so far carried either a metaphor or an engagement.

