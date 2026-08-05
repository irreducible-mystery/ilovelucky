"""demo_v4 -- the six-experiment suite's findings, answered in the kernel.

Each scene replays a finding from comparisons/05 and shows the v4 structure
that answers it. Nothing here is mocked; every output is the kernel's own.
"""
from lucky1 import Ev, Testimony, Gap, Anomaly
from lucky4 import (Sworn, testify4, encodings_of, mass, describe,
                    iterate, Settled, Cycle,
                    framed, frame_of, forbid_fusion, fuse_frames, Session4)

BAR = "=" * 72

# ------------------------------------------------------------ scene 1
print(BAR)
print("SCENE 1 -- the encoding degree of freedom is now visible")
print(BAR)
print("critique A: five defensible encodings of the same data, five verdicts.")
print("v4 does not solve this (nothing inside the kernel can). It marks it.\n")

mixed = testify4(
    Sworn("aggregate-analysis", "for", 0.71,
          encoding="normalized aggregate rate gap, scaled to [0,1] by max rate"),
    Testimony("stratified-analysis", "against", 0.65),   # undeclared!
    combine="max")
print("case file:", describe(mixed))
print("receipts :", encodings_of(mixed))
print("\n-> the undeclared source is named in the trail; a reader of this")
print("   verdict knows one of its two numbers has no stated origin.\n")

# ------------------------------------------------------------ scene 2
print(BAR)
print("SCENE 2 -- balance no longer swallows volume")
print(BAR)
print("critique F: (0.5,0.5) from 1-vs-1 studies == (0.5,0.5) from")
print("5000-vs-5000. The lattice point is identical; the mass is not.\n")

thin = testify4(
    Sworn("study-pro", "for", 0.5, encoding="single trial, effect->weight ramp"),
    Sworn("study-con", "against", 0.5, encoding="single trial, effect->weight ramp"),
    combine="noisy_or")
# per-testimony weight chosen so 400 voices noisy_or to exactly 0.5:
w400 = 1.0 - 0.5 ** (1.0 / 400)
thick_ts = ([Sworn(f"pro-{i}", "for", w400, encoding="meta-batch ramp")
             for i in range(400)] +
            [Sworn(f"con-{i}", "against", w400, encoding="meta-batch ramp")
             for i in range(400)])
thick = testify4(*thick_ts, combine="noisy_or")
print("thin :", describe(thin))
print("thick:", describe(thick))
print("\n-> the SAME lattice point, visibly different volumes. Mass is a")
print("   count, not a measure (registered) -- but the thinness is no longer")
print("   invisible.\n")

# ------------------------------------------------------------ scene 3
print(BAR)
print("SCENE 3 -- the revenge sentence answers in an orbit")
print(BAR)
print("critique C: a sentence about its own lattice position has NO fixed")
print("point; paradox_suite manufactured convergence with hidden damping.")
print("v4: the cycle is the result, and damping is confessed when used.\n")

revenge = lambda mu, lam: (lam, mu)      # 'my certainty is negative': swap map

undamped = iterate(revenge, 1.0, 0.0, damping=0.0)
print("undamped :", undamped)
assert isinstance(undamped, Cycle) and undamped.period == 2

damped = iterate(revenge, 1.0, 0.0, damping=0.5)
print("damped   :", damped)
assert isinstance(damped, Settled)
print("\n-> the same question, two results, and the difference between them")
print("   (the damping) is printed ON the result. The convergence claim")
print("   carries the smoothing that produced it.\n")

# ------------------------------------------------------------ scene 4
print(BAR)
print("SCENE 4 -- frames: contradiction manufactured at the merge")
print(BAR)
print("black hole D + confab D: each frame is impeccable; only the")
print("index-collapsing fusion contradicts. The fusion now carries the bill.\n")

s = Session4()
alice = framed(Ev(0.95, 0.05), "infalling-observer")
bob   = framed(Ev(0.05, 0.95), "external-observer")
print(f"alice ({frame_of(alice)}):", alice)
print(f"bob   ({frame_of(bob)})  :", bob)

fused = s.fuse(alice, bob, reason="attempted superobserver account")
print("\nfused :", fused)
marks = [t for t in fused.trail if isinstance(t, str)
         and ("index-collapsed" in t or "manufactured" in t)]
for m in marks:
    print("mark  :", m)
print("ledger:", s.ledger[-1])

print("\nNow the physically forbidden case, declared from outside:")
forbid_fusion("infalling-observer", "external-observer",
              "no agent can both cross the horizon and collect the radiation")
refused = s.fuse(alice, bob, reason="second attempt")
print("refused:", refused)
assert isinstance(refused, Anomaly)

print("\nSame shape, different domain -- the homonym:")
fin = framed(Ev(0.97, 0.04), "financial-context")
riv = framed(Ev(0.05, 0.96), "river-context")
pun = s.fuse(fin, riv, reason="context stripped: a pun")
print("pun    :", pun)
print("\n-> within a frame nothing changed; across frames the contradiction")
print("   arrives with the receipt of the fusion that made it.\n")

# ------------------------------------------------------------ scene 5
print(BAR)
print("SCENE 5 -- what v4 still cannot do, said out loud")
print(BAR)
from lucky1 import HORIZON
for h in HORIZON[-4:]:
    print(f"  CANNOT {h['claim']}")
print("\ndemo_v4 complete: every scene answers a finding from comparisons/05.")
