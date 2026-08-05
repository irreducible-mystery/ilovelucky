# Comparative Audit: Logic Etau (LPA2v, Paraconsistent-Lib) vs. Lucky

**Object examined:** `paraconsistent` 0.2.4 (pip) / Paraconsistent-Lib
(EAILAB-IFSP), a Python implementation of two-valued Annotated Paraconsistent
Logic (LPA2v), the working core of Logic Etau — the tradition Lucky's Layer 1
explicitly borrowed from. Also cloned for reference: pyraanalyzer.
Probes: `probe_etau.py` (runnable; all findings below reproduce).

The purpose is symmetric: find their hidden assumptions AND ours.
Where they diverge from us, either could be the one paying the wrong price.

---

## 1. Where we agree — and Lucky is genuinely downstream of their work

- **(mu, lam) independence** is their foundation and ours: favorable and
  contrary evidence never forced to sum to 1. Their dc/dct are our Gc/Gct
  (we took the names from this school and confess it in the register).
- **Conflict and ignorance kept apart**: their 12-region lattice separates
  the conflict apex from the ignorance apex exactly as our five regions do;
  probe 1 confirms clean corner behavior identical to Lucky's.
- **No explosion**: contradiction is a location, not a license. Confirmed —
  strong conflict yields a label and a workflow, never an inference free-for-all.
- **Richer interior than ours**: their 12 regions vs. our 5. Their
  quasi-regions (Qt->conflict, Q-conflict->t, etc.) encode *direction of
  tendency* inside the blur — genuinely finer vocabulary than our single
  "blur" region. Lucky's carving is coarser here; noted as a real gap in us.
- **Geometry we lack**: radial distance to the nearest apex (their d, dcr)
  is a second-order reading our verdicts don't have — how far the evidence
  sits from *ideal* support or counter-support, not just from region edges.

## 2. The central finding: the last step gives back what the middle earned

**Probe 2 + the slight-lean surprise.** Their pipeline maintains the full
evidential structure for its entire length — and then `decision_output`
compresses everything to **1.0 / 0.0 / 0.5**:

- strong conflict (dct=+0.80) -> 0.5
- total ignorance (dct=-0.80) -> 0.5
- dead center                -> 0.5

Three profoundly different epistemic situations, one exit value. The
distinction the 12 regions worked to keep is surrendered at the door.
Worse: **a slight lean (dc=+0.10, mu=0.55) exits as decision=1.0** — full
commitment from a whisper of net evidence, because the decision rule is a
hard threshold on muER with no dead zone and no strength report.

In Lucky's terms: their final step is an *unpriced collapse*. No receipt,
no residue, no record that conflict-0.5 and ignorance-0.5 are different
animals. This is the single strongest vindication of Lucky's design choice
that **collapse must be explicit, separate, and leave a ledger entry** —
and it is exactly where a deployed Etau controller would quietly convert
"the sensors disagree violently" into the same actuator value as "the
sensors are silent."

## 3. Their hidden assumptions (each one is a Lucky layer's reason to exist)

**A. Testimony has no origin (probe 3).** Inputs are bare floats. Where mu
came from — one source or thirty, independent or an echo chamber — is
invisible and unrepresentable. The entire intake problem (Lucky Layers 2,
v2 source graph) is delegated, unmarked, to the caller. The library cannot
even *state* the independence assumption it silently rests on.

**B. Silent repair over pointing (probe 4).** Out-of-range inputs are
clamped without any signal at the input proxy (mu=1.7 was even *stored*
unclamped and only repaired at compute — the object will happily report an
impossible input as its current state). Config abuses produce warnings;
input abuses produce nothing. Lucky returns an informational anomaly for
unregistered modes; Etau-lib repairs and moves on. Repair-without-record is
a small unpriced collapse at the very first gate.

**C. The carving's edges are invisible (probe 5).** The same evidence flips
labels across FtC settings, and nothing reports the distance to the flip.
FtC, VlV, VlF are tunable authorities whose influence is not measured
in-band. Lucky v1's flip@ exists precisely for this. (Symmetric honesty:
our flip distance cannot audit intake inflation — field notes 03 — so
neither system sees through its inputs. But ours at least reports the edge.)

**D. Analysis without memory (probe 7).** Mutating the input overwrites the
prior analysis; no history, no trail, no case file. Evidence is a present-
tense quantity. The past is unrecoverable by design.

**E. An analyzer, not a language (probe 6).** No negations, no connectives,
no consensus/merge operations over annotated values — no way to *compose*
evidence claims. The API walk found zero logical operations. LPA2v the
*formalism* has NOT-mu = (lam, mu) etc.; the *library* ships the analyzer
block only. The reasoning-network layer exists as block wiring (feeding
muER of one block into the mu of another), which smuggles composition
through an unannotated channel: muER strips the contradiction dimension,
so downstream blocks inherit a laundered scalar.

**F. Constants presenting as neutral.** FtC=0.50, decision ties at exactly
0.5, the sqrt(1/2) normalization of radial distance — all live in code
without a register of what they foreclose. (This was v0-Lucky's defect A,
so we recognize the species immediately.)

## 4. What they have that Lucky should take seriously

1. **The 12-region interior.** Direction-of-tendency inside blur is real
   information our five regions flatten. A Lucky verdict of "blur, tending
   toward true, away from conflict" would be strictly richer — and their
   region names prove the vocabulary is constructible.
2. **Radial certainty (dcr).** Distance-to-apex is a second sensitivity
   axis, complementary to our distance-to-edge. Both together give a
   verdict coordinates *and* bearings.
3. **Asymmetric thresholds (VlV/VlF).** Different strictness for accepting
   support vs. counter-support — decision-theoretically sound (costs of
   the two mistakes differ) and absent from Lucky, where THRESHOLD is one
   number for all four edges. Their bias knobs are unregistered; ours
   don't exist. Registered asymmetric thresholds would beat both.
4. **Engineering maturity.** Clean caching, typed outputs, parameter
   validation, MATLAB parity for a community of practice. Twenty-plus
   years of deployment stand behind this school; Lucky has three demos.

## 5. Verdict of the comparison (in our own vocabulary, with its own receipt)

Etau/LPA2v solved the **annotation algebra** and the **interior geometry**
of the evidence square — earlier and finer than Lucky. It did not attempt
what Lucky's other layers exist for: provenance, priced collapse, registered
choices, sensitivity-in-band, anomalies as values, vocabulary growth, or
self-description. Those are not flaws of execution; they are simply outside
its concept. The one place the comparison finds an *internal* tension is
the exit: a formalism built to keep conflict and ignorance distinct ships
a decision function that merges them — the middle of the pipeline is wiser
than its final step.

What we take: the 12-region interior, radial certainty, asymmetric
thresholds — all three now queued as registered choices for a future
Lucky revision, each with a birth record citing this audit.

What we keep that they lack: everything about *where evidence comes from*
and *what deciding costs*.

Omissions receipt for this audit: we probed the pip library and read the
source of one implementation; the broader Etau literature (para-quantum
extensions, hardware controllers, the full para-analyzer algorithm with
evidence intervals) was surveyed only through its software shadow. Claims
here bind the library, not the school.
