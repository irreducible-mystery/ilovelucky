# Identity as Path: What HoTT Did to "Sameness"

## 1. The flattening everyone inherited

Every mainstream language treats equality as a *judgment that returns a bit*. `a == b` — yes or no, and if yes, the yes carries no further information. Two yeses are the same yes. This is Leibniz flattened: identity of indiscernibles, collapsed to a boolean.

Martin-Löf type theory already broke this quietly in the 1970s by making equality a *type*: `Id A a b` is the type of *identifications* of `a` with `b`. A proof of equality is an object. But for thirty years, almost everyone assumed the type was trivial — that any two proofs of `a = b` must themselves be equal (the axiom of Uniqueness of Identity Proofs, UIP, or Streicher's Axiom K). The assumption felt so obvious it was rarely even stated: *how could there be two genuinely different ways for a thing to be itself?*

## 2. The Hofmann–Streicher shock

In 1994 Hofmann and Streicher built a model of type theory in **groupoids** where UIP fails. Types are interpreted as groupoids (categories where every morphism is invertible); elements are objects; and *proofs of equality are the morphisms*. In a groupoid there can be many distinct isomorphisms between two objects — hence many distinct proofs that `a = b`, and the difference between the proofs is *mathematically real*.

The philosophical detonation: identity has **internal structure**. The question is not "are these the same?" but "*in how many ways* are these the same, and are those ways themselves the same as each other?" — and that second question iterates, forever. Equality proofs between equality proofs between equality proofs: an infinite tower, which is exactly the structure of a *space* — points, paths, homotopies between paths, homotopies between homotopies. Hence: **Homotopy Type Theory**. The identity type `Id A a b` is the *path space* between `a` and `b` in the space `A`.

## 3. Univalence: the axiom mathematics was already using illegally

Working mathematicians have always said "the cyclic group of order 2 *is* Z/2Z" while knowing the set-theoretic encodings differ. Set theory makes this identification a lie — a convenient abuse of notation. Voevodsky's **univalence axiom** makes it a theorem-schema of the foundation itself:

```
(A ≃ B) ≃ (A = B)
```

Equivalence of types *is* identity of types. Isomorphic structures are literally equal — and, crucially, **each distinct equivalence yields a distinct proof of equality**. The two isomorphisms of Z/2Z with itself (identity and the swap) become two distinct *self-identifications* — two distinct paths from the type to itself. Identity is not just structured; it can be *nontrivially self-related*. A thing can be the same as itself in more than one way.

Programming consequence (still mostly unrealized): if `A = B` via univalence, every program written against `A` transports automatically along the path to work on `B`. Refactoring-as-path-transport. The proof of sameness *is* the migration function. Cubical Agda implements this computationally — `transport` along a path actually runs.

## 4. What this does to the essay's other axes

- **Negation:** in HoTT, `¬(a = b)` says the path space is empty — but there are also types where `a = b` is *not provable and not refutable*, i.e., the path space's inhabitation is open. Identity questions inherit constructive openness.
- **Truth:** propositions get *classified by their identity structure*. A "mere proposition" is a type where all proofs are equal (at most one way to be true); a "set" is a type where all identity proofs are equal (things are the same in at most one way); higher types have genuinely plural identities. Truth-flatness becomes a *special case* you must prove, not an assumption you get free.
- **Fractals:** the tower of iterated identity types (paths, paths-between-paths, ...) is literally a self-similar structure — the identity type of an identity type is again an identity type. Sameness is fractal.

## 5. The gap it exposes

No production language lets values carry structured identity. Database identity (primary keys), object identity (addresses), value identity (structural equality) — all flat. Yet the real-world problems screaming for structured identity are everywhere: schema migration (in how many ways does the old schema map to the new?), entity resolution (these two customer records are "the same" — *via which* correspondence, with what confidence?), API versioning. We solve all of these with ad-hoc migration scripts that are, unrecognized, *untyped path objects*. HoTT is the theory of what those scripts are.
