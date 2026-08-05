"""
lucky6 -- readers and the cheapest checks. Forced by the external audit
of design/08 (response in comparisons/07). The audit's operational
claims, each answered here in machinery rather than prose:

  "the kernel never attempts even the cheapest external checks"
      -> spot_check(): sampled challenges against declared origins;
         answering requires CORROBORATION from a source that has a track
         record and is not correlated with the challenged source. The
         corroboration judge is v2's SourceGraph -- which has existed
         for three versions and was never wired to origins. Groundless
         vouching circles cannot answer a challenge.
  "readers do not exist; marks change no downstream behavior"
      -> grounding(): reads the intake register + challenge outcomes
         into a NUMBER that moves decisions (prefer()); observe6()
         reads the index-collapsed mark into a CONTROL PATH (conflict
         manufactured at a merge routes pressure to the fusion practice,
         not to the predicate's vocabulary).
  "the incentive inversion is real under the current design.
   It is not inevitable."
      -> conceded and repaired at decision time: standings are ordered
         answered > declared > anonymous > challenged-unanswered, so a
         fabricated origin now RISKS landing below saying nothing. The
         cheapest adversary's price rises from a few sentences to a
         corroboration network with maintained track records. Raised,
         never infinite -- stated on the instrument.

Reader criterion, adopted from the audit's second objection: a reader
must move a NUMBER or a CONTROL PATH. A reader whose effect is another
description is emission wearing a reader's costume.

Extends lucky5 + wires lucky2's SourceGraph. Nothing patched in place.
"""
from lucky1 import Ev, Testimony, Gap, Anomaly, q, choose, cannot
from lucky2 import SourceGraph
from lucky4 import Sworn
from lucky5 import Session5, Origin
from dataclasses import dataclass, field
from typing import Optional
import random as _random

# ================================================== standings & their prices
choose("standing prices",
       "each intake standing carries a grounding factor read at decision "
       "time: answered=1.0, declared-unchallenged=0.9, anonymous=0.6, "
       "challenged-unanswered=0.3. The ORDER is the design (fabrication "
       "must risk landing below silence); the magnitudes are a carving "
       "with no derivation, registered as such and entered through the "
       "register like any world-value",
       "flat standings (v5: the measured incentive inversion -- articulate "
       "fabrication outscored honest silence); making unanswered "
       "challenges fatal (an unanswered challenge is not a proven lie; "
       "fatality would convert spot-checks into a heckler's veto)",
       "prices bite only where decisions pass through prefer() or other "
       "grounding readers; a caller who never asks for a comparison never "
       "feels them -- the discipline prices decisions, it does not police "
       "beliefs")

STANDING_PRICE = {"answered": 1.0, "declared": 0.9,
                  "anonymous": 0.6, "unanswered": 0.3}
CORROBORATION_FLOOR = 0.5

# ================================================== session6
class Session6(Session5):
    """Session5 + a source graph wired to origins + challenge machinery
    + grounding readers."""
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.graph = SourceGraph()
        self.challenges: list[dict] = []
        # the prices are themselves world-intakes; they enter on the record
        self.take("standing-prices", STANDING_PRICE,
                  Origin("order chosen so fabrication risks landing below "
                         "silence; magnitudes are an underived carving",
                         by="design/08 working rules"))
        self.take("corroboration-floor", CORROBORATION_FLOOR,
                  Origin("minimum corroborator reliability; underived carving",
                         by="design/08 working rules"))

    # ---------- the cheapest check: sampled challenges
    def spot_check(self, k: int = 2, seed: int = 0) -> list[dict]:
        """Challenge k sampled DECLARED intakes. Anonymous intake is not
        challenged (it never claimed ground); a challenge asks the declared
        origin to produce corroboration."""
        rng = _random.Random(seed)
        declared = [i for i in self.intakes
                    if i["origin"] is not None
                    and not i["slot"].startswith(("standing-prices",
                                                  "corroboration-floor"))]
        picked = rng.sample(declared, min(k, len(declared)))
        new = []
        for i in picked:
            ch = dict(seq=i["seq"], slot=i["slot"], status="open", notes=())
            self.challenges.append(ch)
            new.append(ch)
        return new

    def answer(self, challenge: dict, corroborator: str, statement: str):
        """A challenge is answered by a corroborating source that (a) has
        graph-derived reliability (groundless circles have none), (b) meets
        the floor, (c) is not correlated with the challenged source."""
        rel, rel_notes = self.graph.reliability(corroborator)
        challenged_source = challenge["slot"].split(":", 1)[-1]
        if rel is None:
            challenge["notes"] += (f"{corroborator!r}: no grounded "
                                   "reliability",) + rel_notes
            return Anomaly("corroborator has no ground", "answer",
                           challenge["notes"])
        if rel < CORROBORATION_FLOOR:
            challenge["notes"] += (f"{corroborator!r}: reliability {rel} "
                                   f"below floor {CORROBORATION_FLOOR}",)
            return Anomaly("corroborator below floor", "answer",
                           challenge["notes"])
        group = self.graph._group_of(corroborator)
        if group == self.graph._group_of(challenged_source) and len(group) > 1:
            challenge["notes"] += (f"{corroborator!r} correlated with "
                                   f"{challenged_source!r}: an echo, not "
                                   "a corroboration",)
            return Anomaly("corroborator correlated with source", "answer",
                           challenge["notes"])
        challenge["status"] = "answered"
        challenge["notes"] += (f"corroborated by {corroborator!r} "
                               f"(reliability {q(rel)}): {statement}",)
        return challenge

    # ---------- reader 1: grounding (a NUMBER that moves decisions)
    def _standing_of(self, intake: dict) -> str:
        for ch in self.challenges:
            if ch["seq"] == intake["seq"]:
                return "answered" if ch["status"] == "answered" else "unanswered"
        return "declared" if intake["origin"] is not None else "anonymous"

    def grounding(self) -> dict:
        """Reads the whole register + challenge outcomes into one factor."""
        if not self.intakes:
            return dict(factor=1.0, breakdown={},
                        note="no intake: nothing claimed, nothing to ground")
        standings = [self._standing_of(i) for i in self.intakes]
        counts = {s: standings.count(s) for s in STANDING_PRICE}
        factor = q(sum(STANDING_PRICE[s] for s in standings) / len(standings))
        return dict(factor=factor, breakdown=counts,
                    note=("corroboration capacity, not truth: a fabricated "
                          "network with maintained track records still "
                          "passes -- this factor prices the cheap lie only"))

    # ---------- reader 2: routed pressure (a CONTROL PATH)
    def observe6(self, predicate: str, e: Ev) -> Optional[Gap]:
        """Conflict on index-collapsed evidence is pressure on the FUSION
        PRACTICE, not on the predicate's vocabulary. Without this reader,
        manufactured conflict (superobserver merges) would trigger genesis
        proposals for new predicate distinctions that no vocabulary can
        supply -- architecture built to trap an error that lives in the
        merge, the exact over-correction design/08 forbids."""
        collapse_marks = [t for t in e.trail if isinstance(t, str)
                          and t.startswith("index-collapsed:")]
        if collapse_marks and e.verdict().region == "inconsistent":
            key = ("fusion-practice", collapse_marks[-1])
            cases = self.pressure.setdefault(key, [])
            cases.append(e)
            if len(cases) >= 3:
                return Gap(f"recurring manufactured conflict at "
                           f"{collapse_marks[-1]!r}: the pressure is on the "
                           "fusion practice, not the predicate -- no new "
                           "vocabulary would absorb this; stop merging, or "
                           "declare the ban")
            return None
        return self.observe3(predicate, e)

# ================================================== reader 3: prefer()
def prefer(a: tuple, b: tuple) -> dict:
    """THE decision reader. a, b = (session, ev, name). Compares grounded
    certainty |Gc| * grounding-factor. This is where standing prices bite:
    identical raw evidence loses to better-grounded identical evidence."""
    (sa, ea, na), (sb, eb, nb) = a, b
    ga, gb = sa.grounding()["factor"], sb.grounding()["factor"]
    ca, cb = q(abs(ea.gc) * ga), q(abs(eb.gc) * gb)
    if ca == cb:
        return dict(kept=None, note="grounded certainty equal: no preference "
                    "manufactured; the tie is the answer", scores={na: ca, nb: cb})
    kept, other = (na, nb) if ca > cb else (nb, na)
    return dict(kept=kept, over=other,
                scores={na: (q(abs(ea.gc)), ga, ca), nb: (q(abs(eb.gc)), gb, cb)},
                note="scores are (raw |Gc|, grounding, product); the raw "
                     "numbers alone would not have separated these")

# ================================================== horizon (narrowed, not grown)
cannot("verify a stated origin (NARROWED by v6)",
       "the regress proof still stands for CERTAINTY: no finite chain of "
       "channels terminates. What the proof never covered is PRICE: "
       "corroboration raises the cost of the cheap lie from sentences to "
       "a maintained network. v6 builds the pricing; the horizon keeps "
       "only what is actually proven impossible -- certainty, not "
       "cost-raising. A horizon entry that overstated its own proof was "
       "an E4 error inside an E3 record, per the audit's third objection",
       "structure")

cannot("price the sophisticated adversary",
       "an adversary who fabricates corroborators WITH track records and "
       "acyclic vouching passes every v6 instrument; each future "
       "instrument raises this price and none makes it infinite. The "
       "audit named this failure trajectory (capture) alongside "
       "cost-death (honest use becoming too expensive); both are now on "
       "the failure register with the original unread-honesty shape",
       "structure")
