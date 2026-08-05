"""
lucky3 -- absorption revision. Three structures taken from the Etau/LPA2v
tradition (EAILAB-IFSP Paraconsistent-Lib, audited in comparisons/04),
each with a birth record naming its source:

  1. The 12-region interior : direction-of-tendency inside blur.
     Our single 'blur' region was flatter than their vocabulary; a blur
     that leans toward true-away-from-conflict is now sayable.
  2. Radial certainty        : distance-to-apex as a second sensitivity
     axis. v1's flip distance says how far the verdict is from changing;
     apex distance says how far the evidence is from IDEAL. Coordinates
     AND bearings.
  3. Asymmetric thresholds   : different strictness for entering the true
     region vs. the false region (their VlV/VlF, decision-theoretically
     sound: the two mistakes cost differently). Registered, not buried.

What we deliberately do NOT absorb (registered below): their
decision_output (unpriced collapse merging conflict and ignorance at the
exit); their silent input clamping; their origin-less intake. Absorption
is selective, and the selection has receipts.

Extends lucky1; Session gains an explore that understands tendencies.
"""
from lucky1 import (Ev, Testimony, Gap, Anomaly, Bundle, Session, q,
                    choose, cannot, CHOICES, HORIZON, LIVENESS, testify)
from dataclasses import dataclass
from typing import Callable, Optional
import math

# ---------------------------------------------------------------- births
choose("12-region verdict interior (absorbed)",
       "inside blur, report tendency: which certainty pole (toward-true / "
       "toward-false) and which knowledge pole (toward-conflict / "
       "toward-ignorance) the evidence leans to, plus which dimension "
       "dominates -- adapted from LPA2v's quasi-region vocabulary "
       "(Qt->conflict, Q-conflict->t, ...); birth record: comparisons/04, "
       "EAILAB-IFSP Paraconsistent-Lib (open source)",
       "our v1 flat blur (their interior showed it was needlessly coarse); "
       "their exact 12 labels (their glyph vocabulary encodes MATLAB parity "
       "constraints we do not carry)",
       "tendencies are reported ONLY inside blur: within settled regions "
       "they would be noise on top of a verdict already carrying flip data")

choose("radial (apex) certainty (absorbed)",
       "each verdict carries apex_distance: normalized distance from the "
       "evidence point to the nearest ideal corner -- pure-support (1,0) or "
       "pure-counter (0,1); birth record: comparisons/04, their d/dcr "
       "geometry, sqrt(2)/2 normalization noted as their convention",
       "edge-only sensitivity (v1: how close to flipping, but not how far "
       "from ideal); their dcr sign convention folded into dc (we keep the "
       "axes separate)",
       "two sensitivity axes can disagree: evidence can sit robustly inside "
       "'true' (large flip distance) while far from ideal support (large "
       "apex distance). Both are now visible; readers must learn to read two "
       "numbers where they wanted one -- a priced honesty gain")

choose("asymmetric region thresholds (absorbed)",
       "four independent entry thresholds: t_true, t_false, t_conflict, "
       "t_ignorance (defaults all 0.55 = v1 behavior preserved); birth "
       "record: comparisons/04, their VlV/VlF bias knobs -- absorbed WITH "
       "registration, which their library lacked",
       "one threshold for all edges (v1: assumes accepting support and "
       "accepting counter-support cost the same mistake, which is false in "
       "most deployments); their auto-derived VSSC/VICC coupling (hidden "
       "arithmetic between knobs; ours are independent and visible)",
       "asymmetry is power: a caller can now tilt the carving. The tilt is "
       "in the verdict's own report, so a tilted verdict cannot pose as a "
       "neutral one")

choose("what was NOT absorbed",
       "their decision_output (3-valued exit merging conflict-0.5 with "
       "ignorance-0.5, no receipt), their silent input clamping, their "
       "origin-less bare-float intake",
       "wholesale absorption (would have imported the exact unpriced "
       "collapse Lucky exists to refuse)",
       "selective absorption is itself a carving of their work; this entry "
       "is its receipt, and comparisons/04 is its justification")

cannot("clamp an impossible input silently",
       "an input outside [0,1] is testimony about the CALLER (a scaling "
       "mistake, a broken sensor model); repairing it hides that testimony. "
       "lucky3 returns an informational anomaly carrying the raw values",
       "choice")

# ---------------------------------------------------------------- thresholds
@dataclass(frozen=True)
class Carving:
    """Four independent entry thresholds. Defaults reproduce v1 exactly."""
    t_true: float = 0.55
    t_false: float = 0.55
    t_conflict: float = 0.55
    t_ignorance: float = 0.55
    def tilted(self) -> bool:
        return len({self.t_true, self.t_false, self.t_conflict,
                    self.t_ignorance}) > 1

DEFAULT_CARVING = Carving()

# ---------------------------------------------------------------- verdict3
SQRT_HALF = math.sqrt(0.5)   # their normalization convention, kept and named

@dataclass(frozen=True)
class Verdict3:
    region: str               # true | false | inconsistent | paracomplete | blur
    flip_distance: float      # v1 axis: nearest region change (edge geometry)
    apex_distance: float      # absorbed axis: distance from nearest ideal corner
    tendency: Optional[str]   # inside blur only: e.g. "toward-true/toward-conflict (certainty-led)"
    carving: Carving          # the thresholds that produced this verdict
    def __repr__(self):
        t = f" ~{self.tendency}" if self.tendency else ""
        tilt = " [tilted carving]" if self.carving.tilted() else ""
        return (f"{self.region}(flip@{self.flip_distance:.2f}, "
                f"apex@{self.apex_distance:.2f}){t}{tilt}")

def _apex_distance(mu: float, lam: float) -> float:
    d_support = math.hypot(1.0 - mu, lam)        # to pure-support (1,0)
    d_counter = math.hypot(mu, 1.0 - lam)        # to pure-counter (0,1)
    return q(min(d_support, d_counter) / (2 * SQRT_HALF))  # normalized to [0,1]

def _tendency(gc: float, gct: float) -> str:
    c_pole = "toward-true" if gc >= 0 else "toward-false"
    k_pole = "toward-conflict" if gct >= 0 else "toward-ignorance"
    if abs(gc) > abs(gct):   lead = "certainty-led"
    elif abs(gct) > abs(gc): lead = "knowledge-led"
    else:                    lead = "balanced"
    return f"{c_pole}/{k_pole} ({lead})"

def verdict3(e: Ev, carving: Carving = DEFAULT_CARVING) -> Verdict3:
    gc, gct = e.gc, e.gct
    edges = {
        "true":         q(gc  - carving.t_true),
        "false":        q(-gc - carving.t_false),
        "inconsistent": q(gct - carving.t_conflict),
        "paracomplete": q(-gct - carving.t_ignorance),
    }
    inside = [r for r, d in edges.items() if d >= 0]
    if inside:
        region = max(inside, key=lambda r: edges[r])
        flip, tend = edges[region], None
    else:
        region = "blur"
        flip = q(min(carving.t_true - gc, carving.t_false + gc,
                     carving.t_conflict - gct, carving.t_ignorance + gct))
        tend = _tendency(gc, gct)
    return Verdict3(region, q(flip), _apex_distance(e.mu, e.lam), tend, carving)

# ---------------------------------------------------------------- intake
def testify3(*ts: Testimony, combine: str = "max"):
    """Intake that POINTS at impossible weights instead of repairing them."""
    bad = [t for t in ts if not (0.0 <= t.weight <= 1.0)]
    if bad:
        return Anomaly(
            "impossible testimony weight", "testify3",
            tuple(f"{t.source!r}: weight={t.weight} outside [0,1] -- "
                  "testimony about the caller, not repaired" for t in bad))
    return testify(*ts, combine=combine)

# ---------------------------------------------------------------- session3
class Session3(Session):
    """v1 Session with tendency-aware exploration. Blur branches may now
    dispatch on tendency; pressure keys gain the tendency string, so genesis
    proposals name not just the neighborhood but the LEAN of the confusion."""
    def __init__(self, carving: Carving = DEFAULT_CARVING):
        super().__init__()
        self.carving = carving

    def explore3(self, e: Ev, branches: dict[str, Callable]) -> Bundle:
        v = verdict3(e, self.carving)
        b = self.explore(e, branches)      # v1 weights and purity checks
        if v.region == "blur" and v.tendency:
            key = f"blur:{v.tendency.split(' ')[0]}"       # e.g. blur:toward-true/toward-conflict
            if key in branches:
                b.outcomes.append((key, q(max(w for _, w, _ in b.outcomes) * 0.5
                                          if b.outcomes else 0.5),
                                   branches[key](e)))
        return b

    def observe3(self, predicate: str, e: Ev) -> Optional[Gap]:
        v = verdict3(e, self.carving)
        if v.region != "blur":
            return None
        key = (predicate, round(e.gc, 1), round(e.gct, 1), v.tendency)
        cases = self.pressure.setdefault(key, [])
        cases.append(e)
        if len(cases) >= 3:
            return Gap(f"vocabulary insufficiency: {predicate!r} blurred "
                       f"{len(cases)} times, leaning {v.tendency}; "
                       "this axis fails HERE, in THIS direction")
        return None
