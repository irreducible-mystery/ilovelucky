"""
Hands-on probe of Paraconsistent-Lib (LPA2v / Logic Etau implementation,
EAILAB-IFSP, pip 'paraconsistent' 0.2.4) against the situations Lucky
was built for. Run: python3 probe_etau.py
Each probe targets a suspected hidden assumption; findings feed the
comparative audit (04-etau-comparison.md).
"""
from paraconsistent.blocks.block import ParaconsistentBlock

BAR = "=" * 72

def show(name, mu, lam, **params):
    b = ParaconsistentBlock(mu=mu, lam=lam, **params)
    c = b.complete
    print(f"  {name:34s} mu={mu:<4} lam={lam:<4} -> label={c.label:6s} "
          f"dc={c.dc:+.2f} dct={c.dct:+.2f} decision={c.decision_output} "
          f"muER={c.muER:.3f}")
    return c

print(BAR); print("PROBE 1: the four corners + center (shared vocabulary check)")
show("clear support",       0.9, 0.1)
show("clear counter",       0.1, 0.9)
show("strong conflict",     0.9, 0.9)
show("no data",             0.1, 0.1)
show("dead center",         0.5, 0.5)

print(); print(BAR); print("PROBE 2: decision_output -- what happens to conflict at the exit?")
for (mu, lam, label) in [(0.9,0.9,"strong conflict"), (0.1,0.1,"no data"),
                         (0.5,0.5,"center"), (0.55,0.45,"slight lean")]:
    c = show(label, mu, lam)
print("  QUESTION: does the 3-valued decision (1/0/0.5) preserve the")
print("  conflict/ignorance distinction the 12 regions worked to keep?")

print(); print(BAR); print("PROBE 3: where does testimony come from? (intake check)")
b = ParaconsistentBlock(mu=0.8, lam=0.3)
print("  inputs are bare floats. No sources, no trail, no combination mode.")
print("  Feeding three copies of one echo is the CALLER's problem:")
print("  the library cannot see sources at all ->", b.complete.label)

print(); print(BAR); print("PROBE 4: out-of-range input -- points or silently repairs?")
b2 = ParaconsistentBlock(mu=1.7, lam=-0.4)
print(f"  mu=1.7, lam=-0.4 accepted; clamped to mu={b2.input.mu}, lam={b2.input.lam}")
print(f"  -> label={b2.complete.label}. No anomaly value; the repair is silent")
print("     (config params warn via RuntimeWarning; inputs do not even warn).")

print(); print(BAR); print("PROBE 5: threshold sensitivity -- is the carving's edge visible?")
for ftc in (0.50, 0.55, 0.60):
    c = ParaconsistentBlock(mu=0.8, lam=0.25, FtC=ftc).complete
    print(f"  FtC={ftc}: label={c.label:6s} decision={c.decision_output}")
print("  same evidence, three verdicts across FtC settings. Is the distance")
print("  to the flip reported anywhere? (Lucky v1: flip@ in every verdict.)")

print(); print(BAR); print("PROBE 6: negation family -- what operations exist on evidence?")
print("  Searching the API for negation/AND/OR/consensus over (mu, lam)...")
import paraconsistent, inspect, pkgutil
names = set()
for mod in pkgutil.walk_packages(paraconsistent.__path__, "paraconsistent."):
    try:
        m = __import__(mod.name, fromlist=["*"])
        names.update(n for n in dir(m) if not n.startswith("_"))
    except Exception:
        pass
logical = [n for n in names if any(k in n.lower() for k in
           ("not", "neg", "and", "or_", "conj", "disj", "consens", "merge"))]
print("  logical-connective candidates found:", logical or "NONE")
print("  -> the annotation algebra is present; the LOGIC (connectives,")
print("     negations, inference) is absent. It is an analyzer, not a language.")

print(); print(BAR); print("PROBE 7: does analysis history exist? (provenance check)")
b3 = ParaconsistentBlock(mu=0.6, lam=0.5)
_ = b3.complete
b3.input.mu = 0.9          # change the evidence
c = b3.complete
print(f"  after mutating mu 0.6 -> 0.9: label={c.label}, no record of the prior state")
print("  -> the block caches and invalidates; it does not remember. Evidence")
print("     has no case file; the present overwrites the past silently.")
