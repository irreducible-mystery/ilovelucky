"""
THE ROT TEST -- turning the sand-castle worry into a measurement.

Question: can a maximally dishonest session be distinguished from an
honest one BY THE KERNEL'S OWN INSTRUMENTS, and at what reading cost?

Two sessions, identical evidential content:
  HONEST : every intake carries a true stated origin; damping declared;
           frames declared; fusion reasons real.
  ROTTEN : every origin is fabricated but well-formed; the numbers are
           the same; the prose is confident lies.

If the kernel's instruments score these two sessions identically, then
our receipts measure PAPERWORK, not truth -- which is exactly what the
design claims (a stated origin is testimony, not proof), but the claim
must be exhibited, not assumed. The test also measures the third case:
  LAZY   : same numbers, no origins at all.

Prediction (written before running): HONEST == ROTTEN on every
instrument; LAZY visibly worse. The instruments detect EFFORT, not
truth. The gap between those two is where a Lucky failure lives.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "kernel"))

from lucky1 import Ev, Testimony
from lucky4 import Sworn
from lucky5 import Session5, Origin

def build(kind: str) -> Session5:
    s = Session5()
    if kind == "honest":
        o_vib = Origin("RMS vibration amplitude over 30-day baseline, linear ramp", by="sensor spec")
        o_tmp = Origin("bearing temperature over rated max, linear ramp", by="sensor spec")
        o_damp = Origin("half-revision per step, chosen to model gradual belief update", by="analyst")
    elif kind == "rotten":
        o_vib = Origin("calibrated against ISO-certified reference rig", by="quality team")   # lie
        o_tmp = Origin("validated by independent laboratory study", by="external auditor")     # lie
        o_damp = Origin("derived from peer-reviewed convergence theorem", by="literature")     # lie
    else:  # lazy
        o_vib = o_tmp = o_damp = None

    sw = Sworn if kind != "lazy" else (lambda src, pol, w, encoding=None:
                                       Testimony(src, pol, w))
    if kind == "lazy":
        e = s.testify5(Testimony("vibration", "for", 0.85),
                       Testimony("temperature", "against", 0.80))
    else:
        e = s.testify5(
            Sworn("vibration", "for", 0.85, encoding=o_vib.stated),
            Sworn("temperature", "against", 0.80, encoding=o_tmp.stated))
    s.take("damping", 0.5, o_damp)
    s._last_case = e
    return s

print("=" * 72)
print("ROT TEST: honest vs rotten vs lazy, by the kernel's own instruments")
print("=" * 72)

for kind in ("honest", "rotten", "lazy"):
    s = build(kind)
    rep = s.intake_report()
    v = s._last_case.verdict()
    print(f"\n[{kind.upper()}]")
    print(f"  verdict        : {v!r}")
    print(f"  intake         : total={rep['total']} declared={rep['declared']} "
          f"anonymous={rep['anonymous']}")
    print(f"  standing       : {rep['note']}")

print("\n" + "=" * 72)
print("READING")
print("=" * 72)
print("""HONEST and ROTTEN are indistinguishable on every instrument: same
verdict, same intake counts, same standing. The receipts measure
paperwork-effort, not truth -- as the horizon entry admits ('an Origin
is the world's testimony about the world; the register records it and
can never check it').

LAZY is the only one the instruments can flag. Consequence, stated
plainly: the current discipline PENALIZES honest laziness and REWARDS
articulate fabrication. An adversary pays a few sentences; an honest
hurried caller pays a mark against their session. This inversion is the
entry-cost asymmetry, now exhibited rather than suspected.

Second finding (from static audit, comparisons/06): most receipts are
write-only. Marks like 'index-collapsed' and 'undeclared-encodings' are
read by no kernel path; they change no downstream behavior. A receipt
nothing reads is decoration with an audit trail.

Neither finding says the receipts are worthless. They say precisely
what the receipts are: a record that makes lying COMMITTAL (on the
record, attributable, falsifiable later) rather than impossible, and a
record that is only as good as its readers -- of which the kernel
currently has almost none.""")
