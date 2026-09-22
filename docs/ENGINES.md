# Engines: the design tools a round calls, and where to get them

The chain does not design. Its build step (step 4 of a round) calls design skills, which it
calls engines: it opens the round, the builder invokes the skill, and `design-engine-door.py`
records the run in `engines.jsonl` so the craft manifest can credit it. None of the engines
ship in this repo except `design-room`. Which ones you need depends on the lane of the round.

Run the doctor before the first round. It says what is installed and what is not:

```
/design-chain:doctor
```

or, from a checkout, `python3 scripts/doctor.py`.

## The minimum

A site round needs ONE site-lane engine. Two are free and enough to start:

- `design-room`, in this repo. Multi-lens design review with an art-direction lead. Runs on
  its own; nothing to install.
- `frontend-design`, Anthropic's. `/plugin marketplace add anthropics/claude-code`, then
  `/plugin install frontend-design@claude-code-plugins`.

Everything else is optional and adds range, not permission.

## All of them

| Engine | Lane | What it is for | Where it comes from |
|---|---|---|---|
| design-room | site | the design review lenses and the art-direction bar | this repo, `skills/design-room` |
| frontend-design | site | building a distinctive front end instead of the default | marketplace `anthropics/claude-code`, plugin `frontend-design` |
| ui-ux-pro-max | site | styles, palettes, font pairs, UX guidelines by lookup | marketplace `assafkip/kipi-system`, plugin `kipi-design` |
| scroll-craft | site | scroll-driven motion on a marketing page | marketplace `nateherkai/scroll-craft`, plugin `nateherk-design` |
| web-artifacts-builder | site | building a self-contained web artifact | marketplace `anthropics/skills`, plugin `anthropic-agent-skills` |
| design | brand | logo, identity system, banners, tokens | marketplace `assafkip/kipi-system`, plugin `kipi-design` |
| brand | brand | brand voice and visual identity | marketplace `assafkip/kipi-system`, plugin `kipi-design` |
| canvas-design | brand | visual design on a canvas | marketplace `anthropics/skills`, plugin `anthropic-agent-skills` |
| theme-factory | brand | a theme from tokens | marketplace `anthropics/skills`, plugin `anthropic-agent-skills` |
| algorithmic-art | brand | generative visual assets | marketplace `anthropics/skills`, plugin `anthropic-agent-skills` |
| deck-ai | deck | a slide deck | marketplace `assafkip/kipi-system`, plugin `kipi-core` |
| slideshow | deck | a slideshow video | a personal skill of the original author; not needed for a site round |
| hyperframes, hyperframes-core, hyperframes-animation, hyperframes-creative, hyperframes-keyframes, hyperframes-media | motion | video and motion graphics rendered from HTML | the hyperframes project: `npx hyperframes skills` installs them as personal skills |
| motion-graphics, explainer-visuals, faceless-explainer, general-video, website-to-video, product-launch-video, music-to-video, pr-to-video, remotion-best-practices | motion | the hyperframes workflows for specific kinds of video | same |

The registry is `scripts/design-engines.json`, and each entry carries the same `source`
line. Editing that file is how you add an engine of your own: `skill`, `lane`, `stage`,
`source`. The door reads it live.

## What the door does with them

- A listed engine called with no open round is refused, and the refusal names
  `/design-chain:round`. `DESIGN_CHAIN_ALLOW=1` in your own shell is the override for work
  that is not a design round.
- A listed engine called inside a round is recorded in the round's `engines.jsonl`. A craft
  manifest technique that credits an `engine` needs that record, or the seal refuses it.
- An engine that is not installed is simply never called. The chain will brief, measure and
  seal without it; the build step is where you find out you have nothing to build with, which
  is why the doctor runs first.

## Runtime, separate from engines

Three things every round needs regardless of engines, also checked by the doctor:

- Python with `playwright` and chromium (`pip install playwright Pillow && playwright install chromium`)
- Node 18 or newer, for the vendored anti-pattern detector
- the `claude` CLI on PATH, for the reader gate
