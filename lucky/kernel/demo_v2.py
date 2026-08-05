"""
Demonstration of the v2 explore-build corridors.
Run: python3 demo_v2.py   (from repo/lucky/kernel/)
"""
from lucky1 import Testimony, testify, Session, Gap
from lucky2 import (SourceGraph, testify_related, propose_responders, adopt,
                    digest, compose, collapse_composed, CHOICES, HORIZON)

BAR = "=" * 72
s = Session()

# ================================================================ A
print(BAR); print("A: SOURCE RELATIONS -- correlation, vouching, groundless circles")
g = SourceGraph()
g.record("lab-1", 0.9)                  # observed track record
g.vouch("lab-1", "student-A"); g.vouch("student-A", "student-B")
g.vouch("blog-X", "blog-Y"); g.vouch("blog-Y", "blog-X")   # circle, no ground
g.correlate("wire-1", "wire-2", "wire-3")                  # one upstream feed

r, notes = g.reliability("student-B")
print(f"  student-B reliability (2-step vouch from lab-1): {r}")
r2, notes2 = g.reliability("blog-X")
print(f"  blog-X reliability: {r2} -- notes: {notes2[0]}")

same_feed = [Testimony("wire-1","for",0.8), Testimony("wire-2","for",0.8),
             Testimony("wire-3","for",0.8)]
naive = testify(*same_feed, combine="noisy_or")
aware = testify_related(g, *same_feed, combine="noisy_or")
print("  three copies of one feed, naive noisy_or :", naive)
print("  same, with correlation declared          :", aware)
print("   trail notes:", [t for t in aware.trail if isinstance(t, str)][-2:])
print("  -> v1 would have triple-counted an echo as corroboration.")

# ================================================================ B
print(); print(BAR); print("B: RESPONDER GENERATION -- drafted inside, adopted from outside")
for qtext in ["What color is meaning?", "What color is a boundary?",
              "What color is pressure?"]:
    resp = s.self_model.ask(qtext)
gap = resp     # third ask returned the genesis proposal
print("  gap:", gap)
cands = propose_responders(gap)
for i, c in enumerate(cands):
    print(f"  candidate {i}: keys={c['keys']} coverage={c['coverage']} ({c['basis']})")
d = adopt(s, gap, cands[0], name="color-questions-noted", selected_by="Kelly")
print("  adopted:", d)
print("  re-ask:", s.self_model.ask("What color is doubt?"))
print("  -> the kernel drafted; the outside selected; the birth record names both.")

# ================================================================ D
print(); print(BAR); print("D: BUNDLE COMPOSITION -- underdetermination compounding")
outer_ev = testify(Testimony("m1","for",0.6), Testimony("m2","against",0.55))
inner_ev = testify(Testimony("n1","for",0.5), Testimony("n2","against",0.5))
bundle = s.explore(outer_ev, {
    "inconsistent": lambda e: s.explore(inner_ev, {
        "inconsistent": lambda e2: "audit both instruments",
        "blur":         lambda e2: "audit outer, re-measure inner"}),
    "blur": lambda e: "re-measure the outer question",
})
cb = compose(bundle)
print("  composed:", cb)
act = collapse_composed(s, cb, reason="one action, chosen over full paths")
print("  collapsed to:", repr(act))
print("  receipt:", s.ledger[-1])
print("  -> deep paths are visibly thin; pruning left receipts, unlike explore's floor.")

# ================================================================ C
print(); print(BAR); print("C: DIGEST -- the kernel reads itself, and pays for the reading")
# add some pressure so the digest has a hotspot to report
blurry = testify(Testimony("x","for",0.5), Testimony("y","against",0.45))
for _ in range(2): s.observe("is_alive", blurry)
print(digest(s, budget=3))
print("  the digest act itself, in the ledger:", s.ledger[-1])
print(f"  registers now: {len(CHOICES)} choices, {len(HORIZON)} horizon entries")
print("  -> readability was bought with omission, and the receipt shows the price.")
