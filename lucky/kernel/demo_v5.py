"""demo_v5 -- the building learns to ask where things came from.

Scene 1 replays v4's own doorways and shows them now filing receipts.
Scene 2 shows a session answering for its whole intake at once.
Scene 3 makes the order-blindness rule executable -- including a
deliberately order-sensitive combiner caught by the tripwire.
Scene 4 replays the six-file upload itself as an intake story.
"""
from lucky1 import Ev, Testimony, Anomaly
from lucky4 import Sworn, Settled, Cycle
from lucky5 import Session5, Origin, order_audit

BAR = "=" * 72

# ------------------------------------------------------------ scene 1
print(BAR)
print("SCENE 1 -- v4's anonymous doorways, now on the record")
print(BAR)
s = Session5()

alice = s.framed5(Ev(0.95, 0.05), "infalling-observer",
                  Origin("frame chosen by the worldline of the qubit's carrier",
                         by="scenario author"))
bob = s.framed5(Ev(0.05, 0.95), "external-observer")     # anonymous, admitted
print("alice trail tail:", alice.trail[-1])
print("bob   trail tail:", bob.trail[-1], "   <- marked, not repaired")

s.forbid_fusion5("infalling-observer", "external-observer",
                 "no agent can cross the horizon AND collect the radiation",
                 Origin("Hayden-Preskill style operational bound", by="physics"))

revenge = lambda mu, lam: (lam, mu)
res = s.iterate5(revenge, 1.0, 0.0, damping=0.5)          # anonymous damping
if isinstance(res, tuple):
    settled, anomaly = res
    print("\nanonymous damping:", settled)
    print("                  ", anomaly)
    for n in anomaly.trail:
        print("   note:", n)
res2 = s.iterate5(revenge, 1.0, 0.0, damping=0.5,
                  damping_origin=Origin("evidential half-revision per step",
                                        by="paradox-suite reconstruction"))
print("declared damping :", res2, "  <- same math, different standing\n")

# ------------------------------------------------------------ scene 2
print(BAR)
print("SCENE 2 -- one register, whole-session accountability")
print(BAR)
e = s.testify5(
    Sworn("vibration-sensor", "for", 0.85,
          encoding="RMS amplitude over baseline, ramped to [0,1]"),
    Testimony("temperature-sensor", "against", 0.80),      # nameless number
    combine="max")
print("case file:", e)
rep = s.intake_report()
for k, v in rep.items():
    print(f"  {k}: {v}")
print("\n-> the session no longer answers doorway by doorway; it answers")
print("   for its whole intake at once, anonymity included.\n")

# ------------------------------------------------------------ scene 3
print(BAR)
print("SCENE 3 -- order-blindness: from written rule to tripwire")
print(BAR)
ts = [Sworn(f"src-{i}", "for" if i % 2 else "against", 0.1 + 0.08 * i,
            encoding="synthetic ramp") for i in range(6)]
audit = order_audit(ts, combine="noisy_or")
print("registered combiner (noisy_or):")
for k, v in audit.items():
    print(f"  {k}: {v}")

# now a deliberately order-sensitive 'combiner' outside the kernel:
def first_speaker_wins(ts):
    mu = next((t.weight for t in ts if t.polarity == "for"), 0.0)
    lam = next((t.weight for t in ts if t.polarity == "against"), 0.0)
    return Ev(mu, lam)
import random
positions = set()
for seed in range(6):
    sh = ts[:]; random.Random(seed).shuffle(sh)
    p = first_speaker_wins(sh)
    positions.add((p.mu, p.lam))
print(f"\nfirst-speaker-wins under 6 shuffles: {len(positions)} distinct positions")
print("-> order sensitivity PROVEN for the naive rule; the kernel's own")
print("   combiners pass the tripwire (which bounds nothing, and says so).\n")

# ------------------------------------------------------------ scene 4
print(BAR)
print("SCENE 4 -- the six-file upload, replayed as an intake story")
print(BAR)
lib = Session5()
files = [
    ("critique_suite.py",            Origin("adversarial probe of the library", by="parallel instance")),
    ("experiment1_conflicting_data.py", None),
    ("experiment2_fuzzy_boundaries.py", None),
    ("paradox_suite.py",             Origin("advocacy demonstration (hidden damping later found)", by="parallel instance")),
    ("blackhole_paraconsistent.py",  None),
    ("confabulation_cartography.py", Origin("self-examination, motivation stated in header", by="parallel instance")),
]
for name, o in files:
    lib.take(f"document:{name}", "<contents>", o)
rep = lib.intake_report()
print(f"documents taken: {rep['total']}, declared: {rep['declared']}, "
      f"anonymous: {rep['anonymous']}")
print(f"nameless: {rep['anonymous_slots']}")
print(f"standing: {rep['note']}")
print("\n-> arrival sequence is retained as receipts (seq 0..5); any reading")
print("   that leans on order must now cite which seq numbers it used.")
print("   The synthesis in comparisons/05 was order-blind by procedure --")
print("   all six read before any verdict -- and the register makes that")
print("   procedure checkable instead of merely claimed.")

print("\ndemo_v5 complete: the building asks, not just the door.")
