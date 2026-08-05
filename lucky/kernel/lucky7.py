"""
lucky7 -- the authority boundary. Forced by an external experiment
(comparisons/08) that reproduced v6 and measured its central defect:

    Session6 owns its own SourceGraph. The measured party owns the
    measuring instrument. The 'sophisticated adversary' of rot test 2
    was priced at 'infrastructure' -- but under local ownership that
    infrastructure is two free function calls in the adversary's own
    process. Measured: SOPHISTICATED == HONEST at 0.95. Under an
    external, read-only graph: SOPHISTICATED collapses to 0.60,
    ROTTEN's level. 'Until that boundary exists in the real kernel,
    every grounding factor remains a self-certified receipt.'

v7 builds the boundary -- and registers where the error RELOCATES,
because it does not die:

  1. Authority        : owns the only writable graph; pre-registers
     track records; issues read-only views.
  2. ReadOnlyGraph    : the session-side view; write attempts return
     an informational anomaly (refused at the boundary, on the record).
  3. Session7         : grounding is computed against the view. A
     session WITHOUT an authority still runs -- and its grounding
     report says 'self-certified' in the factor's own note, priced by
     a self-certification discount.
  4. The relocation   : who grounds the Authority? Nothing in v7. The
     self-certification error is not eliminated; it is MOVED across a
     process boundary, where the adversary must compromise a party
     outside their own code. Cost raised, regress intact, said on the
     instrument. (design/08 E3 pattern: inherent errors flee to the
     edges; the edge is now the Authority's own ground.)

Extends lucky6. Nothing patched in place.
"""
from lucky1 import Ev, Anomaly, Gap, q, choose, cannot
from lucky2 import SourceGraph
from lucky5 import Origin
from lucky6 import Session6, STANDING_PRICE, CORROBORATION_FLOOR
from typing import Optional

# ================================================== choices
choose("authority boundary",
       "track records live in an Authority OUTSIDE the session under "
       "test; sessions hold a read-only view; session-side writes are "
       "refused at the boundary and the refusal is itself a receipt",
       "session-owned graphs (v6: measured SOPHISTICATED==HONEST at "
       "0.95 -- the measured party owned the instrument, so grounding "
       "was a self-certified receipt); a global singleton authority "
       "(one capturable choke point, and an unregisterable intake)",
       "the boundary does not verify the Authority: who grounds the "
       "grounder is the same regress, relocated across a process line. "
       "What changed is the PRICE: the adversary must now compromise a "
       "party outside their own process, not call record() twice")

SELF_CERT_DISCOUNT = 0.75
choose("self-certification discount",
       f"a session grounding itself against its OWN graph has its factor "
       f"multiplied by {SELF_CERT_DISCOUNT} and labeled self-certified; "
       "sessions with an external view pay no discount",
       "forbidding self-certified sessions (a session with no authority "
       "available must still be able to run and say so); no discount "
       "(v6: the self-certified 0.95 wore the same costume as a "
       "boundary-certified 0.95)",
       "the magnitude is an underived carving, registered as such; the "
       "ORDER is the design: boundary-certified > self-certified at "
       "equal paperwork")

# ================================================== the boundary
class ReadOnlyGraph:
    """Session-side view of an Authority's graph. Reads pass through;
    writes are refused at the boundary, on the record."""
    def __init__(self, graph: SourceGraph, refusals: list):
        self._g = graph
        self._refusals = refusals

    def reliability(self, source, **kw):
        return self._g.reliability(source, **kw)

    def _group_of(self, source):
        return self._g._group_of(source)

    def record(self, source, score):
        a = Anomaly("write refused at authority boundary", "ReadOnlyGraph",
                    (f"session attempted record({source!r}, {score}); the "
                     "track-record store is not the session's to write",))
        self._refusals.append(a)
        return a

    def vouch(self, voucher, target, weight=1.0):
        a = Anomaly("write refused at authority boundary", "ReadOnlyGraph",
                    (f"session attempted vouch({voucher!r} -> {target!r}); "
                     "vouching is testimony to the Authority, not an edit",))
        self._refusals.append(a)
        return a

    def correlate(self, *sources):
        a = Anomaly("write refused at authority boundary", "ReadOnlyGraph",
                    (f"session attempted correlate{sources!r}",))
        self._refusals.append(a)
        return a

class Authority:
    """Owns the only writable graph. Pre-registers track records; issues
    read-only views. v7 deliberately does NOT model how the Authority
    itself is grounded -- that absence is the registered relocation."""
    def __init__(self, name: str):
        self.name = name
        self.graph = SourceGraph()
        self.refusals: list = []

    def register(self, source: str, score: float, basis: str):
        """Track records enter the Authority with a stated basis --
        the Authority is held to the intake discipline it enforces."""
        self.graph.record(source, score)
        self.graph.vouches.setdefault("__bases__", []).append(
            (source, basis))

    def view(self) -> ReadOnlyGraph:
        return ReadOnlyGraph(self.graph, self.refusals)

# ================================================== session7
class Session7(Session6):
    """Session6 whose grounding is computed against an external view
    when one is provided -- and which confesses self-certification when
    one is not."""
    def __init__(self, authority: Optional[Authority] = None, **kw):
        super().__init__(**kw)
        if authority is not None:
            self.graph = authority.view()
            self._certification = f"boundary-certified by {authority.name!r}"
            self.take("authority", authority.name,
                      Origin("external track-record store; its own ground "
                             "is not modeled here (registered relocation)",
                             by=authority.name))
        else:
            self._certification = "self-certified"
            self.take("authority", None, None)     # anonymous, honestly

    def grounding(self) -> dict:
        g = super().grounding()
        if self._certification == "self-certified":
            g["factor"] = q(g["factor"] * SELF_CERT_DISCOUNT)
            g["note"] = ("SELF-CERTIFIED: the session owns its own track "
                         "records; this factor is the session's word about "
                         "the session's word (discounted "
                         f"x{SELF_CERT_DISCOUNT}). " + g["note"])
        else:
            g["note"] = (f"{self._certification}: track records live "
                         "outside this session's write access. Who grounds "
                         "the grounder is NOT answered here -- the regress "
                         "relocated, priced across a process boundary. "
                         + g["note"])
        g["certification"] = self._certification
        return g

# ================================================== horizon
cannot("ground the grounder",
       "the Authority's track records are the Authority's testimony; "
       "no chain of authorities terminates (same regress, one level up). "
       "v7's contribution is the PRICE and the LABEL: compromising the "
       "store now requires reaching outside the session's process, and "
       "every grounding factor states which kind of certification "
       "produced it. An Authority captured by the adversary reproduces "
       "the v6 defect wholesale -- at higher cost, invisibly to these "
       "instruments. Failure register, trajectory 3 (capture), updated",
       "structure")
