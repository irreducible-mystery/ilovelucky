"""
Demonstration: the lucky0 kernel executing its commitments.
Run: python3 demo.py   (from repo/lucky/kernel/)

Walks all layers: conflicting testimony held without collapse; the plural
negations; explore-all flow with priced collapse; anomalies as information;
blur pressure forcing genesis of new vocabulary; lawful self-limits.
"""
from lucky0 import (Testimony, testify, absent, not_t, conflate, refute,
                    explore, collapse, Bundle, Gap, Anomaly, Necessity,
                    ask_self, CHOICES, HORIZON, RESIDUE_LEDGER)

BAR = "=" * 72

# ---------------------------------------------------------------- 1+2
print(BAR); print("LAYER 1+2: conflict preserved, ignorance distinguished")
conflicted = testify(Testimony("sensor-A", "for", 0.9),
                     Testimony("sensor-B", "against", 0.9))
silent = absent()
print("  sensors disagree :", conflicted)
print("  no data at all   :", silent)
print("  -> same Gc=0, OPPOSITE Gct: 'everybody disagrees' is not 'nobody knows'.")
print("  provenance intact:", [str(t.source) for t in conflicted.trail])

# ---------------------------------------------------------------- 3
print(); print(BAR); print("LAYER 3: the negation family (never conflated)")
e = testify(Testimony("witness-1", "for", 0.8), Testimony("witness-2", "against", 0.3))
print("  e            :", e)
print("  not_t(e)     :", not_t(e), "  <- verdict reversed")
print("  conflate(e)  :", conflate(e), "  <- known <-> unknown")
print("  not_t on conflict:", not_t(conflicted), " <- contradiction SURVIVES negation")
print("  refute(e)    :", refute(e, "counterexample #442"))

# ---------------------------------------------------------------- 4
print(); print(BAR); print("LAYER 4: explore all, collapse explicitly, pay in residue")
branches = {
    "true":         lambda ev: "proceed",
    "false":        lambda ev: "abort",
    "inconsistent": lambda ev: "audit the sources",
    "paracomplete": lambda ev: "gather more data",
    "blur":         lambda ev: "note the carving is failing here",
}
bundle = explore(conflicted, branches)
print("  bundle (uncollapsed):", bundle)
print("  all live perspectives ran; none overwrote another.")
act = collapse(bundle, reason="robot must move one body in one direction NOW")
print("  collapsed to:", repr(act))
print("  residue receipt:", RESIDUE_LEDGER[-1])

# ---------------------------------------------------------------- 5
print(); print(BAR); print("LAYER 5: anomalies as information")
a = Anomaly("division-shaped question asked of silence", origin="flow-rate calc")
a = a.flow("pressure model").flow("alert pipeline")
print("  ", a)
print("   trail:", a.trail)
print("   downstream reads the case file; nothing crashed, nothing was NaN-laundered.")

# ---------------------------------------------------------------- -1 & 6
print(); print(BAR); print("LAYER -1 & 6: the gap consumes, then generates")
g = Gap("what 'alive' means for a virus")
g = g.absorb("tried predicate is_alive/1").absorb("tried fuzzy degree-of-life")
print("  ", g, " <- consuming: attempts accumulate, nothing resolves")

meter = Necessity(threshold=3)
blurry = testify(Testimony("assay-1", "for", 0.5), Testimony("assay-2", "against", 0.45))
genesis_gap = None
for i in range(3):
    genesis_gap = meter.observe("is_alive", blurry) or genesis_gap
print("   blur pressure x3 on 'is_alive' ->", genesis_gap)
new_word = genesis_gap.seed("metabolic-autonomy", meter.pressure["is_alive"])
print("  ", new_word, " <- generative: vocabulary born FROM the gap,")
print("   carrying its birth record. Evolution from necessity.")

# ---------------------------------------------------------------- 7
print(); print(BAR); print("LAYER 7: lawful self-description (pointing, not crashing)")
for q in ["Are you consistent?",
          "Do you have a truth predicate for your own sentences?",
          "Does this code halt?",
          "Have you listed everything you cannot say?"]:
    print(f"  Q: {q}\n  A: {ask_self(q)}")

# ---------------------------------------------------------------- 0
print(); print(BAR); print("LAYER 0: the confession, printed by the confessor")
print(f"  CHOICES register ({len(CHOICES)} entries), e.g.:")
for c in CHOICES[:3]:
    print(f"   - {c['name']}: chose {c['chosen']!r}")
    print(f"     foreclosed: {c['foreclosed']}")
print(f"  HORIZON register ({len(HORIZON)} entries), e.g.:")
for h in HORIZON[-3:]:
    print(f"   - cannot: {h['claim']}  [{h['forced_by']}-forced]")
print()
print("  The kernel knows it is one carving among many, and says so, in-band.")
