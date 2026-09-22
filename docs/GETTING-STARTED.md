# Getting started

Ten minutes to a project the chain accepts. An hour to a first sealed round.

## What you need installed

- Python 3.11 or newer, with `pip install -r requirements.txt` (playwright and Pillow), then
  `playwright install chromium`. The measurements run a real browser.
- Node 18 or newer. The anti-pattern detector under `vendor/impeccable` is JavaScript.
- Claude Code, with this repo installed as a plugin (the README has the one-line install). The
  reader gate runs fresh model readers through `claude -p`.

Check all three at once:

```bash
python3 -c "import playwright, PIL; print('python ok')" && node --version && claude --version
```

## The seven questions

Open Claude Code in the folder that holds your site (or an empty folder for it) and run
`/design-chain:init`. It asks one question at a time and writes a file after each answer.
Every question shows an example answer; the examples below are the same ones.

**1. What is the product, in one line?**
Example: *Ledgerline, invoicing for freelance designers.*
Names the project.

**2. What is the page trying to BE? Three or more sentences, in your words, verbatim.**
Example: *They need to hit the site and immediately understand how I can help them.*
Not features, not constraints. What a visitor should understand and feel. These become dated
founder blocks in `design/VISION.md`, and every brief has to quote one of them word for word.
A round briefed without a vision is aimed at nothing; that is the failure this stage exists for.

**3. Who arrives? One paragraph.**
Example: *A freelance designer with six clients, invoicing from a spreadsheet at 11pm, who
just got paid late for the third time this quarter.*
The top of `design/owners/buyer.md`. This file is also the persona the reader gate role-plays.

**4. Three or more phrases the buyer actually said.**
Example: *I spend Sunday night chasing invoices instead of designing.*
From calls, tickets, reviews, posts. Their words, not yours. The first phrase becomes an anchor:
every brief must quote it verbatim, read live from the file. A phrase you invent is a phrase the
gate holds you to forever, so do not invent one.

**5. The one idea. One sentence the whole page repeats.**
Example: *Every invoice knows whether it has been paid, so you never have to ask.*
An owner with an anchor.

**6. What must it NOT look like? Each with a reason.**
Example: *A generic SaaS template: every competitor already looks like that.*
An owner with an anchor.

**7. Three to six sites you admire.**
Example: *https://stripe.com, https://linear.app, https://calendly.com.*
They are captured at two viewports and measured (type ramp, colours, imagery, motion, space,
button and nav shapes). The standard's floors are derived from them, so pick pages you would be
proud to sit beside. Open them before the next question.

**8. The narrative: what they share, what each does alone, what applies to you.**
Three answers. The third is turned into your first craft requirements, so be concrete: "the
product image in the first fold applies; the signature gradient does not."

**9. What might a stranger think this page is selling?** Two to five labels, the right one first.
Each model reader is made to pick one, and the seal reads the pick. A page that sells the wrong
thing fails here even when every other check is green.

**10. One signal colour, or blank.** It may mean one thing on the page and nothing else.

## What init writes

```
design-chain.json                 the config the gate reads
design/VISION.md                  your words, dated
design/owners/buyer.md            the buyer, their phrases, the reader persona
design/owners/the-idea.md         the one sentence
design/owners/not-this.md         the list with reasons
design/references/exemplars.json  the roster of sites (append-only)
design/references/NARRATIVE.md    your read of the group
design/exemplars/                 the captures a round must cite
design/specs/  design/rounds/     empty, for the chain
```

Then it checks what it wrote the way the gate reads it, and prints either "every input the
chain needs is in place" or a list of what is missing, each line naming the file.

## Then

`/design-chain:round`. One round: brief, three directions, craft manifest, build, measure, critique,
proof, checks, readers, seal. `A-ROUND.md` walks through it. When a step refuses,
`WHY-IT-REFUSES.md` has the message and the fix side by side.

## What it will not do

It will not tell you the design is good. Every gate here is a floor: it catches a wireframe, a
paraphrased brief, an uncited technique, a reader who would leave. A page can clear all of it
and still be wrong. The example under `example/consulting-site` is a real project's real inputs
and one sealed round; read its `VISION.md` to see what "in your own words" looks like when it
is not a form being filled.
