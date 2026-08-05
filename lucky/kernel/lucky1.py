"""
lucky1 -- kernel v1. Revision of lucky0 driven by the v0 audit.

Changes from v0, keyed to the audit's priority list:
  1. Every axiomatic choice registers at import time (module load), never
     lazily. Includes: genesis threshold, numeric substrate, explore weight
     formula, liveness threshold, testimony combination modes, confusion
     identity key.
  2. Verdicts are structured values carrying distance-to-boundary data:
     a verdict that would change under a small perturbation is
     distinguishable, in-band, from a robust one.
  3. Numeric substrate confessed AND hardened: all evidence arithmetic is
     quantized to a registered precision.
  4. testify() gains a registered, configurable combination mode:
     "max" (no corroboration) or "noisy_or" (independent corroboration).
     The mode used is recorded in the trail.
  5. Unparsed self-questions feed a pressure meter on the self-model;
     at threshold, a genesis proposal is emitted, and the self-model can
     be taught new vocabulary carrying its birth record. Distinction is
     now consumed by another layer, not just a certificate.
  6. explore() performs a minimal purity check: each branch receives its
     own copy of the evidence, and mutation of it (or of the session
     ledger) is detected and reported as an informational Anomaly.
  7. Confusion identity is structural (predicate + evidential neighborhood),
     not a bare string match. Registered as a choice with its
     foreclosed alternatives.
Also: session-scoped ledgers (no accumulating module global), corrected
Gap wording, receipts quantized.
"""
from dataclasses import dataclass, field
from typing import Callable, Optional
import copy as _copy
import math

# ---------------------------------------------------------------- registers
# All axiomatic choices register HERE, at import. No lazy registration.
CHOICES: list[dict] = []
HORIZON: list[dict] = []

def choose(name, chosen, foreclosed, consequence):
    CHOICES.append(dict(name=name, chosen=chosen, foreclosed=foreclosed,
                        consequence=consequence))

def cannot(claim, why, forced_by):
    HORIZON.append(dict(claim=claim, why=why, forced_by=forced_by))

cannot("this register of choices is complete",
       "complete self-description is unavailable to any system describing "
       "itself from inside; the register is honest, not exhaustive", "theorem")

choose("confession granularity",
       "register every axiomatic constant and formula at import time",
       "lazy registration (v0's defect: choices missing unless code paths ran)",
       "the register's contents no longer depend on which features were used")

# ------- numeric substrate (priority 3)
PRECISION = 6
def q(x: float) -> float:
    return round(float(x), PRECISION)

choose("numeric substrate",
       f"IEEE-754 doubles quantized to {PRECISION} decimal places at every "
       "evidence operation and every ledger receipt",
       "exact rationals (cost: unbounded denominators); intervals (cost: "
       "width growth); raw doubles (cost: unreadable receipts, v0's leakage)",
       "residue receipts are now stable and readable; a sub-precision "
       "distinction cannot be represented, and that loss is this entry")

# ------- evidence geometry
THRESHOLD = 0.55
choose("verdict geometry",
       f"threshold t={THRESHOLD} carving the evidence square into five "
       "regions (true/false/inconsistent/paracomplete/blur)",
       "other thresholds; smooth membership without regions; learned carvings",
       "any hard carving misclassifies near its edges; the Verdict object "
       "now reports its own distance to those edges (audit priority 2)")

choose("evidence quantification", "degrees on [0,1] x [0,1]",
       "four discrete values; interval-valued belief; qualitative orders",
       "assumes testimony commensurable on a line; a confessed reduction")

choose("lattice operations", "min/max for AND/OR, consensus, accept_all",
       "product forms; averaging forms",
       "verdict combination stays idempotent; corroboration is handled "
       "separately, at testimony intake (see 'testimony combination')")

# ------- testimony combination (priority 4)
choose("testimony combination",
       "configurable per intake: 'max' (default; strongest voice per side) "
       "or 'noisy_or' (independent corroboration: 1 - prod(1 - w)); the mode "
       "used is written into the trail",
       "a single fixed rule (v0 used bare max and under-documented it); "
       "dependence-aware pooling (needs a source-relation model, future work)",
       "'noisy_or' assumes source independence; correlated sources will "
       "overcount. The assumption is now selectable and visible, not silent")

# ------- explore weights (priority 1: previously unregistered)
LIVENESS = 0.05
choose("explore weight formula",
       "raw region weights from (|Gc|,|Gct|) rectified; blur = 1 - max(raw); "
       "normalized to sum 1; branches below liveness cutoff "
       f"{LIVENESS} are not run",
       "softmax over region distances; exact area partition of the square",
       "the liveness cutoff is itself a small collapse: branches under it "
       "vanish without a receipt. Registered here so the cost is on record")

# ------- confusion identity (priority 7)
NEIGHBORHOOD = 1  # decimal places for evidential neighborhood bucketing
choose("confusion identity",
       "two blur events count as 'the same confusion' when they share a "
       f"predicate AND an evidential neighborhood (Gc, Gct rounded to "
       f"{NEIGHBORHOOD} decimal place)",
       "bare predicate-name match (v0: too coarse, merges unlike confusions); "
       "correspondence-based structured identity (richer; future work)",
       "a structural key, still crude: confusions differing only in "
       "provenance are merged; the merge is this entry's price")

# ------- genesis threshold (priority 1: was lazily registered in v0)
GENESIS_THRESHOLD = 3
choose("genesis threshold",
       f"{GENESIS_THRESHOLD} same-confusion events trigger a genesis proposal",
       "eager (one word per confusion) or reluctant (pressure normalized, "
       "insufficiency chronic)",
       "the eager/reluctant dial is a value judgment; it lives here, "
       "not in a constant presenting itself as neutral")

SELF_THRESHOLD = 3
choose("self-model pressure threshold",
       f"{SELF_THRESHOLD} unparsed self-questions trigger a genesis proposal "
       "on the self-model's own vocabulary",
       "never growing the self-model (v0); unbounded auto-growth without "
       "a teaching step",
       "growth requires an explicit teach() with a birth record: the "
       "self-model does not silently rewrite itself")

# ---------------------------------------------------------------- Gap
class Gap:
    """The reified outside. Consuming: operations extend its notes.
    Generative: it can seed a Distinction. No unwrap, no bool coercion."""
    def __init__(self, pointing_at: str, notes: tuple = ()):
        self.pointing_at = pointing_at
        self.notes = notes
    def absorb(self, attempted: str) -> "Gap":
        return Gap(self.pointing_at, self.notes + (attempted,))
    def seed(self, name: str, seed_cases: list) -> "Distinction":
        return Distinction(name=name, born_from=self, seed_cases=list(seed_cases))
    def __repr__(self):
        tail = f" carrying {len(self.notes)} notes" if self.notes else ""
        return f"<Gap -> {self.pointing_at!r}{tail}>"

@dataclass
class Distinction:
    """New vocabulary with a birth record. In v1, other layers consume it."""
    name: str
    born_from: Gap
    seed_cases: list
    def __repr__(self):
        return (f"<Distinction {self.name!r} born from "
                f"{self.born_from.pointing_at!r}, {len(self.seed_cases)} seed cases>")

# ---------------------------------------------------------------- Anomaly
@dataclass
class Anomaly:
    kind: str
    origin: str
    trail: tuple = ()
    def flow(self, through: str) -> "Anomaly":
        return Anomaly(self.kind, self.origin, self.trail + (through,))
    def __repr__(self):
        return f"<Anomaly {self.kind!r} from {self.origin!r} via {len(self.trail)} steps>"

# ---------------------------------------------------------------- Verdict
@dataclass(frozen=True)
class Verdict:
    """A verdict that carries its own sensitivity (audit priority 2)."""
    region: str
    flip_distance: float      # smallest (Gc or Gct) perturbation changing region
    edge_distances: dict      # signed distance to each region's entry edge

    def __repr__(self):
        return f"{self.region}(flip@{self.flip_distance:.2f})"

def _verdict(gc: float, gct: float, t: float = THRESHOLD) -> Verdict:
    edges = {  # positive = inside that region's entry condition
        "true":         q(gc - t),
        "false":        q(-gc - t),
        "inconsistent": q(gct - t),
        "paracomplete": q(-gct - t),
    }
    inside = [r for r, d in edges.items() if d >= 0]
    if inside:
        region = max(inside, key=lambda r: edges[r])
        flip = edges[region]                     # distance back to the edge
    else:
        region = "blur"
        flip = q(min(t - abs(gc), t - abs(gct)))  # nearest exit from blur
    return Verdict(region, q(flip), edges)

# ---------------------------------------------------------------- Evidence
@dataclass(frozen=True)
class Testimony:
    source: str
    polarity: str            # 'for' | 'against'
    weight: float

@dataclass
class Ev:
    mu: float = 0.0
    lam: float = 0.0
    trail: tuple = ()

    def __post_init__(self):
        self.mu, self.lam = q(self.mu), q(self.lam)

    @property
    def gc(self):  return q(self.mu - self.lam)
    @property
    def gct(self): return q(self.mu + self.lam - 1.0)

    def verdict(self) -> Verdict:
        return _verdict(self.gc, self.gct)

    # truth ordering
    def AND(self, o): return Ev(min(self.mu,o.mu), max(self.lam,o.lam), self.trail+o.trail+("AND",))
    def OR(self, o):  return Ev(max(self.mu,o.mu), min(self.lam,o.lam), self.trail+o.trail+("OR",))
    # knowledge ordering
    def consensus(self, o):  return Ev(min(self.mu,o.mu), min(self.lam,o.lam), self.trail+o.trail+("consensus",))
    def accept_all(self, o): return Ev(max(self.mu,o.mu), max(self.lam,o.lam), self.trail+o.trail+("accept_all",))

    def __repr__(self):
        return (f"Ev(mu={self.mu:.2f}, lam={self.lam:.2f} | Gc={self.gc:+.2f} "
                f"Gct={self.gct:+.2f} -> {self.verdict()!r})")

def _combine(weights: list[float], mode: str):
    if not weights: return 0.0
    if mode == "max":      return max(weights)
    if mode == "noisy_or":
        acc = 1.0
        for w in weights: acc *= (1.0 - w)
        return 1.0 - acc
    return None

def testify(*ts: Testimony, combine: str = "max"):
    """Build a case file. Combination mode is registered vocabulary and
    is recorded in the trail. Unknown modes return an informational Anomaly."""
    mu  = _combine([t.weight for t in ts if t.polarity == "for"], combine)
    lam = _combine([t.weight for t in ts if t.polarity == "against"], combine)
    if mu is None or lam is None:
        return Anomaly("unregistered combination mode", "testify",
                       (f"requested {combine!r}; registered: max, noisy_or",))
    return Ev(mu, lam, tuple(ts) + (f"combine:{combine}",))

# ---------------------------------------------------------------- negations
def not_t(e: Ev) -> Ev:      # verdict reversal; fixes inconsistent/paracomplete
    return Ev(e.lam, e.mu, e.trail + ("not_t",))
def conflate(e: Ev) -> Ev:   # known <-> unknown; fixes true/false
    return Ev(1-e.lam, 1-e.mu, e.trail + ("conflate",))
def absent() -> Ev:
    return Ev(0.0, 0.0, ("absent: file silent, not world-negative",))
def refute(e: Ev, witness: str) -> Ev:
    return Ev(e.mu, max(e.lam, 0.9), e.trail + (f"refutation:{witness}",))

cannot("collapse the negation family into one operator",
       "the four negations act differently (distinct fixed points); a single "
       "'not' would discard which reversal was meant", "choice")

# ---------------------------------------------------------------- Session
class Session:
    """Scopes the ledger and pressure meters (fixes v0's accumulating
    module globals). CHOICES/HORIZON stay module-level: they describe the
    kernel itself, not any one run."""
    def __init__(self):
        self.ledger: list[dict] = []
        self.pressure: dict[tuple, list] = {}     # structural key -> cases
        self.self_model = SelfModel(self)

    # ------- flow (priorities 1, 6)
    def explore(self, e: Ev, branches: dict[str, Callable]) -> "Bundle":
        raw = {"true": max(0.0, e.gc), "false": max(0.0, -e.gc),
               "inconsistent": max(0.0, e.gct), "paracomplete": max(0.0, -e.gct)}
        raw["blur"] = max(0.0, 1.0 - max(raw.values()))
        total = sum(raw.values()) or 1.0
        weights = {r: q(w / total) for r, w in raw.items()}
        outcomes, purity_notes = [], []
        for region, weight in weights.items():
            if weight <= LIVENESS or region not in branches:
                continue
            given = _copy.deepcopy(e)             # branch gets its own copy
            ledger_len = len(self.ledger)
            value = branches[region](given)
            if given != e:                        # mutation detected
                purity_notes.append(Anomaly(
                    "branch mutated its evidence copy", f"branch:{region}",
                    ("coexistence claim would have been violated silently in v0",)))
            if len(self.ledger) != ledger_len:
                purity_notes.append(Anomaly(
                    "branch wrote to the ledger during exploration",
                    f"branch:{region}",
                    ("collapse-like effects inside explore are reportable, not permitted silently",)))
            outcomes.append((region, weight, value))
        return Bundle(outcomes, tuple(purity_notes))

    def collapse(self, b: "Bundle", reason: str):
        if not b.outcomes:
            return Gap("collapse of an empty bundle: nothing was live")
        kept = max(b.outcomes, key=lambda o: o[1])
        self.ledger.append(dict(
            kept=kept[0], kept_weight=q(kept[1]),
            discarded=[(r, q(w)) for r, w, _ in b.outcomes if r != kept[0]],
            purity_notes=len(b.purity_notes), reason=reason))
        return kept[2]

    # ------- necessity (priorities 1, 7)
    def observe(self, predicate: str, e: Ev) -> Optional[Gap]:
        v = e.verdict()
        if v.region != "blur":
            return None
        key = (predicate, round(e.gc, NEIGHBORHOOD), round(e.gct, NEIGHBORHOOD))
        cases = self.pressure.setdefault(key, [])
        cases.append(e)
        if len(cases) >= GENESIS_THRESHOLD:
            return Gap(f"vocabulary insufficiency: {predicate!r} blurred "
                       f"{len(cases)} times in neighborhood (Gc~{key[1]}, "
                       f"Gct~{key[2]}); this axis is inadequate here")
        return None

@dataclass
class Bundle:
    outcomes: list                        # [(region, weight, value)]
    purity_notes: tuple = ()
    def __repr__(self):
        inner = ", ".join(f"{r}:{w:.2f}" for r, w, _ in self.outcomes)
        pn = f" +{len(self.purity_notes)} purity notes" if self.purity_notes else ""
        return f"<Bundle {inner}{pn}>"

# ---------------------------------------------------------------- self-model
class SelfModel:
    """Lawful self-description whose vocabulary can grow -- but only via an
    explicit teach() carrying a birth record (audit priority 5)."""
    def __init__(self, session):
        self.session = session
        self.unparsed: list[str] = []
        self.learned: list[Distinction] = []
        self.patterns: list[tuple] = [
            (("consisten",), lambda: Gap(
                "own consistency: unavailable from inside if actually present "
                "(second incompleteness result)")),
            (("truth", "own"), lambda: Gap(
                "own truth predicate: no language contains one (Tarski); "
                "interpretation is available, truth is not")),
            (("halt",), lambda: Gap(
                "halting of arbitrary code: undecidable (Turing)")),
            (("everything", "cannot"), lambda: Gap(
                "the horizon of the horizon: the incapacity register "
                "cannot itself be complete")),
        ]

    def ask(self, question: str):
        ql = question.lower()
        for keys, responder in self.patterns:
            if all(k in ql for k in keys):
                return responder()
        self.unparsed.append(question)
        if len(self.unparsed) >= SELF_THRESHOLD:
            return Gap("self-model vocabulary insufficiency: "
                       f"{len(self.unparsed)} questions unparsed",
                       tuple(self.unparsed))
        return Anomaly("unparsed self-question", "self_model",
                       (f"question {len(self.unparsed)}/{SELF_THRESHOLD} "
                        "toward a genesis proposal",))

    def teach(self, gap: Gap, keys: tuple, responder: Callable, name: str):
        """Vocabulary growth with provenance. The Distinction is consumed:
        it becomes an active pattern, and its birth record stays attached."""
        d = gap.seed(name, list(gap.notes))
        self.learned.append(d)
        self.patterns.append((keys, responder))
        self.unparsed = []
        return d

cannot("declare a collapsed branch correct",
       "only which was kept, why, and what was set aside; correctness would "
       "require a standpoint outside all perspectives", "theorem")
cannot("verify branch purity in general",
       "the v1 check detects mutation of the evidence copy and ledger writes; "
       "arbitrary external effects are undetectable without a full effect "
       "system (recorded as open debt)", "choice")
