"""
Demonstration of the v3 absorption: three Etau structures inside Lucky,
plus what was deliberately left outside. Run: python3 demo_v3.py
"""
from lucky1 import Testimony
from lucky3 import (testify3, verdict3, Carving, Session3, CHOICES)

BAR = "=" * 72
s = Session3()

# ---------------------------------------------------------------- 1
print(BAR); print("1: THE INTERIOR -- blur now has direction")
cases = [
    ("lean true, slight conflict",  0.62, 0.42),
    ("lean false, thin evidence",   0.30, 0.42),
    ("conflict brewing, no lean",   0.68, 0.66),
    ("fog, faint lean true",        0.30, 0.22),
]
for name, mu, lam in cases:
    e = testify3(Testimony("a", "for", mu), Testimony("b", "against", lam))
    print(f"  {name:28s} -> {verdict3(e)!r}")
print("  -> v1 said only 'blur' for all four. Absorbed from LPA2v's")
print("     quasi-regions: the confusion now reports which way it leans")
print("     and whether certainty or knowledge is driving it.")

# ---------------------------------------------------------------- 2
print(); print(BAR); print("2: TWO SENSITIVITY AXES -- edge AND apex")
robust_ideal = testify3(Testimony("a","for",0.97), Testimony("b","against",0.03))
robust_far   = testify3(Testimony("a","for",0.85), Testimony("b","against",0.28))
print("  near-ideal support :", verdict3(robust_ideal))
print("  settled but impure :", verdict3(robust_far))
print("  -> both are 'true' and stable (flip), but apex tells them apart:")
print("     the second carries real contrary evidence and sits far from")
print("     ideal. v1 could not say this; their d/dcr geometry could.")

# ---------------------------------------------------------------- 3
print(); print(BAR); print("3: ASYMMETRIC CARVING -- registered tilt")
e = testify3(Testimony("m","for",0.72), Testimony("n","against",0.12))
neutral = Carving()
strict_accept = Carving(t_true=0.75)     # accepting support costs more here
print("  neutral carving :", verdict3(e, neutral))
print("  strict-accept   :", verdict3(e, strict_accept))
print("  -> same evidence, tilted carving: verdict changes AND the verdict")
print("     itself says '[tilted carving]'. Their VlV/VlF power, absorbed,")
print("     but a tilted verdict can no longer pose as a neutral one.")

# ---------------------------------------------------------------- 4
print(); print(BAR); print("4: WHAT WAS NOT ABSORBED -- pointing instead of repair")
bad = testify3(Testimony("sensor", "for", 1.7))
print("  weight 1.7 ->", bad)
for note in bad.trail: print("    note:", note)
print("  -> their library clamps silently; ours returns testimony about")
print("     the caller. And their decision_output (conflict=0.5=ignorance)")
print("     stays outside: Lucky's exit remains collapse-with-receipt.")

# ---------------------------------------------------------------- 5
print(); print(BAR); print("5: TENDENCY-AWARE PRESSURE -- genesis proposals gain bearings")
foggy = testify3(Testimony("x","for",0.30), Testimony("y","against",0.22))
gap = None
for _ in range(3):
    gap = s.observe3("is_ready", foggy) or gap
print(" ", gap)
print("  -> v1 genesis said 'blurred here'; v3 says 'blurred here, leaning")
print("     THIS way' -- the new word's seed cases now carry a direction.")

print(); print(BAR)
absorbed = [c for c in CHOICES if "absorbed" in c["name"] or "NOT absorbed" in c["name"]]
print(f"BIRTH RECORDS: {len(absorbed)} absorption entries in the register:")
for c in absorbed: print("  -", c["name"])
