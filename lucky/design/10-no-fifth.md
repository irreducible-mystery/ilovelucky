# 10 — There is no fifth. There is no floor. (kernel runs, one consumer program)

Every claim below is a run, per the standing rule. Three runs this turn.
No kernel changes. No v8. No new instruments.

## Run 1: the tetralemma, checked against the kernel

`verdict3` was run over the lattice twice: once with the default carving
(t = 0.55 everywhere) and once with `Carving(0, 0, 0, 0)` — the floor
removed entirely.

| point        | with floor (0.55) | floor removed |
|--------------|-------------------|---------------|
| (0.90, 0.10) | true              | true          |
| (0.10, 0.90) | false             | false         |
| (0.90, 0.90) | inconsistent      | inconsistent  |
| (0.10, 0.10) | paracomplete      | paracomplete  |
| (0.60, 0.50) | **blur**          | true          |
| (0.50, 0.50) | **blur**          | true          |

With the floor removed there are exactly **four** regions: p, not-p,
both, neither. Blur disappears. So the kernel itself agrees: **blur is
not a fifth position**. Blur is the drawn floor made visible — it exists
only because a threshold was carved, and every blur verdict is a
confession of that carving. The four corners are the complete core.
There is no fifth, and the 300 real lines already knew it.

Corollary worth stating plainly: the 0.55 threshold does not add logical
content. It adds a *hesitation band* — a region whose only meaning is
"the carver declines to commit yet." That is exactly what an arbitrary
floor should be: visible, priced, and removable without breaking the
four corners.

## Run 2: one floor drawn and FORGOTTEN, found live

At dead center (0.5, 0.5) with the zero carving, all four edge distances
tie at 0.0 — and `verdict3` returns **"true."** Why: the winner is
selected by `max()` over a dict, and Python's `max` breaks ties by
**insertion order**. "true" is declared first in the source, so perfect
four-way symmetry silently resolves to p.

A grep of `CHOICES` after importing lucky3: **no registered choice
mentions this tie-break.** Fourteen choices registered; the declaration
order of four dictionary keys is not among them, yet it decides the
verdict at every exact tie.

This is Kelly's sentence, exhibited: *the problem is not that we define
arbitrary floors; the problem is when we forget we have arbitrarily
drawn them.* The kernel has one working remembering-mechanism — every
Verdict3 carries its `carving` and flags non-default ones as
`[tilted carving]`, so the threshold travels with the verdict to the
reader. The tie-break has no such passenger seat. One floor remembered,
one forgotten, in the same twenty lines. Registered here as a finding,
not patched (rule: no build to answer a finding this turn; if it is
ever fixed, the fix is one CHOICES entry plus a tie mark in the verdict,
not an instrument).

## Run 3: what would make one real program want the 300 lines

`programs/deploy_gate.py` — a CI deploy gate, one of the most common
programs in the world, written twice: once over `bool` as it is actually
written everywhere (`if all(results.values()): deploy`), once consuming
the kernel (suites → Testimony, region → action).

| scenario                       | bool gate  | kernel gate                    |
|--------------------------------|------------|--------------------------------|
| clean pass                     | DEPLOY     | DEPLOY                         |
| suites disagree                | BLOCK      | RERUN / QUARANTINE FLAKY SUITES|
| **CI outage: no results**      | **DEPLOY** | HOLD + CHECK CI INFRA          |
| everything fails               | BLOCK      | BLOCK + FILE BUG               |

Two divergences, both real:

1. **Row 3 is a famous bug class, not a contrived one.** `all([]) is
   True` — Python's vacuous-truth convention. On a CI outage the boolean
   gate deploys untested code. The fourth corner (neither p nor not-p)
   had no place in `bool`, so the language silently assigned it to p.
   That is a floor drawn by the language designers, so long ago and so
   thoroughly forgotten that it is invisible in the source of every gate
   that has this bug. The kernel gate cannot have it: paracomplete is a
   place to stand.

2. **Row 2 routes a different human.** bool's BLOCK says "the code is
   bad." The kernel's inconsistent says "the *evidence* is bad — the
   suites disagree; investigate the tests." Anyone who has watched a
   team burn a day debugging healthy code under a flaky test knows these
   are different actions with different costs.

### The answer, in one sentence

A real program wants the 300 lines exactly when **its action space is
finer than its condition type** — when conflict, absence, and fragile
agreement each demand a different next action, and `bool` collapses all
three into whichever corner the forgotten floor assigns them to.

And the honest converse: most programs' action spaces really are binary
(`if file exists, read it`), and those programs are **correct not to
want this**. The 300 lines are not for programs that decide; they are
for programs that *triage*. Deploy gates, alert routers, medical intake,
sensor fusion, moderation queues — anywhere the wrong collapse routes
the wrong human.

## What this turn did not do

No kernel v8. No rot test 4. No new registers. One consumer program,
two kernel probes, this note. The tie-break finding waits as a finding.
