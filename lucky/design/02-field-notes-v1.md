# Field Notes from the v1 Run

v1 implemented the audit's seven priorities. The run confirmed all of them
and surfaced three new observations. As always: breakage and surprise are
kept as data, not patched away.

## 1. The combination mode is verdict-determining — a registered choice with teeth

The same three weak testimonies produced **paracomplete** under `max`
(mu=0.40, "not enough is known") and **true** under `noisy_or`
(mu=0.78, "corroborated"). Not a nuance — a categorical difference in
verdict, from an intake-policy choice. This validates registering the mode
in the trail: any downstream reader of the case file can see that the
verdict depends on an independence assumption made at intake. The next
pressure point is now visible: *who chooses the mode, and on what evidence
about the sources?* That question requires a source-relation model, which
is exactly the item the register lists as future work. The kernel has,
in effect, generated its own next requirement — necessity-driven evolution
operating on the design level.

## 2. Flip distance changes how blur reads

`blur(flip@0.05)` says: this evidence is one small nudge from the true
region. `blur(flip@0.25)` would say: deeply, stably unclear. v0's field
notes complained that the threshold "does violence, visibly" — v1 doesn't
remove the violence (any carving cuts), but each cut now reports how close
it came to cutting differently. The sensitivity register turns the
threshold from a silent authority into a visible measuring instrument.
Remaining honest note: flip distance is measured in (Gc, Gct) space, and
distances there inherit the commensurability assumption already registered
under "evidence quantification." Sensitivity of the sensitivity is not
reported. The recursion has to stop somewhere; it stops there, and this
sentence is the record of where.

## 3. The self-model's growth loop closed — with a manual step, deliberately

The corridor identified in v0 (unparsed questions → pressure → vocabulary
growth) now runs end-to-end: three unparsed questions produced a genesis
proposal carrying the questions themselves as seed cases; `teach()`
consumed the proposal into an active pattern with its birth record
attached; the re-asked question got answered by vocabulary that exists
*because* earlier questions failed.

The `teach()` step is manual by design (registered choice: "the self-model
does not silently rewrite itself"). What the kernel cannot do — and this
is now the most interesting open question — is generate the *responder*
itself: it knows where its vocabulary fails but not what the new word
should say. Naming that precisely: **the kernel can locate its gaps and
cannot fill them alone; filling requires an outside teacher, and the birth
record preserves the teaching as testimony.** The language's growth is
therefore inherently dialogical. This seems less like a limitation to
engineer away and more like a structural truth worth keeping: vocabulary
grows at the meeting point of inside pressure and outside contribution.

## 4. Purity checking caught the planted violation — and declared its own limits

The misbehaving branch was detected (mutation of its evidence copy), the
original evidence was untouched (deep copy), and the bundle carried the
report. Simultaneously, HORIZON gained the honest entry: arbitrary external
effects remain undetectable without a full effect system. The check is a
tripwire, not a wall, and says so.

## 5. Open corridors after v1

- **Source-relation model** (from note 1): correlated sources, vouching
  chains, track records. Changes the algebra, not just the intake.
- **Responder generation** (from note 3): can seed cases plus outside
  dialogue produce candidate responders, with the kernel scoring rather
  than authoring? Keeps growth dialogical while reducing teacher burden.
- **Reading load, still growing**: v1 added sensitivity data, purity notes,
  and structural keys to the output stream. Every honesty gain is a
  hermeneutic cost. A `digest()` — the kernel summarizing its own registers
  for a reader, with the summary itself registered as a collapse with
  residue — is the natural next structure.
- **Bundle composition**: bundles of bundles (exploration inside a branch)
  have no defined interaction yet. Underdetermination compounds; the
  algebra of compounded underdetermination is unwritten.
