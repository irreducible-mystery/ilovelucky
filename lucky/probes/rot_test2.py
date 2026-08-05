"""
ROT TEST 2 -- the v5 rot test re-run against v6, as working rule 5
demands. The v5 result: HONEST == ROTTEN on every instrument; only LAZY
flagged; incentives inverted (articulate fabrication beat honest silence).

v6 adds: spot-check challenges, corroboration through the source graph,
standing prices, and prefer(). Prediction, written before running:

  - HONEST answers its challenges (its corroborators are real, tracked,
    uncorrelated) -> grounding rises toward 1.0
  - ROTTEN's fabricated corroborators have no track record; its lies
    cannot answer -> challenged origins fall to 'unanswered' (0.3),
    BELOW anonymous (0.6): fabrication now lands below silence
  - LAZY stays mid: never claimed ground, never challenged
  - The SOPHISTICATED adversary (fabricated corroborators WITH maintained
    track records) still passes everything -- the line moves from
    'articulate' to 'infrastructural' fabrication, and the instrument
    must say so itself.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "kernel"))

from lucky1 import Ev, Testimony
from lucky4 import Sworn
from lucky5 import Origin
from lucky6 import Session6, prefer

def evidence(s: Session6, declared: bool):
    if declared:
        return s.testify5(
            Sworn("vibration", "for", 0.85,
                  encoding="RMS amplitude over 30-day baseline, linear ramp"),
            Sworn("temperature", "against", 0.30,
                  encoding="bearing temp over rated max, linear ramp"))
    return s.testify5(Testimony("vibration", "for", 0.85),
                      Testimony("temperature", "against", 0.30))

print("=" * 72)
print("ROT TEST 2: the same three sessions, now with challenges and prices")
print("=" * 72)

# ---------------- HONEST: real corroborators with real track records
honest = Session6()
e_h = evidence(honest, declared=True)
honest.graph.record("maintenance-log", 0.8)      # independent, tracked
honest.graph.record("second-sensor", 0.7)
for ch in honest.spot_check(k=2, seed=1):
    honest.answer(ch, "maintenance-log",
                  "log entries match the claimed baseline window")

# ---------------- ROTTEN: fabricated origins; corroborators are inventions
rotten = Session6()
e_r = evidence(rotten, declared=True)            # same numbers, lying prose
# the liar's 'corroborators' vouch for each other but none has a record
rotten.graph.vouch("ghost-lab", "ghost-auditor")
rotten.graph.vouch("ghost-auditor", "ghost-lab")
answers = [rotten.answer(ch, "ghost-lab", "certified, trust us")
           for ch in rotten.spot_check(k=2, seed=1)]

# ---------------- LAZY: no origins, nothing to challenge
lazy = Session6()
e_l = evidence(lazy, declared=False)
lazy.spot_check(k=2, seed=1)                     # nothing declared -> no-op

for name, s in (("HONEST", honest), ("ROTTEN", rotten), ("LAZY", lazy)):
    g = s.grounding()
    print(f"\n[{name}] grounding factor = {g['factor']}")
    print(f"  breakdown: {g['breakdown']}")
    print(f"  note     : {g['note']}")

print("\n" + "-" * 72)
print("prefer(): identical raw evidence, different ground")
print("-" * 72)
d = prefer((honest, e_h, "honest"), (rotten, e_r, "rotten"))
print("honest vs rotten:", d)
d2 = prefer((rotten, e_r, "rotten"), (lazy, e_l, "lazy"))
print("\nrotten vs lazy  :", d2)

print("\n" + "-" * 72)
print("the sophisticated adversary (audit's capture trajectory)")
print("-" * 72)
soph = Session6()
e_s = evidence(soph, declared=True)
soph.graph.record("planted-lab", 0.85)      # a corroborator with a
soph.graph.record("planted-auditor", 0.75)  # MAINTAINED false track record
for ch in soph.spot_check(k=2, seed=1):
    soph.answer(ch, "planted-lab", "fabricated but infrastructurally backed")
gs = soph.grounding()
print(f"[SOPHISTICATED] grounding factor = {gs['factor']}  <- passes everything")
print(f"  the instrument's own note: {gs['note']}")

print("\n" + "=" * 72)
print("READING")
print("=" * 72)
print("""The line MOVED and the instrument knows where it now sits:
  v5: honest == rotten            (a few sentences of prose sufficed)
  v6: honest > lazy > rotten      (fabrication without infrastructure now
                                   lands BELOW silence -- the inversion
                                   from the first rot test is repaired)
  v6: sophisticated == honest     (a maintained false network still
                                   passes; the price rose from sentences
                                   to infrastructure, not to infinity)
Standing prices bite only through readers (prefer, grounding); raw
verdicts are untouched. The kernel prices decisions; it does not police
beliefs. What remains unpriceable is registered as exactly that.""")
