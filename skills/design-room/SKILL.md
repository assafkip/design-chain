---
name: "design-room"
user-invocable: false
description: "Codified design tool for product websites and marketing pages. LED by an art-direction lens (a senior art director: is there a subject, a composition, one ownable idea?) that sets the bar first and runs a visual-diff critic last; the 7 evidence-bound usability/anti-slop lenses (first-impression, conversion-usability, decision-psychology, positioning-retell, technical-accuracy, boldness-feasibility, anti-slop) are constraints on its vision, not peers. Grounds every token + design decision in real references, and builds against a vetted palette. Every decision traces to a cited attention or art-direction principle, a real grounded token, or a founder fork — never to an unsourced opinion. The tool refuses to score resonance; Claude assembles, the founder's eye + the market decide. Use when the user wants to design or redesign a website, landing page, or product marketing page, or mentions 'design room', 'design review', 'lens review', 'art direction', or wants grounded multi-lens feedback on a design. Reads codified attention + art-direction canons (no per-run web search); modernity comes from a weekly pulse."
---

# Design Room

A codified design tool. Not a panel of characters who argue. Seven evidence-bound
review **lenses** examine a page; each lens may only cite a principle, fact-check
against grounding, or surface a forced-choice fork. The room produces a fork sheet
and a grounded spec. **Claude assembles, the founder decides.**

## The cut (why this is not personas)

design-room used to voice many characters who argued and "converged." That made
Claude play both sides and call the winner a decision. v2 replaces them with the 7
lenses below. Each lens is bound to evidence: a cited principle from the attention
canon, a fact-check against real grounding tokens, a forced-choice fork the founder
resolves, or a hand-off to the reactive anti-AI gate. The full rationale + the
14→7 mapping is in the design-room-v2 gate-0 decision (in the gtm repo).

## Lenses

These are exactly the 7 (the machine-readable registry + the contracts that gate
this skill live in the gtm repo at `gtm/design-room/`). A lens NEVER originates a
token/color/font/copy line and NEVER resolves its own fork.

| Lens id | What it checks | Bound to |
|---------|----------------|----------|
| `first-impression` | survives the 50ms / first-3-second scan; primary action on the F/Z path in the first screen | cited (Lindgaard 2006, F/Z, hierarchy) |
| `conversion-usability` | interaction cost: target size, choice count, self-evidence, heuristic violations | cited (Fitts, Hick, Krug, Nielsen) |
| `decision-psychology` | a stressed buyer recognises their situation and acts; polish is honoured not faked | cited (aesthetic-usability, recognition-over-recall) |
| `positioning-retell` | which one-sentence retell is the page's spine | **fork** (founder owns positioning) |
| `technical-accuracy` | every technical claim / code sample / screenshot matches a grounding source | grounded fact-check |
| `boldness-feasibility` | where to spend the ONE bold, pattern-breaking moment vs scan-speed + LCP budget | **fork** (Von Restorff + perf) |
| `anti-slop` | generic copy, convergent fonts, gradient-text, emoji icons, "show the situation, don't name the feeling" | the reactive anti-AI **gate** |

Each cited lens reads the **attention canon** ([references/attention-canon.md](references/attention-canon.md)) —
the named, sourced principles and the one testable rule each implies. The lens
does not search the web; the canon is its source of truth.

## The LEAD lens — `art-direction` (a senior art director, not an 8th peer)

The 7 lenses above are the usability / anti-slop **floor**. They are a PM, a
UX-researcher, and a conversion-optimizer. None of them is an art director — so a
page can clear every one of them and still have **no subject, no composition, and a
library-default look** (scar `design-room-blind-to-art-direction`). The
`art-direction` lens (in `lens-registry.json` as `lead_lens`, source kind `lead`)
fixes that: it **LEADS** the room. The 7 floors are demoted to **constraints** on its
vision, not peers that outvote it.

It reads the **art-direction canon**
([references/art-direction-canon.md](references/art-direction-canon.md)) and works in
three layers: **L1 CRAFT** (is there a subject? is it composed? bespoke or default?),
**L2 CONCEPT** (is there ONE distinctive, ownable idea?), **L3 TRUTH** (right for THIS
product, ownable by THIS brand, resonant with THIS buyer).

- It **runs first** (Phase 2) to set the bar from the reference's design decisions
  (`grounding/design-decisions.json`), read through the canon.
- It **runs last** (Phase 6) as a **visual-diff** critic: `check_design_diff.py`
  emits the gap-list (subject? composition? bespoke? finish?) against that bar.
- It blocks on a missing subject / composition / craft the way `anti-slop` blocks
  slop — but it **never resolves its own fork**, **never originates a token or copy
  line**, and **never scores beauty or resonance**. L3 is a **refusal**: the tool
  hands resonance to the founder + a real buyer.

## Dashboard-mode lenses

The 7 floors + the LEAD lens above are `marketing` mode (narrative sites, grounded to
real reference teardowns). `lens-registry.json` also declares a `dashboard` mode for
dense product UI, grounded to the chosen design-system docs plus real dashboard
references (not narrative teardowns). Dashboard mode swaps the 7 marketing floors for
4 dashboard lenses. The same rule holds: a lens never originates a value and never
resolves its own fork.

| Lens id | What it checks | Bound to |
|---------|----------------|----------|
| `information-density` | the right density for the operator's job: mono numerals, 1px separators over card boxes at high density, spec-sheet over card grid | cited (Tufte data-ink, mono numerals) |
| `task-flow` | which one operator task the screen is optimised for, and whether that path is short and obvious | fork (the founder owns the primary task) |
| `data-legibility` | dense data stays scannable: numeric alignment, tabular numerals, a real label / value / delta hierarchy | cited (tabular numerals, alignment) |
| `state-completeness` | every interactive surface has a loading skeleton (not a spinner), a composed empty state, an inline error state, a tactile press | the reactive **gate** (missing any is a gap) |

Dashboard grounding sources live under `grounding_by_mode.dashboard` in the registry.
The `verify_design_room.py` validator (a required check in `gates run`) reads every
lens id from the registry across all collections, so each id above is a checked
reference, not documentation alone.

## Workflow

**The sanctioned entrypoint is the executor, not discipline.** Every phase below is
driven through `gtm/scripts/design_room_run.py` — the one component that walks
`gtm/design-room/pipeline.json` in order and FAILS CLOSED on a skipped mandatory
phase, a missing artifact, or a failed checker (postmortem DR-2026-07-04-01: an
operator skipped Phases 0/4/6 and published with zero tool resistance because the
graph was declared data with no executor). The verbs:

```
design_room_run.py start   <project>              # Phase 0 first write: run-state.json (mandatory)
design_room_run.py advance <project> <stage-id>   # the ONLY way a phase completes; runs its checker live
design_room_run.py resolve-fork <project> <fork> --choice ... --by founder   # Phase 3 fork gate
design_room_run.py preview <project>              # gated preview — only after the design-md phase
design_room_run.py status  <project>              # receipts + next expected phase
```

`advance design-md` refuses until every fork in `forks.md` has a founder
`resolve-fork` receipt (the agent may not self-resolve — the grounded-mode rule is
now a coded hard-stop). `preview` is the sanctioned "founder needs to see something"
path: it routes THROUGH the gate instead of around it. Do not hand-run the phase
checkers or build outside the runner; a phase that did not advance through the runner
did not happen.

The line is: ground (+ emit the steal-manifest + the design-decisions teardown) ->
the LEAD lens sets the bar -> the concept phase widens to N>=3 forks -> review
through the 7 floors -> the braintrust raises gaps -> assemble a fork sheet -> the
founder resolves the forks -> write a grounded design.md spec -> build -> run the
technique-parity regression alarm + the LEAD lens's `check_design_diff.py` +
diagnostics (which never say "done") -> founder's eye. It never originates a
decision for the founder, and it never declares the page done — only the founder's
eye + the market do.

### Phase 0: Runtime contract (canon-drift guard)

Before reading old PRDs, site notes, or handoff docs, load the repo's active
`gtm/design-room/current-contract.json`. The old Claude Design flow is superseded:
the active rule is no LLM-originated design decisions. Every run keeps one
`<project>/design-room/run-state.json`, then clears
`python3 gtm/scripts/check_design_room_runtime_contract.py <project>/design-room/run-state.json`.

The run-state is the executable router for the session. It binds the selected
reference, selected generated/source asset, founder fork, built HTML, and the
traceability chain: source -> design.md -> DOM selector -> rendered proof. If that
chain is missing, the agent is routing from memory again.

### Phase 1: Initialize or Load

**New project:** Run `scripts/init_project.py`. Populate `founders-brief.md` with
the product, the founder, and constraints.

**Existing project:** Read `founders-brief.md`, the `decisions.md` ledger (the
compounding record of every prior decision + why), and any prior `grounding/`,
`design.md`, and fork-sheet from the project's `design-room/` directory. The
decisions ledger is how prior sessions' reasoning carries forward.

### Phase 2.0: Grounding (before any lens runs)

Teardown the founder's reference sites into REAL tokens. See
[references/grounding.md](references/grounding.md). Fingerprint each reference
(stack-recon / Figma MCP), extract tokens + the WHY into `grounding/tokens.md`.
Every candidate token the build will use must originate here, not from Claude.

### Phase 2: Lens review — LEAD lens FIRST, then the 7 floors

The **`art-direction` LEAD lens runs first.** Before the floors weigh anything, it
reads `grounding/design-decisions.json` through the art-direction canon and writes
the **bar** to `review/art-direction.md`: the reference's hero subject, composition,
art-direction approach, and bespoke-vs-default — the design decisions the build must
reach. The 7 floors then run as **constraints** on that bar (a bold subject still has
to clear `first-impression` and `conversion-usability`). The LEAD sets the ceiling-
reach; the floors keep it honest.

Then run each of the 7 floors over the brief + grounding. A lens emits ONLY one of:
- **cited:** "principle X (canon) implies rule Y; the page does/doesn't" — with the canon ref.
- **grounded:** "claim Z on the page matches/does-not-match grounding source S."
- **fork:** "open choice — A vs B; founder picks" (positioning-retell, boldness-feasibility).
- **gate:** hand `anti-slop` to the reactive gate in Phase 6.

Write each lens's output to `review/<lens-id>.md`. A lens that states a preference
without a citation, a grounding source, or a fork is malformed — drop it.

### Phase 2.7: Concept phase (widen to N>=3 forks — the tool may not pick)

Before synthesis, the LEAD lens runs the **concept phase**: it generates **at least
three (N>=3) divergent concepts** for the page — distinct *ideas*, not restyles of
one idea (canon `concept-as-sketch`, Buxton: widen the design space before choosing).
Each concept is written as a **fork** under a `## Concepts` heading in `forks.md`
with its big idea, its hero subject, and its composition — and **carries a trailing
`source:`** (a variation derived from `grounding/design-decisions.json`, an approved
`generated:<asset>` under `build/art/`, or an explicit founder seed `fork:<id>`). A
concept with no source is the agent inventing the idea from taste and dressing it as
a fork — exactly what this phase forbids — and is rejected by
`python3 gtm/scripts/check_fork_provenance.py <project>/design-room/forks.md`.
**The tool may not pick** — concept is the TOP fork the founder resolves, the same
fork discipline as every other lens. **No auto-converge:** the room widens the
options; the founder chooses. Taking the first idea and styling it is the failure
this phase guards against (`check_fork_provenance.py`).

### Phase 3: Synthesis + braintrust (assemble + raise gaps, do not decide)

First, the **braintrust**: run **at least 3 INDEPENDENT critic passes** over the
assembled work (Catmull's Braintrust; Barrett's describe -> analyze -> interpret ->
judge; Lerman's Critical Response Process). Each critic **raises gaps**, evidence-
bound (it cites a design decision or the visual diff); **none decides**, there is **no
vote**, and the founder is the creative director with final authority. This is not a
debate that picks a winner — it is independent gap-raising that hands up.

Then collect the lens outputs + the concept forks + the braintrust gaps into a single
**fork sheet** (`forks.md`): every open choice, each as a forced-choice with the
evidence on each side. Claude **assembles** this sheet. Claude does not pick. The
founder resolves each fork. This is the line: **Claude assembles, the founder
decides.** Record the founder's picks back into
`founders-brief.md` (layered, never replacing). Then APPEND one entry per resolved
fork to `decisions.md` via the deterministic appender (never hand-edit the ledger):
`python3 gtm/scripts/check_decision_log.py append <project>/design-room/decisions.md
--date <today> --title "<short>" --decision "<what>" --tag <FOUNDER-DECIDED|FORK-RESOLVED|
LENS-CITED|GROUNDED> --ref <founder|fork:id|canon:id|grounding/path> --why "<why>"
--supersedes <none|prior-id>`. See [references/decisions-template.md](references/decisions-template.md).

### Phase 4: Grounded mode — the design.md spec

Write the resolved decision to `design.md` (tokens + rationale), NOT prose. See
[references/design-md-template.md](references/design-md-template.md) and the
grounded-mode rule below. Every token MUST carry a `source:` pointing at a
`grounding/` entry or a founder fork. A token with no source is rejected — Claude
may not originate one to make the page work.

### Phase 5: Build (wire the vetted palette)

Build the real page from `design.md`. **Before building, the composition and copy
must be grounded — not just the tokens.** Run, and clear, both:
`python3 gtm/scripts/check_layout_provenance.py <project>/design-room/design.md` and
`python3 gtm/scripts/check_copy_provenance.py <project>/design-room/design.md`. Every
`## Layout` and `## Copy` line must carry a `source:` (grounding / fork / generated).
A sourceless layout or copy line means the agent is about to compose or write the
page from its own taste — the build does not start until both clear. The build
**translates** the grounded spec; it does not invent the gestalt.

The build palette ([references/build-palette.md](references/build-palette.md)) is the
vetted menu; it carries a **last-refreshed date** maintained by the weekly modernity
pulse (see "Modernity" below). Install only the repos the spec names. Wire the ONE
signature moment, assemble sections, run it with zero console errors.

### Phase 6: Convergence gate + the LEAD lens LAST (visual diff)

Run the gate before showing the founder. See
[references/convergence-gate.md](references/convergence-gate.md): the eyeball
render gate + impeccable detectors + vercel guidelines, then cross-check the spec.
This is where the `anti-slop` lens actually fires. Write `build/gate-report.md`.

Then the **`art-direction` LEAD lens runs LAST** as the closing **visual-diff**
critic, every run. The build's design decisions are **NOT authored by the agent** —
that is the agent grading its own homework. They are **extracted from the built
HTML**: `python3 gtm/scripts/extract_design_decisions.py <built.html> -o
build-design-decisions.json`, then bound to the render with
`python3 gtm/scripts/check_decisions_provenance.py build-design-decisions.json <built.html>`
(the built HTML is the AUTHORITATIVE page under review; it FAILS on a hand-authored,
stale, inflated, or wrong-render record — the JSON must equal a fresh
extraction from the artifact). Only then run
`python3 gtm/scripts/check_design_diff.py build-design-decisions.json
grounding/design-decisions.json`. It emits the **gap-list** (subject? composition?
bespoke? finish?) against the bar the LEAD set in Phase 2 — the design twin of
`check_technique_parity.py`. It **never prints a verdict**; it hands the gap-list up.
Never call the design "good" to the founder — the gates are the floor, the founder's
eye + the market are the only ceiling.

If `run-state.json` says `motion.required: true`, run
`python3 gtm/scripts/check_motion_reference_parity.py <project>/design-room/run-state.json`
before showing the founder. This checker samples the declared DOM selector over
time and after scroll. GSAP/Lenis/Rive/canvas presence is not enough: the subject
named in run-state must visibly move. A generated still image is a style frame
unless the run-state explicitly marks the reference as static.

**Record the traceability chain BEFORE advancing convergence (executor).** The
`convergence-lead-last` stage now runs TWO checkers via the executor: the decisions
equality gate AND the FULL runtime-contract end-state check
(`check_design_room_runtime_contract.py`), which requires a non-empty `traceability`
list (requirement_id -> source -> design_ref -> selector -> proof). So before
`python3 gtm/scripts/design_room_run.py advance <project> convergence-lead-last`,
record it through the runner's single-writer chain:
`python3 gtm/scripts/design_room_run.py record-traceability <project> --json <path|->`.
A run that reaches convergence without recorded traceability is refused — record it
first, never after (the field is frozen once the gate clears).

## Grounded mode (Claude assembles, the founder decides)

This is the core rule, enforced by a family of provenance checkers in the gtm repo.
Every design decision carries a trailing `source:` of exactly one of three shapes
(grammar in `gtm/scripts/provenance_source.py`): `grounding/<file>#<anchor>` (a real
reference teardown), `fork:<id>` (a founder-resolved choice), or `generated:<asset>`
(an approved asset under `build/art/` from nano_banana_gen.py / veo_gen.py). A
"source" that is none of these resolves to the agent's taste — forbidden.

1. **No originated tokens.** Every color/font/spacing/radius/motion token in
   `design.md` carries a `source:`. Claude may not invent a token. If grounding
   lacks a needed token, that is a fork for the founder, not a gap Claude fills.
   (`check_token_provenance.py`)
2. **No originated copy.** Every headline/body/identity line lives under `## Copy`
   in `design.md` with a `source:` tracing to the founder's words or grounding.
   Claude assembles and arranges; it does not write the positioning.
   (`check_copy_provenance.py`)
3. **No originated composition.** Every `## Layout` line (hero structure, section
   order, focal point, responsive intent) carries a `source:`. Claude may not invent
   the page's gestalt at build time. (`check_layout_provenance.py`)
4. **No originated concepts.** Every concept under `## Concepts` in `forks.md`
   carries a `source:`. A concept the agent invented from nothing is origination
   dressed as a fork. (`check_fork_provenance.py`)
5. **No self-graded build.** The build's design-decisions are EXTRACTED from the
   rendered HTML (`extract_design_decisions.py`) and bound to it
   (`check_decisions_provenance.py`) — never authored by the agent. The agent may
   not describe its own page; the DOM does.
6. **No process self-routing.** The current workflow is read from
   `gtm/design-room/current-contract.json`, not inferred from older PRDs. A run's
   selected sources, founder fork, subject selector, and rendered proof live in
   `run-state.json`, checked by `check_design_room_runtime_contract.py`.
7. **Every open choice is a forced-choice fork.** When the evidence does not
   decide, the lens emits A-vs-B and the founder picks. Claude never resolves its
   own fork.
8. **Synthesis assembles, never originates.** Phase 3 collects and arranges. It
   adds no new decision.
9. **No resurrected personas.** The v1 persona theater is dead. A project's
   `design-room/personas/` dir must not exist. (`check_no_personas.py`)

## Modernity (no per-run web search)

The per-run workflow does **zero web research**. What is "modern" comes from the
**weekly modernity pulse** (`design_room_pulse.py` in the gtm repo): a scheduled
job researches new repos/trends, writes a dated snapshot, and promotes/rejects
into `references/build-palette.md`, which carries a last-refreshed date. At run
time the room reads the canon and the palette — it does not search.

## Critical Rules

1. **Layer, never replace.** New founder inputs ADD to the brief. Keep all context.
2. **Cite, ground, or fork.** Every lens output is a cited principle, a grounding
   fact-check, or a forced-choice fork. Never an unsourced opinion.
3. **Claude assembles, the founder decides.** No originated tokens, no originated
   copy, no self-resolved forks.
4. **No green state — done is the founder's eye + the market, only.** The Phase 6
   checks never say "done", "good", or "passing"; any visible pass-floor gets
   satisficed to (the founder, 2026-06-25). They are diagnostics + regression alarms
   (`check_technique_parity.py` BLOCKS when the build dropped a declared technique;
   `check_design_diff.py` emits the design gap-list and never a verdict). Aim at the
   reference, not the checks. Never report a page as good — report the gap list + what
   it pulled, and hand it to the founder.
5. **L3 — the tool REFUSES to score resonance.** Whether the page is ownable by THIS
   brand and resonant with THIS buyer (canon `reflective-design`,
   `quality-without-a-name`) is NOT scored. The tool emits the L1/L2 gap-list,
   surfaces the L3 question, and hands the page to the founder's eye and a real
   buyer. A tool that scores resonance is the failure mode. **The founder's eye + the
   market are the only ceiling.**
6. **Decisions compound — append-only, dated, never rewritten.** Every decision is
   appended to `decisions.md` with its date, why (lens/fork/cited principle), and what
   it supersedes. Never edit or delete a prior entry; supersede it. This is the record
   that carries across sessions.

## File Structure

```
<project>/design-room/
  founders-brief.md     -- Canonical. All founder inputs layered.
  decisions.md          -- Compounding canonical record: append-only, dated, hash-chained decisions
  grounding/            -- Reference-site teardowns + candidate tokens (every token starts here)
  grounding/steal-manifest.json -- Declared techniques + fingerprints; the Phase 6 parity alarm reads this
  review/               -- One file per lens (cited / grounded / fork output)
  forks.md              -- The assembled fork sheet the founder resolves
  design.md             -- Grounded spec (tokens + source per token, agent-readable)
  build/                -- The built page + gate-report.md
```

## References

- [references/lens definitions + the attention canon](references/attention-canon.md)
- [references/art-direction-canon.md](references/art-direction-canon.md) — the LEAD lens's visual-design canon (L1 craft / L2 concept / L3 truth)
- [references/grounding.md](references/grounding.md) — Phase 2.0 teardown -> tokens + design-decisions
- [references/build-palette.md](references/build-palette.md) — vetted repo menu (weekly-refreshed)
- [references/design-md-template.md](references/design-md-template.md) — the grounded spec format
- [references/decisions-template.md](references/decisions-template.md) — the compounding decision ledger format
- [references/convergence-gate.md](references/convergence-gate.md) — the ship gate
