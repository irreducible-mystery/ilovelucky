"""
Demonstration of the v1 kernel: each audit priority shown working.
Run: python3 demo_v1.py   (from repo/lucky/kernel/)
"""
from lucky1 import (Testimony, testify, absent, not_t, refute,
                    Session, Gap, Anomaly, CHOICES, HORIZON)

BAR = "=" * 72
s = Session()

# ---------------------------------------------------------------- P1
print(BAR); print("P1: all choices registered at import -- before any feature ran")
print(f"  CHOICES has {len(CHOICES)} entries at load, including:")
for c in CHOICES:
    print(f"   - {c['name']}")

# ---------------------------------------------------------------- P2
print(); print(BAR); print("P2: verdicts carry their own sensitivity")
fragile = testify(Testimony("w1", "for", 0.8), Testimony("w2", "against", 0.3))
robust  = testify(Testimony("w1", "for", 0.98), Testimony("w2", "against", 0.02))
print("  fragile:", fragile)
print("  robust :", robust)
print("  -> v0 printed near-identical labels for these; now the flip distance")
print("     is in-band: one verdict dies under a 0.05 nudge, one survives 0.4.")

# ---------------------------------------------------------------- P3
print(); print(BAR); print("P3: numeric substrate confessed and quantized")
b = s.explore(testify(Testimony("a","for",0.9), Testimony("b","against",0.9)),
              {"inconsistent": lambda e: "audit", "blur": lambda e: "note"})
s.collapse(b, reason="single action required")
print("  receipt:", s.ledger[-1])
print("  -> discarded weights are now readable (v0 leaked 0.19999999999999996)")

# ---------------------------------------------------------------- P4
print(); print(BAR); print("P4: corroboration is a selectable, recorded mode")
weak = [Testimony("s1","for",0.4), Testimony("s2","for",0.4), Testimony("s3","for",0.4)]
print("  max      :", testify(*weak))
print("  noisy_or :", testify(*weak, combine="noisy_or"))
print("  -> three weak independent voices now CAN strengthen each other,")
print("     and the mode used is written into the trail. Unknown mode?")
print("    ", testify(*weak, combine="mystery"), "<- informational, not a crash")

# ---------------------------------------------------------------- P5
print(); print(BAR); print("P5: the self-model grows from its own unparsed questions")
for qtext in ["What is your favorite number?",
              "Do you dream?",
              "What can you see from where you stand?"]:
    print(f"  Q: {qtext}\n  A: {s.self_model.ask(qtext)}")
gap = s.self_model.ask("Where does your vocabulary end?")
print("  Q4 ->", gap)
d = s.self_model.teach(
    gap, keys=("vocabulary",),
    responder=lambda: Gap("my vocabulary ends where my patterns end; this "
                          "answer exists because earlier questions failed"),
    name="vocabulary-boundary-awareness")
print("  taught:", d)
print("  re-ask:", s.self_model.ask("Where does your vocabulary end?"))
print("  -> new self-description born from documented insufficiency,")
print("     birth record attached. The Distinction is now consumed, not framed.")

# ---------------------------------------------------------------- P6
print(); print(BAR); print("P6: branch purity check")
ev = testify(Testimony("a","for",0.9), Testimony("b","against",0.9))
def misbehaving(e):
    e.mu = 0.0          # mutates its copy
    return "acted on altered evidence"
b2 = s.explore(ev, {"inconsistent": misbehaving})
print("  bundle:", b2)
for note in b2.purity_notes: print("   note:", note, note.trail)
print("  original evidence untouched:", ev)
print("  -> coexistence violations are now reportable, not silent.")

# ---------------------------------------------------------------- P7
print(); print(BAR); print("P7: structural identity for confusions")
mid  = testify(Testimony("x","for",0.5),  Testimony("y","against",0.45))
high = testify(Testimony("x","for",0.72), Testimony("y","against",0.28))
for _ in range(2): s.observe("is_alive", mid)
print("  2x blur near (Gc~0.0) + 1x blur near (Gc~0.4):")
print("   ", s.observe("is_alive", high) or "no genesis: different neighborhoods")
print("   ", s.observe("is_alive", mid)  or "no genesis yet")
print("  keys tracked:", [k for k in s.pressure])
print("  -> v0 merged all blur under one name; v1 separates unlike confusions,")
print("     so genesis proposals point at a specific region of failure.")

# ---------------------------------------------------------------- horizon
print(); print(BAR); print(f"HORIZON ({len(HORIZON)} entries); the newest, on itself:")
h = HORIZON[-1]
print(f"   cannot: {h['claim']}  [{h['forced_by']}-forced]")
print(f"   why: {h['why']}")
