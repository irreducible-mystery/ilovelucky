# Lucky: Foundational Layers (v0)

## A language that points at its gaps

**Status:** founding design. Everything here is contingent and says so.
**Method:** each layer declares four things — what it *gives*, the *hidden
choices* it makes (surfaced, never silent), what it *cannot say* (and why),
and *where it breaks* (breakage is data, not failure).

---

## Reading the prose without freezing it

The originating direction (Kelly), de-prosed into kernel commitments:

| Pointing phrase | Kernel commitment |
|---|---|
| "conflicting perspectives... complementary" | evidence carries favorable and contrary degrees **independently**; perspectives interfere without overwriting each other |
| "they all have a gap... generative and consuming" | `Gap` is a first-class value: it absorbs operations (consuming) and can seed new distinctions (generative). It is never an error. |
| "no escape hatch but points instead" | nothing exits the semantics silently; every exit is reified as a Gap with context. There is no `unsafe`, no `unsafePerformIO`, no cut. There is only *pointing at what is outside*. |
| "not prematurely collapsing" | branching does not choose; it **explores all live regions** and returns a bundle. Collapse is a separate, explicit, priced act that records what it discarded (the Residue Ledger). |
| "states explicitly what it cannot state and cannot prove and why" | the **Horizon**: a runtime register of incapacity claims, each with its reason (theorem-forced or choice-forced), grown during execution |
| "errors as possibly informational" | anomalies are values carrying case files (origin, path, hints); they flow, accumulate context, and can be *read* |
| "where categorization blurs" | **blur** is a first-class verdict region, distinct from true/false/inconsistent/paracomplete; blur pressure is *metered* |
| "evolve from necessity" | repeated blur on the same predicate triggers a **genesis proposal**: the vocabulary itself is declared insufficient and a new distinction is seeded from the gap |
| "not superior to another, but still valid" | the **Confession** layer: the kernel's own axiomatic choices are recorded with their alternatives and consequences. Lucky knows it is one carving among many. |

The prose is insufficient; so is this table; so is the kernel. The insufficiency
is recorded (Layer 0) rather than hidden. That recording is the design.

---

## Layer −1 · The Gap (pre-linguistic substrate)

**Gives:** an acknowledgment, *inside* the language, that the language does not
exhaust what is. `Gap` is the reified outside — not null (absence of value),
not error (violation of expectation), not unknown (a truth value). It is the
remainder of every carving.

**Behavior:**
- *Consuming:* any operation touching a Gap yields a Gap with extended context.
  The Gap does not resolve; it accumulates the history of attempts on it.
- *Generative:* a Gap can `seed()` a new Distinction — fresh vocabulary whose
  birth record cites the gap that necessitated it. New words come *from*
  the unsayable, carrying their origin.

**Hidden choices (surfaced):** representing the unrepresentable at all is a
paradox we accept knowingly — `Gap` is a *pointer to* the outside, not the
outside. The map has a symbol for "off the map"; the symbol is still on the map.

**Cannot say:** what the gap contains. By construction. A Gap that could be
inspected would be a value, and the layer would have failed by succeeding.

**Breaks when:** users treat Gap as an error to be handled away, or as null.
The kernel resists: Gap has no `unwrap`, no default, no coercion to boolean.

---

## Layer 0 · Confession (choices and horizon)

**Gives:** two registers, populated at load and during execution:
- **CHOICES** — every axiomatic decision the kernel makes, with the alternatives
  it forecloses and the consequence of the choice. The kernel's contingency,
  in the kernel.
- **HORIZON** — incapacity claims: things this system cannot state or prove,
  each tagged *theorem-forced* (Gödel II, Tarski, Turing/Rice — no possible
  successor language escapes these) or *choice-forced* (consequences of our
  own carvings — a successor could choose otherwise, at other costs).

**Hidden choices:** deciding what counts as a "choice" worth confessing is
itself a choice. The register is honest, not complete — completeness of
self-description is exactly what Gödel forecloses. The register says so, about
itself, as its first entry.

**Cannot say:** that the confession is finished. Ever.

**Breaks when:** the registers grow too large to read — confession without a
reader is ritual. (Open problem, inherited from the hermeneutics-of-output
essay: outputs need reading instructions; confessions doubly so.)

---

## Layer 1 · Evidence algebra (the bilattice)

**Gives:** the value substrate. Not booleans. Each evidential value is a pair
(μ, λ): degree of favorable evidence, degree of contrary evidence, varying
**independently**. Following Belnap/Ginsberg/Fitting, two distinct orderings
that booleans fuse:

- **truth ordering** (⋀, ⋁, with negation ¬ swapping μ↔λ): how the *verdict* combines
- **knowledge ordering** (⊗ consensus, ⊕ accept-all, with conflation − swapping known↔unknown): how the *information* combines

Derived readings: certainty Gc = μ−λ; contradiction Gct = μ+λ−1. Five verdict
regions: **true, false, inconsistent, paracomplete, blur**. Verdicts are
*observations* of evidence, never mutations of it. Explosion is blocked by
construction: contradiction is a location in the lattice, not a license.

**Hidden choices (surfaced, entered in CHOICES):**
1. *Quantification is a collapse.* Putting evidence on [0,1] assumes all
   testimony is commensurable on a line. Alternatives: Belnap's four discrete
   values, Dempster–Shafer intervals, qualitative orders. We chose reals for
   v0 tractability and confess it.
2. *min/max lattice ops ignore corroboration:* two independent weak sources
   never strengthen each other. Alternatives (product, Łukasiewicz) trade this
   for other distortions. Chosen; confessed.
3. *The para-analyzer geometry* (threshold, four corners + blur center) is one
   carving of the evidence square. The blur region is where this carving
   confesses its own arbitrariness — which is why blur is generative (Layer 6).

**Cannot say:** "true in the world." Only: "the evidence file, combined under
these confessed operations, sits in the true-region of this confessed geometry."

**Breaks when:** sources are not independent (double-counted testimony inflates
μ or λ), or when evidence is inherently non-scalar (narrative testimony).
Both breakages are metered, not masked.

---

## Layer 2 · Testimony and provenance

**Gives:** values of testimonial origin are **case files**, not facts: every
(μ, λ) carries its trail — who said what, with what polarity and weight, and
which operations it flowed through. The program is a juror, and the docket
is inspectable. Nothing is laundered into a bare number.

**Hidden choices:** a testimony schema (source, polarity, weight) flattens the
speech-act: it drops *when*, *under what incentive*, *in reply to what*. v0
confesses this; a later layer may thicken testimony into dialogue.

**Cannot say:** whether a source is reliable — only track record within the
file. Source reliability estimated from the file is circular (sources vouch
for sources); the circle is noted in HORIZON, not hidden.

**Breaks when:** provenance trails grow unboundedly. Truncation policies are
collapses and must go through the Residue Ledger like any collapse.

---

## Layer 3 · The negation family (kept plural)

**Gives:** at least four negations, first-class and never conflated:

| negation | action on (μ,λ) | reading |
|---|---|---|
| `¬t` truth negation | (λ, μ) | the verdict reversed: evidence *against* becomes evidence *for* the negation |
| `−k` conflation | (1−λ, 1−μ) | the knowledge reversed: what is known becomes unknown and vice versa |
| `absent` default | file empty → (0,0) marked | "my file is silent" — a fact about the file, never about the world |
| `refute` constructive | attach a refutation trail | "here is the machine that eats claims of P" — negation with a witness |

Note the fixed points: `¬t` fixes Both and Neither (contradiction survives
verdict-reversal); `−k` fixes True and False (knowledge-reversal preserves
settled verdicts). The two negations *commute past different things* — this
non-interchangeability is the first-class-ness.

**Cannot say:** "not P" simpliciter. The kernel forces the speaker to choose
*which* not — and records the choice in the trail.

**Breaks when:** users want plain boolean not. There is no plain not. This is
the point of maximum cultural friction, accepted deliberately.

---

## Layer 4 · Flow without collapse

**Gives:** the branch primitive is not two-way and does not choose.
`explore(ev, branches)` computes soft weights for all five regions from
(Gc, Gct), runs **every live branch**, and returns a **Bundle** of weighted
outcomes — the perspectives interfere without collapsing one another.

Collapse exists — action in the world often demands one body, one motion —
but as a **separate, explicit, priced act**: `collapse(bundle, reason)` picks
by policy and files a **Residue** in the Ledger: what was discarded, at what
weight, for what stated reason. The road not taken has a receipt.

**Hidden choices:** running all branches assumes branches are side-effect-free
enough to co-exist (v0: they are, by discipline; a real implementation needs
an effect system — noted in HORIZON as debt). Weight formulas are a carving;
confessed in CHOICES.

**Cannot say:** which branch was "right." Only which was chosen, why, and what
it cost.

**Breaks when:** branch fan-out compounds (bundles of bundles). Exponential
possibility is the honest shape of underdetermination; managing it without
silent pruning is the layer's open frontier. Every pruning is a collapse;
every collapse leaves residue; the Ledger is the audit trail of everything
the program decided not to be.

---

## Layer 5 · Anomaly (errors as information)

**Gives:** no exceptions, no crashes, no NaN-with-the-case-file-burned.
Operations that cannot proceed return an **Anomaly**: kind, origin, and a
context trail extended by everything it subsequently flows through. Anomalies
are *read*, not caught: an anomaly arriving downstream is a report about
upstream reality (or about the vocabulary's insufficiency — in which case it
can be handed to Layer 6 as blur pressure).

**Cannot say:** that an anomaly is meaningless. It may be uninterpreted;
it is never noise by fiat.

**Breaks when:** anomaly trails become the program's main output — a system
that mostly reports its own confusions. But note: for exploratory work at the
edge of a vocabulary, that *is* the desired output. Confusion, well-documented,
is the raw material of Layer 6.

---

## Layer 6 · Necessity and genesis (evolution from need)

**Gives:** the vocabulary is not fixed. A **Necessity meter** counts blur
verdicts per predicate. When blur pressure on a predicate crosses threshold,
the kernel emits a **genesis proposal**: this carving has failed often enough,
here, that the single axis is declared insufficient — and the accumulated
blur cases become the seed data for a *new distinction*, created via
`gap.seed(name)`, whose birth record cites the gap and the pressure that
necessitated it.

New words are born from documented failure of old words, and remember it.
Evolution from necessity, mechanized minimally.

**Hidden choices:** the pressure threshold; what counts as "the same" blur
(identity of confusions — a hard problem, related to essay 01's structured
identity). Both confessed.

**Cannot say:** what the new distinction *means* — meaning accrues from
subsequent use. The kernel can only issue the birth certificate.

**Breaks when:** genesis is too eager (vocabulary inflation: a word per
confusion) or too shy (blur normalized, insufficiency chronic). The eager/shy
dial is a value judgment; it lives in CHOICES, not in a constant pretending
to be neutral.

---

## Layer 7 · Self-description with honest limits (horizon, not mirror)

**Gives:** the kernel answers questions about itself the only way it lawfully
can. Asked to prove its own consistency → Gap, citing Gödel II. Asked for a
truth predicate over its own sentences → Gap, citing Tarski. Asked to decide
halting of arbitrary code → Gap, citing Turing. These are not exceptions or
refusals — they are *pointings*, filed in HORIZON with reasons, distinguishable
from choice-forced limits which a successor language could lift.

This is the anti-escape-hatch made structural: where other languages put
`unsafe` (silent exit), Lucky puts a signed statement of incapacity
(loud non-exit).

**Cannot say:** everything it cannot say. The horizon of the horizon recedes.
Filed, of course, in HORIZON — as its own last entry.

---

## What Lucky is not (its own validity claim, kept honest)

Lucky is not superior to boolean languages. For a controlled tiny universe —
a thermostat, a checksum — the boolean's fused assumptions are all *true
enough*, and Lucky's apparatus is pure cost. Lucky's regime of validity is
the situation Kelly names: multiple perspectives, real conflict, live gaps,
vocabulary under pressure. Every language is a theory of what can be safely
ignored; Lucky's theory is that in its home regime, *nothing about the
evidence's structure* can be safely ignored — and it pays for that theory
in ergonomics, gladly, and says so.
