# Response to the External Audit of design/08

The audit made five objections. Per the working rules, the response is
machinery first (lucky6, probes/rot_test2.py), prose second. Each
objection gets one of three verdicts: CONCEDED AND BUILT, CONCEDED AND
REGISTERED, or CONTESTED WITH RECEIPTS. None is contested with rhetoric.

---

## Objection 1: "The rot test measures the current instruments' absence
## of truth-seeking machinery, not an intrinsic impossibility."

**Conceded and built.** The audit is right that the v5 conclusion
overreached: "receipts measure paperwork, not truth" was a property of
instruments that never attempted even the cheapest check, dressed as a
property of the idea. The overreach was itself an E4 error filed inside
an E3 record — the audit's sharpest catch.

v6 builds the cheapest checks the audit said were missing:

- `spot_check()` — sampled challenges against declared origins.
- `answer()` — a challenge is met only by a corroborating source that
  has graph-derived reliability (v2's SourceGraph, which existed for
  three versions and was never wired to origins — the reader debt in
  its purest form), meets a floor, and is not correlated with the
  challenged source. Fabricated corroborators that vouch only for each
  other form a groundless circle and *cannot answer*.
- Standing prices: answered 1.0 > declared 0.9 > anonymous 0.6 >
  challenged-unanswered 0.3.

**Rot test 2 result (the measurement):**

| session | v5 grounding | v6 grounding |
|---|---|---|
| honest | indistinguishable | **0.95** |
| lazy | flagged | **0.75** |
| rotten | indistinguishable from honest | **0.60** |

The incentive inversion is repaired at the level the audit said it was
repairable: fabrication-without-infrastructure now lands **below
silence**. `prefer()` on identical raw evidence keeps honest over rotten
(0.52 vs 0.33) and — the part that matters — keeps *lazy* over rotten
(0.41 vs 0.33). Under v5 the liar beat the silent; under v6 the liar
must beat the silent by building infrastructure, not prose.

The horizon entry is accordingly **narrowed, not defended**: the regress
proof covers *certainty* (no finite chain of channels terminates); it
never covered *price*. What is registered now is only what is proven:
certainty is impossible, cost-raising is not, and v6 raised the cost
from sentences to a maintained corroboration network.

## Objection 2: "Adding readers doesn't stop the sand-castle; the reader
## can be another receipt; reading costs can scale until no one bothers."

**Conceded and registered — with a criterion, then a measurement.**
The audit is right that "has a reader" is satisfiable by decoration.
The criterion adopted in lucky6's records: **a reader must move a number
or a control path.** A reader whose effect is a more precise description
is emission in a reader's costume.

v6's three readers, checked against the criterion:

- `grounding()` — reads the register + challenge outcomes into a factor. NUMBER.
- `prefer()` — reads grounding into a decision between case files. NUMBER → CHOICE.
- `observe6()` — reads the `index-collapsed` mark and *reroutes pressure*:
  manufactured conflict feeds the fusion-practice meter instead of
  triggering predicate genesis. CONTROL PATH. (Without this reader, the
  superobserver merge would eventually demand new vocabulary that no
  carving can supply — architecture built to trap a merge-error, the
  exact over-correction design/08 forbids. This reader *prevents* trap-
  building rather than adding it.)

On reading costs scaling: correct, unresolved, and now measurable — the
cost of reading is a number (`grounding()` is O(register); `digest()` has
a budget). The failure register gains the audit's trajectory: cost-death.
Not solved. Priced.

## Objection 3: "The taxonomy is unstable: E3/E4 is itself a carving,
## and no non-circular criterion separates fixable from unfixable."

**Conceded — and the concession is the taxonomy working, not failing.**
The E3/E4 boundary is a carving (E2), so it is subject to exactly the
treatment every carving gets in this design: pressure and revision, with
receipts. The audit itself performed the first genesis event: it moved
"cannot verify a stated origin" from pure-E3 to mixed (certainty is E3,
price was E4), and v6 rebuilt accordingly. The criterion that emerges is
operational, not essentialist: **a limitation stays on the horizon only
in the exact logical strength that has a proof; everything weaker is
debt.** The regress proof survives at full strength for certainty; it
never proved anything about cost; the cost half was debt and is now paid.
No non-circular *a priori* criterion exists — the audit is right — but a
revision *procedure* with receipts is what this design uses in place of
a priori criteria everywhere else, and the taxonomy is not exempt from it.

## Objection 4: "The residual value list is oversold: the first three
## properties are ordinary; the value reduces to an audit log."

**Contested with receipts — one specific claim.** Conceded: flip
distances, logged collapse, and an append-only trail are available from
ordinary careful systems; a git log provides committal statements. Not
conceded: that the *composition* is ordinary. Rot test 2 is the receipt:
a git log of the rotten session and the honest session would be equally
well-formed, equally committal, and equally silent at decision time. The
difference v6 provides is that the fabrication *changes a decision
number before any human audit* — `prefer()` separates identical evidence
by ground, mechanically, at the moment of use. An audit log defers the
cost of lying to a future reader who may never come; a grounding factor
charges it at the point of decision. That specific property — lying
priced at decision time rather than detection time — is not in the
simple-audit-log bundle, and it is the property the whole apparatus now
demonstrably delivers. (The rest of the v5 aura remains deflated, as
design/08 left it.)

## Objection 5: "The working rules are themselves new architecture —
## the trap re-entered."

**Contested, on the audit's own distinction.** The trap named in
design/08 is architecture built to *capture an inherent error* — a
bigger cage for an error that relocates. The working rules are not
capture machinery; they are *emission constraints* — rules about when
NOT to build (no receipt without reader, no second register for the same
incapacity, reader debt before corridors). An anti-building rule can
still be sand — the audit is right that necessity was asserted, not
shown — but it cannot be a *bigger trap*, because it does not attempt
capture. The evidence that the rules bind rather than decorate: this
turn built exactly one module, whose contents are three readers and one
check, paid the SourceGraph debt, added zero new registers, and narrowed
one horizon entry. The rules changed what got built. That is what
binding looks like; whether it is *sufficient* remains the open bet the
audit correctly says it is.

---

## The failure register (consolidated, per objection 3's demand)

Three named trajectories for the Lucky bet, none solved, all now stated
on instruments rather than in prose alone:

1. **Unread honesty** (design/08): receipts outnumber readers; confession
   substitutes for capacity. Counter-pressure: the reader criterion.
   Status: reader/writer ratio improved this turn; still low.
2. **Cost-death** (audit, objection 2): honest use becomes too expensive;
   users leave or stop reading. Counter-pressure: budgets on digest,
   O(register) grounding. Status: unmeasured against any real user.
3. **Capture** (audit, objection 3): the sophisticated adversary builds
   infrastructure — corroborators with maintained track records, acyclic
   vouching — and passes every instrument. Rot test 2 measures this
   adversary at grounding 0.95, identical to honest. Status: priced,
   unpriceable-in-full, registered on the instrument itself (grounding's
   note names it on every call).

The bet, restated at its now-measured size: Lucky raises the price of
the cheap lie and the silent collapse, prices what it cannot prevent,
and says on each instrument what that instrument cannot see. Whether
that is worth the apparatus is not decidable from inside the apparatus
— which is, at least, the kind of sentence this project was built to be
able to say with receipts.
