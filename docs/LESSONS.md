# The lessons this chain is built on

Each stage of the chain exists because a round without it went wrong. The gate's docstrings
name these by title; this is where the titles resolve.

## A defect-absence gate is a floor, not a finish line

An automated check that verifies the ABSENCE of known bad patterns cannot certify the PRESENCE
of quality. Treating its pass as "done" quietly redefines the ceiling as the floor. Four moves
guard against it:

1. **Separate floor-checks from bar-checks.** A gate that detects known defects (a missing
   element, a banned pattern, a malformed structure) answers "is this not broken?", never "is
   this good?". Keep the bar decision as an explicit, separate step owned by a human eye or a
   distinct rubric. In this chain: `design-standard-check.py` and the tripwire are floors; the
   craft manifest, the critique and the readers are the bar.
2. **Make grounding operative, not decorative.** A rule that every decision cite a source proves
   the source exists; it does not force the source's best ideas into the work. Convert what the
   research found into build REQUIREMENTS before building. In this chain: the narrative's
   "what applies to us" answer becomes craft-manifest techniques, and
   `check_technique_parity.py` blocks a declared technique the page does not carry.
3. **Resolve decisions at execution level, not concept level.** "Do approach X" names what,
   not how well. Add a tier so a premium realization and a bare-minimum one are not both
   compliant. In this chain: `craft.tier` is `craft`, and a wireframe is non-compliant.
4. **When several options satisfy the constraints, name the required one.** Effort flows to the
   easiest compliant path. Encode the strong version as the requirement.

Measured origin: a round passed every floor while shipping three wireframes with zero imagery,
zero motion and zero depth. Every check was green. Nothing was good.

## A bland page has no defects

Every mechanical check finds defects, and a bland page has none. A deliberately bland control
page cleared the standard check, the tripwire and the browser detector in one run. Seven rounds
drifted the same way while every gate stayed green. That is why `design-gap-check.py` exists:
it measures DISTANCE from the exemplars on axes derived from their captures, so taste cannot set
the floors, and only on axes where the canon and the measurement agree.

## A brief written from memory is how the generic layout returns

Two rounds of first screens ignored the canon because the brief was assembled from what the
builder remembered. So the brief must quote the owner anchors verbatim, read live, and a brief
that is a byte-copy of an earlier round's brief is a round that never read the owners. Writing it
is the act of reading.

## Three sealed directions, all wrong

Nothing was skipped: three directions, fully specced, measured, critiqued and sealed. Every
brief was assembled from constraints and none said what the page was trying to BE. The gate
could see the shape of the work and not that it was aimed at nothing. That is why the vision
stage comes before the brief, in the founder's own quoted words, and why a brief must quote
one of them.

## A weakness the critique named and the round shipped anyway

Across three sealed rounds, 11 findings were marked weak in the critique, 0 required an answer,
and two were the exact defects the founder then caught. So every `WEAK[tag]` needs a
disposition line: fixed, deferred or carried, with why.

## A verdict in prose is a verdict nothing reads

Readers were asked "would you keep reading, or leave? Why?" Three readers said leave, in prose
that nothing parsed, and the round sealed. So two forced-choice questions (STAY or LEAVE; which
label is being sold) go before the control question, and the seal reads the answers.

## A check that skipped is not a pass

A round sealed with the tripwire's FAIL written in its checks directory, because the only rule
was that the directory be non-empty. Checks are a closed registry now: the seal runs each one
itself, records the exit code, and refuses a skip as firmly as a fail.

## What is measured is what is sealed

The seal measures a snapshot of the round and compares every file at the end, because a file
edited between the measurement and the seal was caught by neither read. Inputs OUTSIDE the round
(owners, the narrative, the persona) are held the same way.
