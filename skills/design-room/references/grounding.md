# Grounding — teardown reference sites into real tokens (Phase 2.0)

Runs BEFORE the lens review. The point: the lenses weigh REAL designs and REAL
tokens, not imagined ones, and every token the build uses originates here — not
from Claude. This is the gap every competing design skill has (generation-time
guessing with no visual grounding). Fix it at the front.

## Inputs
- Reference sites the founder loves (URLs). Ask for 2-4 if none given.
- Optional: a Figma file (if the founder has one).

## The move

### 1. Fingerprint each reference site (stack + motion)
Use the installed **stack-recon** skill (or `gtm/scripts` teardown if present) to
fingerprint each reference URL:
- Network libs + JS globals (GSAP? Lenis? Three.js? Rive?)
- DOM structure of the hero
- Fonts (foundry vs system)
- The one signature motion moment

Write each teardown to `grounding/<site-slug>-teardown.md`. Steal technique, never
pixels.

### 2. Extract taste into tokens
For each reference, pull concrete tokens + the WHY behind them:
- Color palette (hex), type scale, spacing rhythm, radius, shadow language, motion
  timing/easing.
- The opinionated trade-off each choice makes (e.g. "tight tracking + heavy weight
  = authority over friendliness").

If a Figma file exists, use the **Figma MCP** (figma/mcp-server-guide) to pull real
frames/tokens/components instead of eyeballing.

Write to `grounding/tokens.md` — the candidate token set the lenses weigh and the
founder's forks resolve.

### 2b. Emit the steal-manifest (binds the teardown to the build)
Grounding a technique in prose is decorative — it dies in the teardown unless the
build is forced to reproduce it. So the teardown ALSO emits
`grounding/steal-manifest.json`: one entry per technique the build will steal, each
with a checkable fingerprint:
```json
{ "reference": "<site>",
  "techniques": [
    { "id": "splittext-headline", "technique": "GSAP SplitText kinetic headline",
      "role": "hero h1", "import": ["SplitText"], "applied": ["SplitText\\("] }
  ] }
```
`import` = how the technique loads; `applied` = evidence it is used on the
role-equivalent element. Phase 6's `check_technique_parity.py` reads this and BLOCKS
if the build dropped any declared technique. A teardown that says "steal X" without
a manifest entry for X has not actually bound the build — that is the failure mode
this exists to prevent.

### 2c. Emit the design-decisions teardown (binds the ART DIRECTION, not just the stack)
The steal-manifest binds the STACK (libs + motion). It says nothing about the
reference's DESIGN DECISIONS — the hero subject, the composition, the art-direction
approach. That is exactly the gap the rebuild closes: we fingerprinted the stack and
reproduced it while the art direction stayed absent (scar
`design-room-blind-to-art-direction`). So the teardown ALSO emits
`grounding/design-decisions.json`: the reference's design decisions as checkable
facts, which the **art-direction LEAD lens** reads to set the bar and which Phase 6's
`check_design_diff.py` diffs the build against.

```json
{
  "subject": "<reference site or 'build'>",
	  "design_decisions": {
	    "hero_subject": "what the hero is OF / ABOUT — the figure the eye locks onto (e.g. 'a rendered 3D security console'; 'an illustrated attack-path map'). Empty string = no subject (a gap).",
	    "composition": "the focal point + hierarchy (e.g. 'single off-center focal hero, asymmetric 60/40 split, one strong diagonal'). Empty string = an uncomposed equal-weight stack (a gap).",
	    "art_direction_approach": "one of: type | illustration | photo | 3d | character",
	    "bespoke_vs_default": "one of: bespoke | mixed | default",
	    "reference_motion_required": true,
	    "subject_behavior": "what the subject does over time or scroll, stated as observable behavior",
	    "motion_role": "one of: protagonist | ambient | none",
	    "motion_storyboard": ["frame 0: subject state", "frame 2s: subject state", "scroll: subject state"]
	  }
	}
	```

These keys are fixed (the LEAD lens and `check_design_diff.py` rely on them):
`hero_subject`, `composition`, `art_direction_approach`, `bespoke_vs_default`. An
empty `hero_subject` or `composition`, an `art_direction_approach` that is absent, or
a `bespoke_vs_default` of `default` is a GAP the LEAD lens raises — never a verdict.
A `reference_motion_required` value of true means the build must later clear
`check_motion_reference_parity.py` against `run-state.json`. A generated still image
is a style frame unless the reference itself is static or the founder explicitly
resolved it as the final static subject.
A reference design-decisions sample lives at
`fixtures/grounded/design-decisions.sample.json`.

### 3. Hand grounding to the lenses
Every cited/grounded lens reads `grounding/tokens.md` + the teardowns before it
runs. The **art-direction LEAD lens** additionally reads
`grounding/design-decisions.json` (the design teardown) to set the bar. Each token a
lens references must trace back to here. The job is "validate / push / refine these
real tokens" — never "invent from scratch."

## Output
```
grounding/
  <site>-teardown.md       -- stack + motion fingerprint per reference
  tokens.md                -- candidate tokens + rationale the lenses weigh
  steal-manifest.json      -- declared STACK techniques (Phase 6 parity alarm reads this)
  design-decisions.json    -- the reference's DESIGN DECISIONS (the LEAD lens bar; check_design_diff.py reads this)
```

## Rule
Grounding is candidate input, not a decision. The lenses still weigh in and the
founder still decides. Layer, never replace.
