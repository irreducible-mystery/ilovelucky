# Field Notes from the First Run (v0)

Breakage and surprise are the most valuable information. The first execution
of lucky0 produced several — recorded here, not patched away.

## 1. `refute` on a well-evidenced claim yields INCONSISTENT — and that's right

`refute(e, witness)` on e=(0.80, 0.30) produced (0.80, 0.90) → inconsistent.
First instinct: bug — shouldn't refutation make things *false*?
No. The refutation attached contrary evidence **without erasing the favorable
file**. If strong evidence-for exists and a strong refutation arrives, the
honest state IS inconsistency — the sources are now in real conflict, and the
right response is *audit*, not quiet flip. A boolean `not` would have
overwritten the history; the kernel preserved the collision. The "bug"
was the boolean intuition, surviving in the reader.

## 2. Gc=+0.50 landed in blur (t=0.55) — the threshold is doing violence, visibly

e=(0.80, 0.30) reads as "lean true, thin margin" to a human, but fell into
blur by 0.05. The para-analyzer's threshold is a hard carving of a continuous
square, and the demo tripped over it immediately. This is the geometry
confessing its own arbitrariness at first contact — precisely the pressure
Layer 6 is designed to meter. Note for v1: verdict could return *distance
from region boundaries* along with the region — outputs carrying their own
sensitivity (essay 04's prescription), so a verdict that flips under a 0.05
perturbation is distinguishable from one robust to 0.4.

## 3. The residue receipt exposed floating-point residue — a confession within a confession

`discarded: [('blur', 0.19999999999999996)]`. The ledger, built to record
what collapse discards, incidentally recorded that our substrate (IEEE 754)
does its own silent collapsing. Fitting: every layer rests on a lower carving
with its own unconfessed choices. Enter in CHOICES eventually: "numeric
substrate: IEEE doubles; foreclosed: rationals, intervals; consequence:
the ledger's own receipts are approximate."

## 4. The unparsed self-question path is genesis pressure on the self-model

`ask_self` returns an Anomaly for questions outside its tiny vocabulary — and
that anomaly is marked as blur pressure *on the self-model itself*. Layer 6
metering applied to Layer 7: the self-description vocabulary should grow from
the record of questions it failed to parse. Not implemented in v0; the design
implies it. This is the most interesting corridor found so far: **the
kernel's self-model evolving from the necessity-record of its own confusions.**

## 5. What v0 cannot yet say (its local horizon, distinct from the theorem-forced one)

- **Source dependence**: two testimonies from correlated sources double-count.
  The evidence algebra assumes independence and only confesses it.
- **Effects in branches**: `explore` runs all branches; v0 relies on
  discipline, not enforcement, to keep them coexistence-safe. Debt: an effect
  system, or bundle-local worlds.
- **Identity of confusions**: Necessity counts blur *per predicate name* —
  the crudest possible identity for "the same confusion." Essay 01's
  structured identity is the eventual answer: two blurs are "the same" via a
  *correspondence*, not via a string match.
- **Reading load**: CHOICES + HORIZON + LEDGER + trails is already a lot of
  confession for sixty lines of demo. The hermeneutic burden (essay 04) is
  real and unsolved: honesty that nobody can read is a new kind of silence.
