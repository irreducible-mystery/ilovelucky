# Paraconsistency in the Field: Contradiction-Tolerant Logic in Real Control Systems

## 1. From scandal to engineering

Paraconsistent logic began as a philosophical scandal — da Costa's C-systems (Brazil, 1963), Jaśkowski's discussive logic (Poland, 1948), Priest's dialetheism ("some contradictions are true") — and mainstream logic treated it as, at best, an exotic curiosity. The engineering turn is the interesting part: contradiction-tolerance stopped being a claim about reality and became a **specification for systems that receive testimony**.

The pivot document is Belnap's "How a computer should think" (1977). His argument is brutally practical: a computer connected to multiple information sources *will* be told both `p` and `¬p`. A logic that explodes (derives everything from the conflict) is not "rigorous" — it is *unfit for purpose*, like a bridge design that assumes no wind. The four values — True, False, Both, Neither — are not metaphysical claims about propositions; they are the four possible *states of the evidence ledger*. FDE (first-degree entailment) is the logic that computes soundly over that ledger.

## 2. Annotated logic: contradiction as a point in a lattice

Blair and Subrahmanian (1987–89) turned this into **paraconsistent logic programming**: atoms are annotated with values from a lattice — in the simplest useful case, pairs (μ, λ) where μ ∈ [0,1] is the degree of *favorable* evidence and λ ∈ [0,1] the degree of *contrary* evidence, varying **independently**. This independence is the whole point. From (μ, λ) you derive two orthogonal measures:

- **Certainty degree**: Gc = μ − λ (net verdict: leaning true or false)
- **Contradiction degree**: Gct = μ + λ − 1 (evidential health: consistent, saturated, or conflicted)

A proposition can score Gc ≈ 0 for two *opposite* reasons: nobody knows anything (μ≈λ≈0, Gct≈−1, "paracomplete") or everybody disagrees violently (μ≈λ≈1, Gct≈+1, "inconsistent"). Boolean logic, fuzzy logic, and probability all collapse these two situations. Annotated logic keeps them apart — and *that* separation is what real decision systems need, because the correct response to ignorance (gather data) is different from the correct response to conflict (audit your sources).

## 3. Deployment: the Brazilian school

Da Silva Filho, Abe, Torres and colleagues (São Paulo) built the **Paraconsistent Annotated Evidential Logic Eτ** program: hardware ("Paraquantum" logic controllers), the para-analyzer algorithm (which divides the (μ, λ) unit square into twelve decision regions — true, false, inconsistent, paracomplete, and eight boundary regions), and deployed systems:

- **Autonomous robot navigation** (the Emmy robot series): ultrasonic sensors disagree constantly — one says path clear, another says obstacle. Classical fusion averages (destroying the conflict signal); paraconsistent control *routes on the conflict itself*: high Gct triggers "slow down and re-sense" behavior distinct from both "go" and "stop." The contradiction is used as *information about the sensing situation*.
- **Industrial process control & fault diagnosis**: conflicting sensor testimony about, e.g., transformer health is scored (Gc, Gct); persistent high contradiction *is itself the fault signature* (a failing sensor or a genuinely anomalous regime).
- **Medical decision support and signal analysis** (EEG classification), where inter-expert disagreement is the norm and must be represented, not laundered.

A 2024 systematic review in *Engineering Applications of AI* catalogs decades of these applications — the tradition is real, productive, and almost entirely unabsorbed by mainstream software culture.

## 4. Where the mainstream secretly needs it

- **Data integration**: two systems of record disagree about a customer's address. SQL gives you NULL or a forced overwrite; both destroy the disagreement. The honest value is Both-with-provenance.
- **Distributed consensus edges**: during partition, replicas *legitimately* hold contradictory states; CRDTs resolve by commutativity, but conflicts that can't commute (business-rule conflicts) currently get ad-hoc "last-writer-wins" — silent weakening of one testimony. A Belnap-typed merge would surface Both instead of destroying it.
- **ML pipelines**: model ensembles that disagree, retrieval sources that conflict, labelers who contradict each other. Current practice averages logits or majority-votes labels — collapsing Gct into Gc, then wondering why calibration fails precisely on contested inputs. The contested-ness was the most valuable bit, and the pipeline erased it at the first aggregation.

## 5. The design gap, precisely stated

What would native paraconsistency in a practical language require?

1. Every value of testimonial origin carries an evidence annotation (source, μ, λ) — not as metadata, but as *part of the type*.
2. Operators lift over annotations by lattice operations (Belnap's ⊓, ⊔ over the knowledge and truth orderings — two distinct orderings, another thing booleans fuse).
3. Control flow gains new primitives: `branch on Gc`, `branch on Gct` — separate dimensions of decision.
4. Explosion is blocked *by construction*: no inference path from `p:(1,0) ∧ p:(0,1)` to arbitrary `q`.

Nothing in this list is technically hard. It is culturally hard: it requires admitting, in the type system, that most of what a program knows arrived as testimony from sources that disagree — that the program is not a calculator over facts but a *juror over evidence*. The boolean is a metaphysical comfort blanket, and the field has been reluctant to give it up.
