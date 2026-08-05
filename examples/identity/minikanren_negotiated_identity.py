"""
A micro-miniKanren: identity as NEGOTIATION (unification), and
programs that run backwards because they never chose a direction.
Run: python3 minikanren_negotiated_identity.py

In relational programming, `eq(a, b)` doesn't TEST sameness --
it CONSTRAINS the future so that a and b become the same.
Identity is a promise, not a fact. And because append is a RELATION,
not a function, it splits lists as readily as it joins them:
the input/output asymmetry -- the root of irreversibility -- was
never introduced.
"""
from itertools import islice, count

class Var:
    _c = count()
    def __init__(self): self.i = next(Var._c)
    def __repr__(self): return f"_{self.i}"

def walk(t, s):
    while isinstance(t, Var) and t in s: t = s[t]
    return t

def unify(a, b, s):
    a, b = walk(a, s), walk(b, s)
    if a is b or a == b and not isinstance(a, Var): return s
    if isinstance(a, Var): return {**s, a: b}
    if isinstance(b, Var): return {**s, b: a}
    if isinstance(a, tuple) and isinstance(b, tuple) and len(a) == len(b) == 2:
        s1 = unify(a[0], b[0], s)
        return unify(a[1], b[1], s1) if s1 is not None else None
    return None

# Goals: substitution -> stream of substitutions
def eq(a, b):
    def goal(s):
        s1 = unify(a, b, s)
        if s1 is not None: yield s1
    return goal

def disj(g1, g2):
    def goal(s):
        # interleave: fair choice between alternative worlds
        it1, it2 = g1(s), g2(s)
        while True:
            done = 0
            for it in (it1, it2):
                try: yield next(it)
                except StopIteration: done += 1
            if done == 2: return
    return goal

def conj(g1, g2):
    def goal(s):
        for s1 in g1(s):
            yield from g2(s1)
    return goal

def fresh2(f):
    def goal(s): return f(Var(), Var())(s)
    return goal

NIL = "()"
def cons(h, t): return (h, t)

def appendo(l, r, out):
    """append AS A RELATION: no privileged inputs or outputs."""
    def goal(s):
        g = disj(
            conj(eq(l, NIL), eq(r, out)),
            fresh2(lambda h, t: fresh2(lambda rest, _:
                conj(eq(l, cons(h, t)),
                     conj(eq(out, cons(h, rest)),
                          lambda st: appendo(t, r, rest)(st)))))
        )
        yield from g(s)
    return goal

def to_list(t, s):
    t = walk(t, s)
    out = []
    while isinstance(t, tuple):
        out.append(walk(t[0], s)); t = walk(t[1], s)
    return out

def from_list(xs):
    out = NIL
    for x in reversed(xs): out = cons(x, out)
    return out

if __name__ == "__main__":
    # Forward: append [1,2] [3] = ?
    q = Var()
    s = next(appendo(from_list([1,2]), from_list([3]), q)({}))
    print("forward :  append [1,2] [3] =", to_list(q, s))

    # BACKWARD: which pairs (X, Y) append to [1,2,3]? ALL of them:
    x, y = Var(), Var()
    print("backward:  all splits of [1,2,3]:")
    for s in islice(appendo(x, y, from_list([1,2,3]))({}), 4):
        print("           ", to_list(x, s), "+", to_list(y, s))
    print()
    print("The same code computed the function AND its inverse, because")
    print("it never was a function -- it was a relation all along.")
