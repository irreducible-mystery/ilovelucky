# What Is an Error Here? A Grounding Pause

Written at Kelly's request before any further building. The question:
errors come in kinds; some are inherent and cannot be resolved — they
relocate to the edges when trapped, and over-correction builds ever-larger
traps that the error always escapes. Sometimes the best available move is
visibility: make the error-kind known so it is caught fast. But that needs
grounding, and the grounding itself can become a beautiful castle made of
sand. So: what do we even mean by an error? What does a failure of the
Lucky idea look like? What shape is it? Where is the gap?

This document was written *after* running an experiment (probes/rot_test.py)
and a static audit of the kernel, not before. The answers below are
grounded in what the instruments actually showed, including two findings
that are uncomfortable.

---

## 1. The taxonomy we have been using without naming it

Five kinds of error have been circulating in this project. Naming them
matters because the correct treatment differs per kind, and treating one
kind with another kind's medicine is precisely how sand castles start.

**E1 — World errors.** A sensor breaks; a study is fraudulent; a weight of
1.7 arrives. The world's testimony is wrong or malformed. *Treatment:
record and surface.* These were never ours to fix (testify3 returns the
out-of-range weight as an anomaly about the caller). Resolvable case by
case, inexhaustible as a class.

**E2 — Carving errors.** Our vocabulary cuts the world in the wrong place:
a threshold at 0.55 that should be asymmetric, a blur region hiding two
distinguishable tendencies. *Treatment: pressure meters and genesis* —
accumulate the failures until they name their own repair. Resolvable, one
at a time, and each resolution creates new edges (a finer carving has more
boundary, and boundaries are where sorites-revenge lives — critique B
showed decisions jumping at 2e-7 deltas *because* there were crisp lines
to jump across). This is the first inherent relocation: **carving errors
are not reduced by finer carving; they are relocated to more numerous,
finer edges.**

**E3 — Structural incapacities.** The classical substrate; the inability
to verify a stated origin; the unstatable conditional; the regress of
intake. *Treatment: HORIZON — say it, and stop.* These are the errors
Kelly's message describes exactly: they cannot be resolved, only pointed
at. Every attempt to trap one builds the next room it escapes into. The
verification regress is the cleanest specimen: to check an origin you need
a second channel; the second channel's reports need origins; a third
channel... The regress does not terminate. v5 did not try to terminate it;
v5 made each step leave a receipt. That is the "visibility instead of
capture" move, and it is the right treatment *for this kind only*.

**E4 — Discipline errors (ours).** The kernel's own honesty machinery
misleading: a receipt that looks load-bearing but is decorative; an
instrument that measures effort while appearing to measure truth; a
confession register that grows monotonically and is read by no one. These
are new in kind — they did not exist before we built the discipline,
because they are errors *of* the discipline. The rot test was designed to
hunt exactly these, and found two (§2).

**E5 — The failure of the idea itself.** Not an error *in* Lucky but the
shape of Lucky being wrong. §3.

## 2. What the instruments actually showed (the uncomfortable part)

**Finding 1 — The rot test: our instruments detect effort, not truth.**
Three sessions with identical evidence: HONEST (true origins), ROTTEN
(fabricated but well-formed origins), LAZY (no origins). Run: HONEST and
ROTTEN are indistinguishable on every kernel instrument — same verdict,
same intake counts, same standing ("can pass as declared-ground"). Only
LAZY is flagged. So the current discipline **penalizes honest laziness and
rewards articulate fabrication**. An adversary pays a few sentences of
confident prose; an honest hurried caller pays a mark against their
session. The entry-cost gradient points the wrong way for adversaries and
the right way only for the sloppy.

This is not a refutation of the register — the horizon entry predicted it
("a stated origin is testimony, not proof"). But there is a difference
between a limitation confessed in a docstring and a limitation *exhibited
as an inversion of incentives*. The honest claim for what receipts buy is
narrower than the register's aura suggests: a receipt makes lying
**committal** — on the record, attributable, checkable-later-by-someone-
with-a-world-channel — rather than impossible or even detectable. That is
worth having. It is much less than the register *feels* like it provides.
The gap between what it provides and what it feels like it provides is a
discipline error (E4) that was live until the rot test named it.

**Finding 2 — The static audit: most receipts are write-only.** Grepping
for *readers* of the registers: CHOICES is read once (digest ranks it by
text length); the ledger is read once (digest sums it); pressure is read
by genesis. But HORIZON is read by nothing. The trail marks that v4 was
proudest of — `index-collapsed`, `conflict-manufactured-at-merge`,
`undeclared-encodings`, `frame-origin-unknown` — are read by **no kernel
path**. Nothing downstream behaves differently because they are present.
They exist for a hypothetical future reader who has never yet arrived.

A receipt nothing reads is decoration with an audit trail. Worse: each
such mark *feels* like progress at commit time, which is exactly the
sand-castle dynamic — the castle is made of confessions, and confession
has been cheap because nothing charges for it or collects on it.

## 3. So what IS a failure of the Lucky idea? Its shape

Lucky's one bet, stated plainly: **making limits visible is worth the cost
of the visibility apparatus.** Everything else — gaps, blur, priced
collapse, confession registers, receipts — is machinery for that bet.

The bet fails, not with a crash, but with a specific quiet shape, in three
stages:

1. **Receipts outnumber readers.** The kernel emits more marks than
   anything consumes. (Measured: already true. The reader/writer ratio of
   our registers is near zero.)
2. **The discipline's cost lands on the honest.** Declaring origins costs
   the truthful caller effort and costs the liar nothing but typing.
   (Measured: already true, by the rot test.)
3. **Confession substitutes for capacity.** The system's answer to every
   hard case becomes a more articulate description of why the case is
   hard. The registers grow; nothing else changes. Anomalies are filed
   and never re-read; horizons accumulate like unread terms of service.
   The final state is a system that is *perfectly honest and perfectly
   useless* — every verdict wrapped in so many receipts that reading the
   honesty costs more than re-deriving the answer from the raw evidence.

That is the shape: **failure by unread honesty.** Not wrongness —
weightlessness. The sand castle is not a castle of false claims; it is a
castle of true confessions that nothing loads.

And the gap — where the failure lives — is precisely the gap between
*emitting* a receipt and *reading* one. Every structure we have built
operates at emission. Almost nothing operates at reading. The rot test
was, notably, the first time this project pointed the kernel's instruments
at the kernel's own output and asked "can you actually tell?" — and the
answer for the adversarial case was no.

## 4. Treatments, matched to kinds — and the over-correction trap

The trap Kelly names — building ever-larger traps for errors that always
escape — has a precise signature in our terms: **applying E2 treatment
(more vocabulary, finer carving) to an E3 incapacity (unresolvable).**
The verification regress cannot be carved away; each new register that
tries is a bigger trap with the same escape. v5's `take()` was correct to
record rather than gate. The rot test now bounds what that recording buys.

The complementary trap also exists: applying E3 treatment (confess and
stop) to an E4 discipline error that is actually fixable. "Our receipts
are write-only" must NOT become a horizon entry — it is not an incapacity,
it is a debt. Confessing it would be the sand-castle move: one more
articulate description substituting for a change.

Working rules going forward, adopted as CHOICES in the kernel (not prose):

1. **No new receipt without a reader.** Any new mark, register, or
   confession must ship with at least one kernel path that reads it and
   behaves differently because of it — or it does not ship. (Emission
   without consumption is how failure-by-unread-honesty compounds.)
2. **Reader debt is paid before new corridors open.** The existing
   write-only marks get readers before v6 grows anything else.
3. **Claims about what a receipt buys are stated in adversarial terms.**
   Not "origins are declared" but "lying about origins is committal."
   Every instrument's description must survive the question: *what does
   the cheapest adversary pay?*
4. **Inherent errors get visibility with a cost bound.** For E3 kinds,
   the treatment is: name the kind ONCE, give it a stable name, make its
   instances cheap to recognize (pattern, not essay), and stop. No
   second register for the same incapacity. Escapes are noted as
   instances, not answered with architecture.
5. **The rot test runs on every version.** Any new discipline is pointed
   at itself before it is trusted: build the honest case, the rotten
   case, the lazy case; if the instrument cannot tell rotten from honest,
   that inability is stated ON the instrument, in its own repr, not in a
   design document two directories away.

## 5. What stays, said without the aura

After the deflation, what the current kernel actually provides, in
adversarial terms:

- Verdicts that carry their distance from flipping (an adversary must
  move real weight, and the amount is printed).
- Collapse that leaves the discarded weights on record (an adversary can
  collapse, but not silently).
- Contradiction and ignorance kept distinct (an adversary cannot dress
  absence-of-evidence as conflict-of-evidence or vice versa).
- Fusion that bills the fuser (an adversary can manufacture conflict at a
  merge, but the merge is marked — *when something reads marks*).
- Lying made committal, never impossible (rot test, permanent).

That list is smaller than the repo's prose suggests. It is what is real.
The next version builds readers, not registers.
