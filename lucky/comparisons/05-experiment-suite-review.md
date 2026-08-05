# Review: The Six-Experiment Suite Against Lucky v3

Six experiment files from a parallel investigation of the Eτ/LPA2v library
were reviewed in full (1,614 lines): `critique_suite.py`,
`experiment1_conflicting_data.py`, `experiment2_fuzzy_boundaries.py`,
`paradox_suite.py`, `blackhole_paraconsistent.py`,
`confabulation_cartography.py`. This document maps every finding onto
Lucky's current state (v3) and records what the evidence forces us to
adjust. Three piles: already answered, genuinely shared gaps, and
horizon confessions we owe.

---

## 1. Findings Lucky already answers

| Finding | Where it appears | Lucky's answer |
|---|---|---|
| Conflict must be surfaced, not averaged away | exp1 (naive average is conflict-blind; dct exposes it) | Gc/Gct pair since v0; the two-axis verdict is the kernel's spine |
| Abstention beats forced classification at fuzzy boundaries | exp2 (accuracy/coverage sweep over FtC) | blur region + Carving thresholds (v3); abstention feeds pressure meters, which feed genesis — abstention is not a dead end, it is data |
| Contradiction must not propagate to unrelated claims | paradox 2 (Russell + non-explosion test) | locality: each `Ev` carries its own annotations; no global entailment exists to explode through |
| Over-determined (⊤) vs under-determined (⊥) are different pathologies | black hole C (the singularity is theory-silence, not contradiction) | `inconsistent` vs `paracomplete` regions, distinct since v0; the experiment is a beautiful external confirmation that the distinction pays rent |
| Escape routes from a joint inconsistency have measurable costs | black hole B (three firewall resolutions, each "burns" different evidence) | priced collapse + Residue Ledger; each resolution is a collapse whose discarded weight is filed |
| Exit-stage collapse merging conflict with ignorance is a defect | exp1 uses `decision_output` uncritically; critique G exposes it | already refused in v3's negative birth record ("what was NOT absorbed") |
| Pure introspection cannot ground self-assessment | confab C (bistable fixed point: stores the initial condition, not any fact; external anchors unify it) | dialogical adoption (v2): the kernel drafts responders but adoption requires outside selection. The experiment supplies the *mechanism* for why this choice was structurally necessary, not merely cautious. Recorded as a strengthened birth note. |
| A self-summary is itself a lossy act | confab A (ACTUAL vs REPORTED annotations, counterfeit distance) | `digest()` files itself in the ledger as a collapse with an omissions receipt (v2). Partial: see §3 for what we still owe. |

One more quiet confirmation: our v1 combiners (`max`, `noisy_or`, and the
min/max lattice operations) are associative and commutative, so critique E
(fusion non-associativity — three sources, different parenthesizations,
different verdicts, no canonical tree) does not bite the current kernel.
Where tree structure *does* matter in Lucky — correlation groups in the
SourceGraph, nested bundles in composition — the structure is declared and
carried as provenance rather than left implicit in evaluation order. This
was luck as much as design; it is now registered as a constraint: **any
future combiner must either be associative or carry its tree.**

---

## 2. Genuinely shared gaps — what v4 adjusts

### 2.1 The encoding degree of freedom (critique A, and everywhere)

Critique A showed five defensible encodings of the same Berkeley data
yielding materially different verdicts: the world→(μ,λ) mapping lives
*outside* the logic, unregistered. What makes this the deepest finding is
that it silently recurs inside the other experiments themselves:

- exp2 anchors its fuzzy ramps on class means — a choice, undeclared as one
- paradox 3 (sorites) picks a logistic with midpoint 100 and slope 3.0
- paradox 4 (Simpson's) scales λ by "20% max plausible gap" — an invented constant
- black hole A picks background weights w_qm=0.95, w_sc=0.85 from judgment

Lucky is equally guilty: a `Testimony.weight` arrives as a bare float. How
the world became that number is exactly as unregistered as Eτ's inputs.

**Adjustment (v4):** testimony gains a declared *encoding* — a statement of
how the number was produced. Undeclared encodings are not rejected (that
would just push the laundering upstream); they are *marked*, counted, and
surfaced in the trail. The verdict of a case file built on undeclared
encodings says so. GIGO is not solved — it cannot be solved from inside —
but it is no longer laundered. The gap between world and number is now a
place the kernel can point at.

### 2.2 Weight-of-evidence collapse (critique F)

(0.5, 0.5) from one study against one study is indistinguishable from
(0.5, 0.5) from five thousand against five thousand. The lattice position
carries the *balance* of evidence but not its *volume* (Keynes's "weight"
is unstatable). Lucky's trail technically retains every testimony, but
nothing surfaces the count — the verdict presents thin and thick evidence
identically.

**Adjustment (v4):** `Ev` exposes `mass` — the count of testimonies in the
trail — and the repr shows it. A balanced verdict at mass 2 and a balanced
verdict at mass 10,000 now *look different*. Registered honestly: mass is
a count, not a measure; it does not compare across combination modes, and
it says nothing about the quality of the testimonies it counts. It is the
cheapest quantity that stops the collapse from being silent.

### 2.3 Cycle blindness (critique C, exposed by paradox_suite's own Liar)

The two files disagree with each other, and the disagreement is the finding.
`paradox_suite.py` claims the Liar is "contained": its evidential iteration
converges to the lattice center. But the convergence is manufactured by an
**unconfessed damping parameter** (smoothing weight 0.5 applied at each
step). `critique_suite.py` runs the undamped revenge version — a sentence
about its own lattice position — and finds *no fixed point at all*: a
permanent 2-cycle (1,0)↔(0,1), with the center escape hatch closed.

The library has no way to *return a cycle as a result*. Neither does Lucky.
A self-referential process that settles into an orbit is currently either
forced to converge (by hidden damping) or fails to terminate.

**Adjustment (v4):** `iterate()` — run a self-referential update watching
for both fixed points and orbits. A fixed point returns `Settled` (carrying
the steps taken and any damping used, *confessed*). An orbit returns
`Cycle` — period, the orbit itself, first-class and final. The 2-cycle IS
the answer to the revenge Liar; a kernel that never prematurely collapses
should be able to say "this question's answer is an oscillation" and stop
there with a clean conscience. Damping remains available but becomes a
registered parameter that appears in the result: convergence claims carry
the damping that produced them.

### 2.4 Index quarantine (black hole D + confab D — the structural rhyme)

The most interesting *new* structure in the suite. Two experiments from
unrelated domains find the same shape:

- **Complementarity:** Alice's frame and Bob's frame are each fully
  consistent; only the forbidden "superobserver" fusion of both produces
  near-maximal contradiction — and physics itself renders that fusion
  operationally impossible.
- **Polysemy:** "bank" carries strong evidence for incompatible meanings;
  the lexicon is a warehouse of quarantined ⊤-states, disambiguated per
  utterance by context-indexing. A pun is a momentary indexing failure.

The rhyme is exact: *contradiction that exists only under index-collapsing
fusion is not a pathology of the claims — it is a fact about the fusion.*
Neither Eτ nor Lucky v3 can say this. Our SourceGraph handles correlated
sources, but frames are not correlation: two frames can be individually
impeccable, uncorrelated, and still illegitimate to merge.

**Adjustment (v4):** evidence may carry a *frame*. Fusing across frames is
a priced act — it files in the ledger like any collapse, and the fused
result's trail is permanently marked as index-collapsed, so any
contradiction it exhibits carries the receipt of the fusion that made it.
Where frames have been *declared* non-fusable, the fusion returns an
informational anomaly pointing at the superobserver problem instead of a
result. Contradiction within a frame remains what it always was; the new
vocabulary distinguishes it from contradiction manufactured at the merge.

---

## 3. Horizon confessions we owe (registered in v4, not built)

**The classical substrate (critique G).** Their 12-region classifier is a
cascade of bivalent comparisons — "paraconsistency as a managed dialect
inside a classical host." Every word of this applies to Lucky: our kernel
is Python; every `if` in `verdict3` is bivalent; the blur region is
delimited by crisp float comparisons. We do not escape this and will not
pretend to. Registered on the HORIZON: the kernel *describes* graded,
conflicted, unsettled states in a substrate that is none of those things.
The description layer and the substrate layer must not be confused, and
the kernel's honesty lives entirely at the description layer.

**Conditionals (critique D, Curry).** Curry's paradox trivializes systems
with modus ponens and contraction *without using negation at all* — so
paraconsistency (a negation therapy) cannot help. Eτ escapes only by being
unable to state conditionals in the first place: annotations attach to
atoms. Lucky is in the identical position: we have combination operations,
not an implication. This is registered as a horizon boundary, not quietly
enjoyed as an accident: if Lucky ever grows a conditional, contraction is
the hidden decision that must be priced at birth.

**Actual vs reported states (confab A).** The counterfeit-distance
construction — an evidence-starved state wearing a well-supported state's
costume, invisible to any scalar projection — is a precise description of
what `digest()` already guards against at the register level (omissions
receipt) but which applies to *every* surface the kernel presents. The
general principle is registered: any exit surface is a reported state; the
counterfeit distance is measurable only where the actual state is retained.
Lucky's trails are that retention. Discarding trails is therefore not a
compression decision but an epistemic one.

**Training pressure as a vector field (confab B).** External reward on
outputs advects mass out of honest-ignorance toward confident assertion
wherever no correctness signal reaches. For Lucky the lesson is about the
*selection pressure on the kernel's own registers*: any future tuning of
Carving thresholds by outcome feedback needs its objective declared,
because an objective that penalizes blur verdicts will manufacture
certainty exactly the way the simulation shows. Registered alongside the
Carving choice.

---

## 4. What was deliberately NOT taken

- **Convergence-by-damping as paradox "containment"** (paradox 1): the
  center fixed point is an artifact of the smoothing weight. v4's
  `iterate()` inverts the move — damping is allowed but confessed, and
  orbits are results, not failures.
- **Time-parameterized trajectory plotting** (black hole A/C): expressible
  today as repeated calls; a trajectory type would be vocabulary without
  new distinctions. Reconsider if trajectories recur in pressure meters.
- **Per-domain encoding recipes** (all files): each experiment hand-crafts
  its world→(μ,λ) mapping. Absorbing any one recipe would bless it; the
  v4 move is to make the *recipe slot* visible, not to standardize recipes.

---

## 5. Summary of forced adjustments

| # | Source finding | v4 structure |
|---|---|---|
| 1 | Encoding degree of freedom (critique A + recurrences) | Declared encodings on testimony; undeclared marked and counted, never repaired |
| 2 | Weight-of-evidence collapse (critique F) | `Ev.mass` surfaced; balance and volume no longer conflated |
| 3 | No fixed point / manufactured convergence (critique C vs paradox 1) | `iterate()` returning `Settled` (damping confessed) or `Cycle` (orbit as first-class result) |
| 4 | Index quarantine (black hole D + confab D) | Frames on evidence; cross-frame fusion priced and marked; declared-illegitimate fusion returns anomaly |
| 5 | Classical substrate, Curry, reported-state, training-pressure | HORIZON/CHOICES records — pointings, not features |
