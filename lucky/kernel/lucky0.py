"""
lucky0 -- kernel v0 of a language that points at its gaps.

Layers implemented (see design/00-foundational-layers.md):
  -1  Gap        : the reified outside; consuming and generative
   0  Confession : CHOICES (contingency register) and HORIZON (incapacity register)
   1  Evidence   : bilattice (mu, lam); two orderings; five verdict regions
   2  Testimony  : values are case files with provenance trails
   3  Negations  : a plural family, never conflated into one 'not'
   4  Flow       : explore-all-branches Bundles; collapse is explicit + priced (Residue Ledger)
   5  Anomaly    : errors as information-bearing values with case files
   6  Necessity  : blur pressure metered; genesis of new distinctions from gaps
   7  Self       : lawful self-description -- Godel/Tarski/Turing as pointings, not crashes

No escape hatches. No exceptions cross the API. Nothing silently collapses.
"""
from dataclasses import dataclass, field
from typing import Callable, Optional
import itertools

# ---------------------------------------------------------------- Layer 0
CHOICES: list[dict] = []
HORIZON: list[dict] = []

def choose(name: str, chosen: str, foreclosed: str, consequence: str):
    CHOICES.append(dict(name=name, chosen=chosen, foreclosed=foreclosed,
                        consequence=consequence))

def cannot(claim: str, why: str, forced_by: str):
    """forced_by: 'theorem' (no successor escapes) or 'choice' (ours; costs to lift)."""
    entry = dict(claim=claim, why=why, forced_by=forced_by)
    HORIZON.append(entry)
    return entry

# The registers' first entries are about themselves:
cannot("this confession register is complete",
       "completeness of self-description is foreclosed (Godel II analogue); "
       "the register is honest, not exhaustive", "theorem")
choose("confession granularity",
       "register axiomatic choices at layer boundaries",
       "registering every micro-decision (unreadably large) or none (dishonest)",
       "the register is a curated confession; curation is itself a choice")

# ---------------------------------------------------------------- Layer -1
class Gap:
    """The reified outside. Not null, not error, not unknown.
    Consuming: operations on a Gap yield a Gap with extended context.
    Generative: a Gap can seed a new Distinction."""
    def __init__(self, pointing_at: str, context: tuple = ()):
        self.pointing_at = pointing_at
        self.context = context
    def absorb(self, attempted: str) -> "Gap":
        return Gap(self.pointing_at, self.context + (attempted,))
    def seed(self, name: str, seed_cases: list) -> "Distinction":
        return Distinction(name=name, born_from=self, seed_cases=seed_cases)
    def __repr__(self):
        tail = f" after {len(self.context)} attempts" if self.context else ""
        return f"<Gap -> {self.pointing_at!r}{tail}>"
    # Deliberately missing: unwrap(), __bool__(), default coercions.

@dataclass
class Distinction:
    """New vocabulary, born from a gap, carrying its birth record."""
    name: str
    born_from: Gap
    seed_cases: list
    def __repr__(self):
        return (f"<Distinction {self.name!r} born from gap "
                f"{self.born_from.pointing_at!r} with {len(self.seed_cases)} seed cases>")

# ---------------------------------------------------------------- Layer 1+2
choose("evidence quantification", "degrees on [0,1] x [0,1]",
       "Belnap's 4 discrete values; Dempster-Shafer intervals; qualitative orders",
       "assumes all testimony commensurable on a line; a confessed collapse")
choose("lattice operations", "min/max (Godel t-norm)",
       "product (corroboration-sensitive), Lukasiewicz",
       "independent weak sources never strengthen each other in v0")

@dataclass(frozen=True)
class Testimony:
    source: str
    polarity: str          # 'for' | 'against'
    weight: float

@dataclass
class Ev:
    """An evidential value: a case file, never a bare number."""
    mu: float = 0.0        # favorable evidence
    lam: float = 0.0       # contrary evidence  (independent of mu!)
    trail: tuple = ()      # provenance: testimonies and operations

    # --- readings (observations, not mutations) ---
    @property
    def gc(self):  return self.mu - self.lam          # certainty
    @property
    def gct(self): return self.mu + self.lam - 1.0    # contradiction

    def verdict(self, t: float = 0.55) -> str:
        if self.gc >= t:    return "true"
        if self.gc <= -t:   return "false"
        if self.gct >= t:   return "inconsistent"     # everybody disagrees
        if self.gct <= -t:  return "paracomplete"     # nobody knows
        return "blur"                                  # the carving is failing HERE

    # --- truth ordering (verdict combination) ---
    def AND(self, o):  return Ev(min(self.mu,o.mu), max(self.lam,o.lam), self.trail+o.trail+("AND",))
    def OR(self, o):   return Ev(max(self.mu,o.mu), min(self.lam,o.lam), self.trail+o.trail+("OR",))

    # --- knowledge ordering (information combination) ---
    def consensus(self, o):   # what both files agree on
        return Ev(min(self.mu,o.mu), min(self.lam,o.lam), self.trail+o.trail+("consensus",))
    def accept_all(self, o):  # merge everything both files hold
        return Ev(max(self.mu,o.mu), max(self.lam,o.lam), self.trail+o.trail+("accept_all",))

    def __repr__(self):
        return f"Ev(mu={self.mu:.2f}, lam={self.lam:.2f} | Gc={self.gc:+.2f} Gct={self.gct:+.2f} -> {self.verdict()})"

def testify(*ts: Testimony) -> Ev:
    """Build a case file from testimony. Favorable and contrary accumulate
    INDEPENDENTLY -- conflict is preserved, never averaged away."""
    mu  = max((t.weight for t in ts if t.polarity == "for"),     default=0.0)
    lam = max((t.weight for t in ts if t.polarity == "against"), default=0.0)
    return Ev(mu, lam, tuple(ts))

# ---------------------------------------------------------------- Layer 3
def not_t(e: Ev) -> Ev:
    """Truth negation: verdict reversed. Fixes inconsistent & paracomplete."""
    return Ev(e.lam, e.mu, e.trail + ("not_t",))

def conflate(e: Ev) -> Ev:
    """Knowledge negation: known <-> unknown. Fixes true & false."""
    return Ev(1-e.lam, 1-e.mu, e.trail + ("conflate",))

def absent() -> Ev:
    """Default negation: 'my file is silent' -- a fact about the FILE."""
    return Ev(0.0, 0.0, ("absent: file silent, not world-false",))

def refute(e: Ev, refutation: str) -> Ev:
    """Constructive negation: contrary evidence WITH a witness attached."""
    return Ev(e.mu, max(e.lam, 0.9), e.trail + (f"refutation:{refutation}",))

cannot("say plain boolean 'not P'",
       "the kernel has four negations that behave differently; conflating them "
       "is the boolean's central information-destroying move", "choice")

# ---------------------------------------------------------------- Layer 5
@dataclass
class Anomaly:
    """An error as information: a case file, not a crash."""
    kind: str
    origin: str
    trail: tuple = ()
    def flow(self, through: str) -> "Anomaly":
        return Anomaly(self.kind, self.origin, self.trail + (through,))
    def __repr__(self):
        return f"<Anomaly {self.kind!r} from {self.origin!r} via {len(self.trail)} steps>"

# ---------------------------------------------------------------- Layer 4
RESIDUE_LEDGER: list[dict] = []

@dataclass
class Bundle:
    """Uncollapsed outcomes: perspectives coexisting, weighted, interfering."""
    outcomes: list          # [(region, weight, value)]
    def __repr__(self):
        inner = ", ".join(f"{r}:{w:.2f}" for r, w, _ in self.outcomes)
        return f"<Bundle {inner}>"

def explore(e: Ev, branches: dict[str, Callable], t: float = 0.55) -> Bundle:
    """Run EVERY live region's branch. No choosing. Choosing is collapse,
    and collapse is someone else's explicit, priced act."""
    w = {
        "true":         max(0.0,  e.gc),
        "false":        max(0.0, -e.gc),
        "inconsistent": max(0.0,  e.gct),
        "paracomplete": max(0.0, -e.gct),
    }
    w["blur"] = max(0.0, 1.0 - max(w.values()))
    outcomes = []
    for region, weight in w.items():
        if weight > 0.05 and region in branches:
            outcomes.append((region, weight, branches[region](e)))
    return Bundle(outcomes)

def collapse(b: Bundle, reason: str):
    """Explicit, priced collapse. The discarded outcomes get a receipt."""
    if not b.outcomes:
        return Gap("collapse of an empty bundle: nothing was live")
    kept = max(b.outcomes, key=lambda o: o[1])
    discarded = [(r, w) for r, w, _ in b.outcomes if r != kept[0]]
    RESIDUE_LEDGER.append(dict(kept=kept[0], kept_weight=kept[1],
                               discarded=discarded, reason=reason))
    return kept[2]

cannot("declare a collapsed branch 'right'",
       "only which was chosen, why, and what it cost; rightness would require "
       "the view from outside all perspectives, which no observer has", "theorem")

# ---------------------------------------------------------------- Layer 6
class Necessity:
    """Meters blur pressure; when a carving fails often enough HERE,
    proposes genesis: new vocabulary seeded from the gap."""
    def __init__(self, threshold: int = 3):
        self.threshold = threshold
        self.pressure: dict[str, list] = {}
        choose("genesis threshold", f"{threshold} blur events",
               "eager (a word per confusion) or shy (blur normalized, chronic)",
               "the eager/shy dial is a value judgment, not a neutral constant")
    def observe(self, predicate: str, e: Ev) -> Optional[Gap]:
        if e.verdict() == "blur":
            cases = self.pressure.setdefault(predicate, [])
            cases.append(e)
            if len(cases) >= self.threshold:
                return Gap(f"vocabulary insufficiency: predicate {predicate!r} "
                           f"blurred {len(cases)} times; single axis inadequate")
        return None

# ---------------------------------------------------------------- Layer 7
def ask_self(question: str):
    """Lawful self-description: forced limits are POINTED AT, with reasons."""
    q = question.lower()
    if "consisten" in q:
        return Gap("own consistency: unprovable from inside if actually consistent "
                   "(Godel II)", ("filed in HORIZON",))
    if "truth" in q and ("own" in q or "self" in q or "these sentences" in q):
        return Gap("own truth predicate: no language contains one (Tarski); "
                   "interpretation is legal, truth is not", ("filed in HORIZON",))
    if "halt" in q:
        return Gap("halting of arbitrary code: undecidable (Turing)",
                   ("filed in HORIZON",))
    if "cannot say" in q and "everything" in q:
        return Gap("the horizon of the horizon: the register of incapacities "
                   "cannot itself be complete", ("the last entry points past itself",))
    return Anomaly("unparsed self-question", "ask_self",
                   ("this anomaly is informational: the self-model's vocabulary "
                    "did not cover your question -- blur pressure on ask_self",))

for _c in [("own consistency is provable here", "Godel II", "theorem"),
           ("a truth predicate for this language exists in it", "Tarski", "theorem"),
           ("halting of arbitrary lucky code is decidable", "Turing/Rice", "theorem")]:
    cannot(*_c)
cannot("everything this system cannot say is listed",
       "the horizon recedes; this entry points past itself", "theorem")
