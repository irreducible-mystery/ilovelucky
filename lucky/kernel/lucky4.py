"""
lucky4 -- revision forced by the six-experiment suite (comparisons/05).

Four structures, each with a birth record naming the finding that forced it:

  1. DECLARED ENCODINGS : the world->weight mapping becomes a visible slot.
     Undeclared encodings are marked and counted, never repaired -- the
     laundering point between world and number is now a place the kernel
     can point at. (critique A: five defensible encodings of the same
     data, five different verdicts.)
  2. EVIDENCE MASS      : balance and volume are no longer conflated. A
     balanced verdict from two testimonies and one from ten thousand now
     look different. (critique F: Keynes's weight of evidence is
     unstatable on the lattice.)
  3. ITERATION          : self-referential updates may settle OR orbit.
     A cycle is a first-class result, not a failure; convergence claims
     carry the damping that produced them. (critique C's revenge Liar has
     NO fixed point -- a 2-cycle IS its answer; the paradox suite's
     "containment" was manufactured by unconfessed smoothing.)
  4. FRAMES             : contradiction that exists only under
     index-collapsing fusion is a fact about the fusion, not the claims.
     Cross-frame fusion is priced and permanently marked; declared
     non-fusable frames return an anomaly instead of a superobserver.
     (black hole complementarity + polysemy: the same quarantine shape
     in two unrelated domains.)

Extends lucky3 (which extends lucky1). Nothing is patched in place.
"""
from lucky1 import (Ev, Testimony, Gap, Anomaly, Session, q,
                    choose, cannot, CHOICES, HORIZON, testify)
from lucky3 import Session3, verdict3, Carving, DEFAULT_CARVING, testify3
from dataclasses import dataclass
from typing import Callable, Optional
import copy as _copy

# ================================================== 1. DECLARED ENCODINGS
choose("encoding declaration",
       "a testimony may carry an encoding: a statement of how the world "
       "became this number. Undeclared encodings are marked in the trail "
       "and counted on the case file, never rejected and never repaired",
       "rejecting undeclared encodings (pushes the laundering upstream, "
       "out of sight); standardizing encoding recipes (blesses one "
       "world->number mapping as if the choice were not a choice)",
       "the mapping from world to weight cannot be validated from inside "
       "the kernel -- GIGO is not solved, it is made visible; a verdict "
       "built on undeclared encodings says so, and that is all it can do")

@dataclass(frozen=True)
class Sworn(Testimony):
    """A testimony that declares how its weight was produced."""
    encoding: str = ""

def testify4(*ts: Testimony, combine: str = "max"):
    """Intake with encoding accounting on top of v3's range pointing."""
    result = testify3(*ts, combine=combine)
    if isinstance(result, Anomaly):
        return result
    undeclared = [t.source for t in ts
                  if not (isinstance(t, Sworn) and t.encoding)]
    if undeclared:
        result.trail += (f"undeclared-encodings:{len(undeclared)}/{len(ts)} "
                         f"({', '.join(undeclared)})",)
    else:
        result.trail += (f"all-encodings-declared:{len(ts)}",)
    return result

def encodings_of(e: Ev) -> dict:
    """Read the encoding ledger of a case file from its trail."""
    declared = {t.source: t.encoding for t in e.trail
                if isinstance(t, Sworn) and t.encoding}
    undeclared = [t.source for t in e.trail
                  if isinstance(t, Testimony)
                  and not (isinstance(t, Sworn) and t.encoding)]
    return {"declared": declared, "undeclared": tuple(undeclared)}

# ================================================== 2. EVIDENCE MASS
choose("evidence mass",
       "mass(e) = the count of testimonies retained in the trail; surfaced "
       "next to the verdict so balance and volume are distinguishable",
       "a calibrated weight-of-evidence measure (requires a model of "
       "testimony quality we do not have); hiding volume entirely (v1-v3, "
       "now known to conflate 1-vs-1 with 5000-vs-5000)",
       "mass is a count, not a measure: it does not compare across "
       "combination modes, it counts a rumor and a meta-analysis alike, "
       "and mass under 'max' combination changes nothing in the verdict -- "
       "it only stops the thinness of evidence from being invisible")

def mass(e: Ev) -> int:
    return sum(1 for t in e.trail if isinstance(t, Testimony))

def describe(e: Ev) -> str:
    """A reported state that keeps its volume and encoding receipts."""
    enc = encodings_of(e)
    return (f"{e!r} mass={mass(e)} "
            f"encodings[declared={len(enc['declared'])}, "
            f"undeclared={len(enc['undeclared'])}]")

# ================================================== 3. ITERATION
choose("iteration outcomes",
       "iterate() watches a self-referential update for BOTH fixed points "
       "and orbits: Settled carries the steps taken and any damping used "
       "(confessed in the result); Cycle carries the period and the orbit "
       "itself as a first-class, final answer",
       "forcing convergence with hidden smoothing (manufactures a center "
       "fixed point and calls the paradox 'contained'); treating "
       "non-convergence as error (a stable orbit is information, not "
       "failure); infinite iteration (never returns anything at all)",
       "some questions answer in oscillations: the revenge sentence about "
       "its own lattice position has no fixed point at any damping short "
       "of the one that erases the question; a kernel that never "
       "prematurely collapses must be able to hand back the orbit")

@dataclass(frozen=True)
class Settled:
    point: tuple                # (mu, lam)
    steps: int
    damping: float              # confessed: 0.0 means the map itself settled
    def __repr__(self):
        d = f", damping={self.damping}" if self.damping else ""
        return f"Settled(({self.point[0]:.4f},{self.point[1]:.4f}) in {self.steps} steps{d})"

@dataclass(frozen=True)
class Cycle:
    period: int
    orbit: tuple                # ((mu,lam), ...) length == period
    entered_at: int
    damping: float
    def __repr__(self):
        pts = " -> ".join(f"({m:.2f},{l:.2f})" for m, l in self.orbit)
        return f"Cycle(period={self.period}: {pts}, entered@{self.entered_at})"

def iterate(step: Callable[[float, float], tuple], mu: float, lam: float,
            damping: float = 0.0, max_steps: int = 1000):
    """Run (mu,lam) -> step(mu,lam), blended by the CONFESSED damping:
    next = (1-damping)*step + damping*current. Returns Settled, Cycle,
    or a Gap if the budget ends with neither."""
    seen = {}                             # quantized point -> first index
    cur = (q(mu), q(lam))
    for i in range(max_steps):
        if cur in seen:
            start = seen[cur]
            orbit, p = [], cur
            while True:
                orbit.append(p)
                nm, nl = step(*p)
                p = (q((1-damping)*nm + damping*p[0]),
                     q((1-damping)*nl + damping*p[1]))
                if p == cur:
                    break
            if len(orbit) == 1:
                return Settled(cur, start, damping)
            return Cycle(len(orbit), tuple(orbit), start, damping)
        seen[cur] = i
        nm, nl = step(*cur)
        nxt = (q((1-damping)*nm + damping*cur[0]),
               q((1-damping)*nl + damping*cur[1]))
        if nxt == cur:
            return Settled(cur, i, damping)
        cur = nxt
    return Gap("iteration budget exhausted without settlement or orbit",
               (f"{max_steps} steps, damping={damping}; the process may be "
                "aperiodic at this precision, or the budget too small -- "
                "the kernel cannot tell which from here",))

# ================================================== 4. FRAMES
choose("frame quarantine",
       "evidence may carry a frame (an index: observer, context, stratum). "
       "Fusing across frames is a priced act filed in the ledger; the "
       "fused trail is permanently marked index-collapsed. Frames declared "
       "non-fusable return an informational anomaly instead of a result",
       "forbidding all cross-frame fusion (some merges are legitimate and "
       "the ban would be dodged by stripping frames); allowing silent "
       "fusion (v1-v3: the superobserver forgery -- contradiction "
       "manufactured at the merge, billed to the claims)",
       "the kernel cannot know WHICH fusions are illegitimate; physics "
       "forbids the black-hole superobserver, grammar disambiguates the "
       "homonym, and neither rule is derivable from the annotations -- "
       "non-fusability is testimony from outside, recorded like all of it")

_NON_FUSABLE: dict = {}          # frozenset({f1,f2}) -> why

def forbid_fusion(frame_a: str, frame_b: str, why: str):
    _NON_FUSABLE[frozenset((frame_a, frame_b))] = why

def framed(e: Ev, frame: str) -> Ev:
    return Ev(e.mu, e.lam, e.trail + (f"frame:{frame}",))

def frame_of(e: Ev) -> Optional[str]:
    for item in reversed(e.trail):
        if isinstance(item, str) and item.startswith("frame:"):
            return item[6:]
    return None

def fuse_frames(session: Session, a: Ev, b: Ev, reason: str, mode: str = "accept_all"):
    """Cross-frame fusion: priced, marked, refusable."""
    fa, fb = frame_of(a), frame_of(b)
    if fa is None or fb is None or fa == fb:
        return getattr(a, mode)(b)        # same frame or unframed: ordinary combination
    key = frozenset((fa, fb))
    if key in _NON_FUSABLE:
        return Anomaly("fusion across non-fusable frames", "fuse_frames",
                       (f"{fa!r} + {fb!r}: {_NON_FUSABLE[key]}",
                        "each frame remains individually consultable; "
                        "no superobserver exists to hold the merge"))
    fused = getattr(a, mode)(b)
    fused.trail += (f"index-collapsed:{fa}+{fb}",)
    session.ledger.append(dict(
        kept=f"fusion({fa}+{fb})", kept_weight=1.0,
        discarded=[(f"frame-separation:{fa}|{fb}", 1.0)],
        purity_notes=0, reason=f"cross-frame fusion: {reason}"))
    v = fused.verdict()
    if v.region == "inconsistent":
        fused.trail += ("conflict-manufactured-at-merge: this contradiction "
                        "carries the receipt of the fusion that made it",)
    return fused

# ================================================== horizon confessions
cannot("escape the classical substrate",
       "every verdict boundary in this kernel is a bivalent float "
       "comparison in a bivalent host language; the kernel DESCRIBES "
       "graded, conflicted, unsettled states in a substrate that is none "
       "of those things. The description layer and the substrate layer "
       "must not be confused; the kernel's honesty lives entirely in the "
       "description layer", "substrate")

cannot("state conditionals",
       "annotations attach to claims, not to entailments between claims; "
       "there is no implication here and so no modus ponens and so no "
       "Curry collapse -- an immunity by poverty, not by therapy. If a "
       "conditional is ever grown, contraction is the hidden decision "
       "that must be priced at birth", "choice")

cannot("measure counterfeit distance without the actual state",
       "every exit surface (repr, digest, describe) is a REPORTED state; "
       "the gap between reported and actual is measurable only where the "
       "actual is retained. Trails are that retention -- discarding a "
       "trail is an epistemic decision, not a compression decision",
       "structure")

cannot("tune carvings by outcome feedback without a declared objective",
       "selection pressure that penalizes blur verdicts will drain the "
       "honest-ignorance region and manufacture certainty exactly where "
       "no correctness signal reaches; any future threshold tuning must "
       "register its objective next to the Carving it tunes", "choice")

# ================================================== session4
class Session4(Session3):
    """Session3 plus frame-aware ledger access; fuse() delegates to the
    priced cross-frame fusion above."""
    def fuse(self, a: Ev, b: Ev, reason: str, mode: str = "accept_all"):
        return fuse_frames(self, a, b, reason, mode)
