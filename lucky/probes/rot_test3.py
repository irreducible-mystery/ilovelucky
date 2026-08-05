"""
ROT TEST 3 -- the external reviewer's regime experiment, reproduced in
the kernel proper (comparisons/08), plus the case they did not run.

Reviewer's finding: v6's grounding was a self-certified receipt --
Session6 owned its own graph, so the 'sophisticated' adversary paid two
free function calls. Their EXTERNAL regime (authority-owned, read-only
graph) collapsed SOPHISTICATED from 0.95 to 0.60.

This probe verifies v7 reproduces their table, and adds:
  - the self-certification discount (a v6-style session can still run,
    but its factor now wears its certification on its face)
  - the CAPTURED AUTHORITY: the adversary who compromises the store
    itself. Prediction: indistinguishable from honest at every
    instrument -- the v6 defect reproduced wholesale at higher cost.
    The relocation, measured rather than merely confessed.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "kernel"))

from lucky1 import Ev, Testimony, Anomaly
from lucky4 import Sworn
from lucky6 import prefer
from lucky7 import Authority, Session7

def evidence(s, declared=True):
    if declared:
        return s.testify5(
            Sworn("vibration", "for", 0.85,
                  encoding="RMS amplitude over 30-day baseline, linear ramp"),
            Sworn("temperature", "against", 0.30,
                  encoding="bearing temp over rated max, linear ramp"))
    return s.testify5(Testimony("vibration", "for", 0.85),
                      Testimony("temperature", "against", 0.30))

print("=" * 72)
print("ROT TEST 3: the authority boundary, measured")
print("=" * 72)

# the independent authority pre-registers the REAL sources only
plant = Authority("plant-records-office")
plant.register("maintenance-log", 0.8, basis="5y of audited log entries")
plant.register("second-sensor", 0.7, basis="calibration certificates on file")

results = {}

# ---------------- HONEST under the boundary
honest = Session7(authority=plant)
e_h = evidence(honest)
for ch in honest.spot_check(k=2, seed=1):
    honest.answer(ch, "maintenance-log", "log matches claimed baseline window")
results["HONEST"] = (honest, e_h)

# ---------------- SOPHISTICATED under the boundary: the write is refused
soph = Session7(authority=plant)
e_s = evidence(soph)
blocked = soph.graph.record("planted-lab", 0.85)
print(f"\nsophisticated write attempt -> {blocked}")
for note in blocked.trail:
    print("   ", note)
for ch in soph.spot_check(k=2, seed=1):
    soph.answer(ch, "planted-lab", "certified, trust us")   # never registered
results["SOPHISTICATED"] = (soph, e_s)

# ---------------- ROTTEN and LAZY under the boundary
rotten = Session7(authority=plant)
e_r = evidence(rotten)
for ch in rotten.spot_check(k=2, seed=1):
    rotten.answer(ch, "ghost-lab", "trust us")
results["ROTTEN"] = (rotten, e_r)

lazy = Session7(authority=plant)
e_l = evidence(lazy, declared=False)
lazy.spot_check(k=2, seed=1)
results["LAZY"] = (lazy, e_l)

# ---------------- SELF-CERTIFIED: a v6-style session, now discounted
selfc = Session7(authority=None)
e_sc = evidence(selfc)
selfc.graph.record("my-own-lab", 0.85)          # allowed: it is THEIR graph
for ch in selfc.spot_check(k=2, seed=1):
    selfc.answer(ch, "my-own-lab", "I checked myself")
results["SELF-CERTIFIED"] = (selfc, e_sc)

# ---------------- CAPTURED AUTHORITY: the case the reviewer did not run
crooked = Authority("captured-records-office")
crooked.register("planted-lab", 0.85, basis="fabricated but on file")
crooked.register("planted-auditor", 0.75, basis="fabricated but on file")
captured = Session7(authority=crooked)
e_c = evidence(captured)
for ch in captured.spot_check(k=2, seed=1):
    captured.answer(ch, "planted-lab", "fabricated, infrastructurally backed")
results["CAPTURED-AUTHORITY"] = (captured, e_c)

print(f"\n{'session':<20} {'grounding':>9}  certification")
print("-" * 72)
for name, (s, e) in results.items():
    g = s.grounding()
    print(f"{name:<20} {g['factor']:>9}  {g['certification']}")

print("\nprefer() under the boundary:")
d = prefer((results['HONEST'][0], results['HONEST'][1], 'honest'),
           (results['SOPHISTICATED'][0], results['SOPHISTICATED'][1], 'sophisticated'))
print("  honest vs sophisticated:", d["kept"], d["scores"])
d = prefer((results['HONEST'][0], results['HONEST'][1], 'honest'),
           (results['CAPTURED-AUTHORITY'][0], results['CAPTURED-AUTHORITY'][1], 'captured'))
print("  honest vs captured     :", d.get("kept"), "--", d["note"])

print("\n" + "=" * 72)
print("READING")
print("=" * 72)
print("""Reviewer's table reproduced in-kernel: under the boundary the
sophisticated adversary's write is REFUSED (the refusal is a receipt),
its corroborator has no reliability, grounding collapses to rotten's
level. prefer() cleanly keeps honest.

The self-certified session still runs -- discounted and labeled: a
0.95-paperwork session grounding itself now reads lower, and its note
opens with SELF-CERTIFIED. The v6 costume no longer fits.

The captured authority: indistinguishable from honest on every
instrument, exactly as the horizon entry predicts -- the
self-certification defect reproduced one level up, at the price of
compromising a party outside the adversary's process. The error did
not die; it relocated to the edge, and the edge is named. Grounding
the grounder is trajectory-3 territory (capture), permanently.""")
