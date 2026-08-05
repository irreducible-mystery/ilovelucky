"""
lucky2 -- explore-build extension of the v1 kernel. Four corridors:

  A. Source-relation model : correlation groups, vouching chains with
     circle detection; reliability as a derived, confessed quantity
  B. Responder generation  : the kernel drafts candidate self-descriptions
     from its own gap records; adoption stays dialogical (outside selection)
  C. digest()              : the kernel summarizes its own registers for a
     reader -- and the summary is itself a collapse, with an omissions
     receipt filed in the ledger. Honesty about the cost of readability.
  D. Bundle composition    : exploration inside exploration; compounded
     underdetermination flattened with path provenance and a depth meter.

Everything imports and extends lucky1; nothing is patched in place.
"""
from lucky1 import (Ev, Testimony, Gap, Anomaly, Distinction, Bundle,
                    Session, q, choose, cannot, CHOICES, HORIZON,
                    LIVENESS, _combine)
from dataclasses import dataclass, field
from typing import Callable, Optional
import itertools

# ================================================================ A. SOURCES
choose("source correlation handling",
       "declared correlation groups; within a group, voices merge by max "
       "(treated as one voice) before cross-group combination",
       "pairwise correlation coefficients with analytic discounting (needs "
       "a joint model we do not have); ignoring correlation (v1's silence)",
       "undeclared correlations still overcount; the model only helps "
       "where the graph is honest -- garbage graph, garbage discount")

choose("vouching propagation",
       "reliability = own track record if present, else damped mean of "
       "vouchers' reliability (damping 0.8, depth limit 3); circles are "
       "detected and returned as notes, not resolved",
       "eigenvector-style global solution (hides the circularity it solves); "
       "refusing all vouched reliability (discards real structure)",
       "a vouching circle with no track record anywhere in it has NO "
       "ground; the kernel points at the circle instead of inventing a floor")

DAMPING, VOUCH_DEPTH = 0.8, 3

class SourceGraph:
    """Relations between sources: correlation groups and vouching edges.
    Reliability is derived, never asserted from nowhere."""
    def __init__(self):
        self.track: dict[str, float] = {}          # source -> observed record [0,1]
        self.vouches: dict[str, list] = {}         # source -> [(voucher, weight)]
        self.groups: list[set] = []                # correlation groups

    def record(self, source: str, score: float):
        self.track[source] = q(score)

    def vouch(self, voucher: str, target: str, weight: float = 1.0):
        self.vouches.setdefault(target, []).append((voucher, weight))

    def correlate(self, *sources: str):
        self.groups.append(set(sources))

    def reliability(self, source: str, _seen=None, _depth=0):
        """Returns (value, notes). Circles and groundlessness become notes."""
        _seen = _seen or set()
        if source in self.track:
            return self.track[source], ()
        if source in _seen:
            return None, (f"vouching circle at {source!r}: no ground anywhere in it",)
        if _depth >= VOUCH_DEPTH:
            return None, (f"vouch chain for {source!r} exceeded depth {VOUCH_DEPTH}",)
        vs = self.vouches.get(source)
        if not vs:
            return None, (f"{source!r}: no track record, no vouchers -- reliability is a gap",)
        vals, notes = [], []
        for voucher, w in vs:
            v, n = self.reliability(voucher, _seen | {source}, _depth + 1)
            notes.extend(n)
            if v is not None:
                vals.append(v * w * DAMPING)
        if not vals:
            return None, tuple(notes) or (f"{source!r}: all vouch paths groundless",)
        return q(sum(vals) / len(vals)), tuple(notes)

    def _group_of(self, source):
        for g in self.groups:
            if source in g:
                return frozenset(g)
        return frozenset({source})

def testify_related(graph: SourceGraph, *ts: Testimony, combine="noisy_or"):
    """Testimony intake that consults the source graph.
    - weights scaled by derived reliability (unknown reliability -> 0.5,
      and the substitution is noted in the trail, not silent)
    - correlated sources merge (max) within their group before combination"""
    notes = []
    def effective(t: Testimony):
        r, n = graph.reliability(t.source)
        notes.extend(n)
        if r is None:
            r = 0.5
            notes.append(f"{t.source!r}: reliability unknown; neutral 0.5 substituted")
        return q(t.weight * r)

    out = {}
    for polarity in ("for", "against"):
        by_group = {}
        for t in ts:
            if t.polarity != polarity:
                continue
            by_group.setdefault(graph._group_of(t.source), []).append(effective(t))
        merged = [max(ws) for ws in by_group.values()]      # one voice per group
        if len(by_group) != sum(1 for t in ts if t.polarity == polarity):
            notes.append(f"{polarity}: correlated voices merged "
                         f"({sum(len(w) for w in by_group.values())} -> {len(merged)})")
        out[polarity] = _combine(merged, combine) or 0.0
    return Ev(out["for"], out["against"],
              tuple(ts) + (f"combine:{combine}+source-graph",) + tuple(notes))

cannot("derive reliability for a groundless vouching circle",
       "mutual vouching with no track record anywhere contains no information "
       "about the world, only about the circle; any assigned number would be "
       "an invented floor", "theorem")

# ================================================================ B. RESPONDERS
choose("responder generation",
       "the kernel drafts candidate responders from a gap's seed cases "
       "(shared-token extraction + echo templates) and scores them by seed "
       "coverage; ADOPTION requires outside selection via teach()",
       "full self-authorship (the kernel cannot judge the meaning of its own "
       "candidates); no drafting (v1: full teacher burden)",
       "growth stays dialogical: inside pressure drafts, outside judgment "
       "adopts; the birth record now names both contributors")

def propose_responders(gap: Gap) -> list[dict]:
    """Draft candidates from the gap's own notes. Ranked, never adopted."""
    seeds = [str(s) for s in gap.notes]
    tokens = {}
    for s in seeds:
        for w in s.lower().replace("?", "").split():
            if len(w) > 3:
                tokens[w] = tokens.get(w, 0) + 1
    shared = sorted((w for w, c in tokens.items() if c > 1),
                    key=lambda w: -tokens[w])[:3]
    candidates = []
    if shared:
        candidates.append(dict(
            keys=tuple(shared[:2]),
            draft=(f"questions sharing {shared!r} exceeded my patterns; "
                   f"this response exists because {len(seeds)} of them failed"),
            coverage=q(sum(1 for s in seeds if any(t in s.lower() for t in shared))
                       / max(len(seeds), 1)),
            basis="shared-token"))
    candidates.append(dict(
        keys=("__echo__",),
        draft=("I could not parse this family of questions: " +
               " | ".join(seeds[:3]) + (" ..." if len(seeds) > 3 else "")),
        coverage=1.0, basis="echo (always applicable, least informative)"))
    return sorted(candidates, key=lambda c: -c["coverage"])

def adopt(session: Session, gap: Gap, candidate: dict, name: str,
          selected_by: str) -> Distinction:
    """Outside selection of a kernel-drafted candidate. Both parties recorded."""
    responder = (lambda text=candidate["draft"]: Gap(text))
    d = session.self_model.teach(gap, candidate["keys"], responder, name)
    d.seed_cases.append(f"drafted by kernel ({candidate['basis']}), "
                        f"selected by {selected_by}")
    return d

cannot("judge the adequacy of a self-drafted responder",
       "adequacy is judged by the questions that arrive AFTER adoption; "
       "at drafting time only coverage of past failures is measurable", "choice")

# ================================================================ C. DIGEST
choose("digest policy",
       "digest(budget) selects: choices with the longest consequence text "
       "(proxy for weight), newest horizon entries, ledger totals, pressure "
       "hotspots, self-model state. Every omission is counted and the digest "
       "act is itself filed in the ledger as a collapse with residue",
       "full dumps (unreadable -- honesty as noise); silent summaries "
       "(readable -- honesty lost); reader-model-based selection (no reader "
       "model exists yet)",
       "the proxy 'longest consequence text = most consequential' is crude "
       "and registered; a digest is a reading the kernel gives of itself, "
       "and like every reading it discards")

@dataclass
class Digest:
    lines: list
    omitted: dict
    reading_instructions: str
    def __repr__(self):
        body = "\n".join("  " + l for l in self.lines)
        om = ", ".join(f"{k}:{v}" for k, v in self.omitted.items())
        return (f"<Digest>\n{body}\n  --- omitted: {om}\n"
                f"  --- {self.reading_instructions}\n</Digest>")

def digest(session: Session, budget: int = 3) -> Digest:
    """The kernel reads itself for a reader. The reading is priced."""
    lines, omitted = [], {}

    ranked = sorted(CHOICES, key=lambda c: -len(c["consequence"]))
    for c in ranked[:budget]:
        lines.append(f"CHOICE {c['name']}: {c['chosen']}")
    omitted["choices"] = max(0, len(CHOICES) - budget)

    for h in HORIZON[-budget:]:
        lines.append(f"CANNOT ({h['forced_by']}): {h['claim']}")
    omitted["horizon"] = max(0, len(HORIZON) - budget)

    if session.ledger:
        total_discarded = q(sum(w for e in session.ledger
                                for _, w in e.get("discarded", [])))
        lines.append(f"LEDGER: {len(session.ledger)} collapses; "
                     f"total discarded weight {total_discarded}")
    else:
        lines.append("LEDGER: no collapses yet")

    hot = sorted(session.pressure.items(), key=lambda kv: -len(kv[1]))[:budget]
    for key, cases in hot:
        lines.append(f"PRESSURE {key}: {len(cases)} blur events")
    omitted["pressure_keys"] = max(0, len(session.pressure) - budget)

    sm = session.self_model
    lines.append(f"SELF: {len(sm.patterns)} patterns "
                 f"({len(sm.learned)} learned), {len(sm.unparsed)} unparsed pending")

    d = Digest(
        lines=lines, omitted=omitted,
        reading_instructions=("each line abbreviates a register entry; the "
                              "registers remain the record; this digest is a "
                              "collapse and is filed as one"))
    session.ledger.append(dict(
        kept=f"digest of {len(lines)} lines",
        discarded=[(k, v) for k, v in omitted.items() if v],
        reason="readability requires compression; compression discards",
        purity_notes=0, kept_weight=None))
    return d

cannot("produce a digest that loses nothing",
       "a summary that loses nothing is the original; readability is bought "
       "with omission, and the omissions receipt is the purchase record", "theorem")

# ================================================================ D. COMPOSITION
choose("bundle composition",
       "nested bundles flatten: path label 'outer/inner', weights multiply "
       "(quantized), depth recorded as an underdetermination meter; paths "
       f"falling below liveness {LIVENESS} after multiplication are pruned "
       "WITH a receipt (unlike explore's registered receipt-free cutoff)",
       "keeping the tree unflattened (faithful but unreadable at depth); "
       "renormalizing after each level (hides how thin deep paths become)",
       "multiplied weights shrink fast: compounded underdetermination is "
       "visibly thin, which is honest -- deep possibility IS thin")

@dataclass
class ComposedBundle:
    outcomes: list          # [(path, weight, value)]
    depth: int
    pruned: list            # [(path, weight)] -- receipts for thin paths
    def __repr__(self):
        inner = ", ".join(f"{p}:{w:.3f}" for p, w, _ in self.outcomes)
        return (f"<ComposedBundle depth={self.depth} {inner}"
                f" | pruned:{len(self.pruned)}>")

def compose(b: Bundle) -> ComposedBundle:
    """Flatten exploration-inside-exploration with path provenance."""
    flat, pruned, depth = [], [], 1

    def walk(outcomes, prefix, w_acc, d):
        nonlocal depth
        depth = max(depth, d)
        for region, w, value in outcomes:
            path, wt = f"{prefix}{region}", q(w_acc * w)
            if isinstance(value, Bundle):
                walk(value.outcomes, path + "/", wt, d + 1)
            elif isinstance(value, ComposedBundle):
                walk([(p, ww, vv) for p, ww, vv in value.outcomes],
                     path + "/", wt, d + value.depth)
            elif wt <= LIVENESS:
                pruned.append((path, wt))
            else:
                flat.append((path, wt, value))
    walk(b.outcomes, "", 1.0, 1)
    return ComposedBundle(sorted(flat, key=lambda o: -o[1]), depth, pruned)

def collapse_composed(session: Session, cb: ComposedBundle, reason: str):
    """Collapse over full paths: the receipt names entire discarded subtrees."""
    if not cb.outcomes:
        return Gap("collapse of a fully-pruned composition: every deep path "
                   "was thinner than liveness; underdetermination exceeded "
                   "the resolution of action")
    kept = cb.outcomes[0]
    session.ledger.append(dict(
        kept=kept[0], kept_weight=kept[1],
        discarded=[(p, w) for p, w, _ in cb.outcomes[1:]] + cb.pruned,
        reason=reason, purity_notes=0, depth=cb.depth))
    return kept[2]

cannot("act at underdetermination depth beyond action's resolution",
       "when every composed path is thinner than the liveness floor, the "
       "evidence supports exploration, not action; the kernel returns the "
       "gap instead of manufacturing a preference", "choice")
