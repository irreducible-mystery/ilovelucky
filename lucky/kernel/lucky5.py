"""
lucky5 -- the uniform intake discipline. Forced by v4's own field notes
(design/06 §6): the encoding critique regresses onto its cure. v4 taught
ONE doorway (testimony weights) to ask "where did you come from?" while
its own new doorways -- frame labels, fusion bans, damping constants --
admit values from the world with no stated origin. v5 teaches the
building, not the door:

  1. ONE REGISTER, ALL DOORS : every value entering from the world passes
     through Session5.take(slot, value, origin). Declared origins are
     recorded; anonymous arrivals are recorded AS anonymous -- marked,
     counted, never repaired, never refused. The session can always
     answer: "what did the world tell you, and what arrived nameless?"
  2. ARRIVAL ORDER IS A FACT : the register preserves the sequence in
     which the world spoke. Kernel combiners never consult it (they are
     order-independent); any future reader that DOES consult order must
     cite the sequence numbers it used. Order becomes a receipt, not a
     hidden influence.
  3. ORDER-BLINDNESS IS CHECKED, NOT ASSUMED : order_audit() runs a
     combination under shuffled arrival orders and reports whether the
     position moved. v4 registered "combiners must be associative" as a
     written rule; v5 makes the rule executable. (Forced by critique E,
     where Etau's fusion answer depends on an undeclared grouping tree --
     and by the observation that even READING a batch of documents is an
     intake whose order can tilt the verdict.)

Extends lucky4. Nothing is patched in place.
"""
from lucky1 import Ev, Testimony, Gap, Anomaly, q, choose, cannot, HORIZON
from lucky4 import (Session4, Sworn, testify4, iterate, Settled, Cycle,
                    framed, frame_of, forbid_fusion, fuse_frames, mass,
                    encodings_of)
from dataclasses import dataclass
from typing import Callable, Optional
import itertools
import random as _random

# ================================================== 1. THE REGISTER
choose("uniform intake register",
       "every world-value enters through take(slot, value, origin): frame "
       "labels, fusion bans, damping constants, carving thresholds, and "
       "(bridged) testimony encodings all file in ONE sequenced register; "
       "anonymous arrivals are admitted and marked, never repaired",
       "per-doorway disciplines (v4: one honest door in a porous building); "
       "refusing anonymous values (pushes the laundering upstream -- the "
       "caller invents an origin to get past the door, which is worse); "
       "validating stated origins (the kernel cannot check the world's "
       "word about the world; a stated origin is testimony, not proof)",
       "the register makes anonymity VISIBLE, not impossible: a session "
       "built entirely on nameless intake still runs -- it just can no "
       "longer pass as a session built on declared ground")

@dataclass(frozen=True)
class Origin:
    stated: str                  # how the world became this value
    by: str = ""                 # who states it (optional)
    def __repr__(self):
        who = f" (per {self.by})" if self.by else ""
        return f"Origin({self.stated!r}{who})"

class Session5(Session4):
    """Session4 plus the intake register. All v5 doorways route here."""
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.intakes: list[dict] = []

    def take(self, slot: str, value, origin: Optional[Origin] = None):
        """The single doorway. Returns the value unchanged; the RECORD is
        the discipline."""
        self.intakes.append(dict(
            seq=len(self.intakes), slot=slot, value=repr(value),
            origin=origin))
        return value

    def intake_report(self) -> dict:
        declared = [i for i in self.intakes if i["origin"] is not None]
        anon = [i for i in self.intakes if i["origin"] is None]
        return dict(
            total=len(self.intakes),
            declared=len(declared),
            anonymous=len(anon),
            anonymous_slots=tuple(i["slot"] for i in anon),
            note=("this session can pass as declared-ground" if not anon
                  else "this session rests partly on nameless intake"))

    # ------- v5 doorways (each an existing act, now routed through take)
    def framed5(self, e: Ev, frame: str, origin: Optional[Origin] = None) -> Ev:
        self.take(f"frame:{frame}", frame, origin)
        out = framed(e, frame)
        if origin is None:
            out.trail += (f"frame-origin-unknown:{frame}",)
        return out

    def forbid_fusion5(self, frame_a: str, frame_b: str, why: str,
                       origin: Optional[Origin] = None):
        self.take(f"fusion-ban:{frame_a}+{frame_b}", why, origin)
        tag = why if origin else why + " [ban origin unknown]"
        forbid_fusion(frame_a, frame_b, tag)

    def iterate5(self, step: Callable, mu: float, lam: float,
                 damping: float = 0.0,
                 damping_origin: Optional[Origin] = None,
                 max_steps: int = 1000):
        if damping:
            self.take("damping", damping, damping_origin)
        result = iterate(step, mu, lam, damping=damping, max_steps=max_steps)
        if damping and damping_origin is None and isinstance(result, Settled):
            # a convergence bought with a nameless constant says so
            return Settled(result.point, result.steps, result.damping), \
                   Anomaly("settlement produced by anonymous damping",
                           "iterate5",
                           (f"damping={damping} entered with no stated origin; "
                            "the fixed point below is real, but the CHOICE "
                            "that manufactured it is nameless",))
        return result

    def testify5(self, *ts: Testimony, combine: str = "max"):
        """Bridge: v4's per-testimony encodings file into the register,
        so the session's intake story is complete in one place."""
        for t in ts:
            enc = t.encoding if isinstance(t, Sworn) and t.encoding else None
            self.take(f"testimony:{t.source}", t.weight,
                      Origin(enc, by=t.source) if enc else None)
        return testify4(*ts, combine=combine)

# ================================================== 2. ORDER AS RECEIPT
choose("arrival order retention",
       "the register keeps the sequence in which the world spoke; kernel "
       "combiners never consult it, and any future reader that does must "
       "cite the sequence numbers it used",
       "discarding order (erases a fact -- a correction read before its "
       "target reads as prophecy, after it as repair; the difference is "
       "real even when the combined position is identical); letting order "
       "silently influence combination (critique E's grouping-tree defect, "
       "generalized)",
       "order-as-receipt only protects readings that go THROUGH the "
       "kernel; a human or model reading raw documents in upload order is "
       "an intake the register cannot see")

# ================================================== 3. THE EXECUTABLE RULE
choose("order-blindness audit",
       "order_audit() re-runs a combination under shuffled arrival orders "
       "and compares positions; agreement is EVIDENCE of order-blindness "
       "for these inputs, disagreement is PROOF of order-sensitivity",
       "trusting the associativity of registered combiners (true today, "
       "unenforced tomorrow -- v4 admitted the immunity was luck); "
       "proving associativity formally (the substrate is floating-point, "
       "where even addition is not exactly associative)",
       "the audit samples permutations; passing it bounds nothing -- it "
       "is a tripwire, not a theorem, and says so in its result")

def order_audit(ts: list, combine: str = "max", trials: int = 6,
                seed: int = 0) -> dict:
    """Shuffle arrival order; report whether the position moves."""
    rng = _random.Random(seed)
    base = testify4(*ts, combine=combine)
    if isinstance(base, Anomaly):
        return dict(order_blind=None, note="intake anomaly precedes audit",
                    anomaly=base)
    positions = {(base.mu, base.lam)}
    for _ in range(trials):
        shuffled = ts[:]
        rng.shuffle(shuffled)
        e = testify4(*shuffled, combine=combine)
        positions.add((e.mu, e.lam))
    return dict(
        order_blind=(len(positions) == 1),
        distinct_positions=len(positions),
        trials=trials,
        note=("tripwire passed: no order sensitivity FOUND (not proven "
              "absent)" if len(positions) == 1 else
              "order sensitivity PROVEN: the combiner consults arrival "
              "order and must cite it or be retired"))

# ================================================== horizon
cannot("register its own reading order",
       "the register sequences what enters a SESSION; the acts that built "
       "this kernel -- which documents were read first, which critique "
       "was absorbed before which -- happened outside any session and "
       "left order-receipts only in prose (field notes, commit history). "
       "The kernel's own genesis is anonymous intake by its own standard",
       "structure")

cannot("verify a stated origin",
       "an Origin is the world's testimony about the world; the register "
       "records it and can never check it. A false origin passes as "
       "declared ground -- the discipline converts silent laundering into "
       "on-record assertion, which is an improvement in accountability, "
       "not in truth", "structure")
