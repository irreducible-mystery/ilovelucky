# Field Notes from the v2 Explore-Build Turn

Format note: this turn was deliberately explore-build (no external feedback
in-cycle, per Kelly's cadence direction). Four corridors built; observations
below are self-collected and will meet outside review only after the next
build stretch. Defects found are kept as data, not silently fixed.

## 1. The strongest finding: a ROBUST verdict was an artifact

Three copies of one upstream feed, taken naively with corroboration mode on,
produced `true(flip@0.44)` — not merely a wrong verdict but a wrong verdict
*wearing a high sensitivity score*. With the correlation declared, the same
testimony collapsed to `paracomplete(flip@0.05)`: one weak voice, echoed.

This matters beyond the feature. v1's sensitivity register (flip distance)
reported robustness *within* the evidence file; it could not see that the
file itself was inflated. Robustness-to-perturbation and soundness-of-intake
are different properties, and a reader who conflates them will trust echo
chambers precisely because they are loud. The digest of this: **sensitivity
data inherits the intake's assumptions and cannot audit them.** Filed as the
new leading edge of the horizon — each honesty layer reveals the next
layer's silence.

## 2. Groundless circles returned as gaps, and it felt structurally right

blog-X vouches for blog-Y vouches for blog-X, no track record anywhere:
reliability came back as no-value plus a note naming the circle. The
temptation resisted (and registered) was to assign a floor value. A circle
of mutual vouching contains information about the circle's existence and
none about the world; the kernel now says exactly that. Note for later:
the *shape* of detected circles is itself testimony (coordinated sources
often vouch in rings) — the anomaly could feed a source-graph pressure
meter the way blur feeds vocabulary pressure. Unbuilt; noted.

## 3. Responder generation worked, and its first draft contains a visible flaw

The shared-token drafter extracted ("what", "color") as keys. "color" is the
real signal; "what" will over-match nearly any future question. The
candidate was adopted anyway (by outside selection, as designed), so the
self-model now carries a slightly over-broad pattern — and its birth record
preserves exactly how it came to be over-broad. This is the dialogical
design working as intended: the kernel drafted imperfectly, the outside
selected knowingly, and the imperfection is auditable rather than hidden.
A stop-word list would fix the instance; the class of problem (drafts
inherit the crudeness of their extraction method) is registered and stays.

## 4. digest() ranked its own policy first — the proxy's bias, self-exhibited

The "longest consequence text" proxy for importance selected, as the top
line of the first digest, the digest policy choice itself — the newest and
most verbosely-consequenced entry. The kernel's self-summary opened by
describing how it self-summarizes. Comic, and diagnostic: the proxy rewards
verbosity, and verbosity correlates with recency of design attention, not
with load-bearing weight. The correct ranking signal would be *how often a
choice's consequences are exercised at runtime* — a usage meter over the
CHOICES register. Unbuilt; it would make the confession layer self-weighing.

## 5. Composition showed thin depth honestly

The depth-2 path carried weight 0.143 against the depth-1 path's 0.810 —
multiplied weights shrink fast, which is the honest shape of compounded
underdetermination: each level of exploration dilutes commitment. The
receipt now names full paths ("inconsistent/blur"), so the ledger records
not just *that* an alternative was set aside but *how deep* it was. The
open question scales: at depth 4-5, everything is thin, and collapse over
uniformly thin paths approaches arbitrary choice with paperwork. The
registered incapacity ("action's resolution") anticipates this; lived
contact with it has not happened yet.

## 6. Corridor interactions noticed while building

- digest() reported PRESSURE hotspots and SELF state in one frame — the
  first time the kernel's separate meters appeared as one self-portrait.
  Composition of *registers* (not just bundles) may be the real digest
  frontier: which choices, pressures, and ledger entries are causally
  linked, not just co-listed.
- testify_related() writes intake notes into the trail; digest() does not
  yet read trails. A future digest could surface "N values in this session
  carry substituted-neutral reliability" — session-level intake hygiene.
- Responder drafting used gap notes; source circles produce notes of the
  same shape. One mechanism (draft-from-accumulated-failure) may serve
  both vocabularies. Unification untested.

## 7. State of the cadence

Two build strokes on one review stroke, as directed. The next external
review has a richer target: not nuance-versioning of v1, but four new
structures with their own self-collected defect list (over-broad keys,
verbosity-biased digest ranking, sensitivity/intake conflation) already
on record for the reviewer to confirm, extend, or overturn.
