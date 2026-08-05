# ilovelucky — The Hidden Metaphysics of Programming Languages

> Every programming language is a frozen argument about what reality is.
> Its bugs are the return of what it repressed.

This repository is an inquiry into the buried metaphysical commitments of
programming languages — how they handle **truth, NEGATION, identity, time,
evolution, self-reference, infinity, asynchrony, asymmetry** — pursued in two
modes: **essays** that excavate the assumptions, and **runnable examples**
that let you execute the metaphysics and watch it behave.

## Structure

```
├── metaphysics_of_programming_languages.md   The main essay (start here)
├── essays/
│   ├── 01-identity-as-path.md                HoTT: sameness acquires structure
│   ├── 02-linear-logic-quantum-rust.md       The triple convergence on conservation
│   ├── 03-paraconsistency-in-the-field.md    Contradiction-tolerant logic, deployed
│   └── 04-hermeneutics-of-output.md          When answers need interpreters
└── examples/
    ├── negation/
    │   ├── prolog_negation_as_failure.pl     Absence as evidence; learning destroys truth
    │   ├── asp_two_negations.lp              Ignorance vs. known falsehood, in one rule
    │   ├── asp_plural_worlds.lp              Truth as equilibrium; plural realities
    │   ├── belnap_four_valued.py             ✓ Contradiction quarantined, not explosive
    │   └── paraconsistent_para_analyzer.py   ✓ Routing on conflict itself (robot control)
    ├── truth/
    │   ├── lean_constructive_truth.lean      Two truths, one language; the noncomputable border
    │   └── probabilistic_truth.py            ✓ Truth as distribution; output as evidence
    ├── time/
    │   ├── janus_reversible.py               ✓ A universe where forgetting is forbidden
    │   └── erlang_no_global_now.erl          No global now; identity as mortal PID
    ├── identity/
    │   ├── rust_linear_identity.rs           Having a thing ≠ having it twice
    │   └── minikanren_negotiated_identity.py ✓ Identity as promise; programs run backwards
    ├── infinity/
    │   └── haskell_actual_infinity.hs        Actual infinity; esse est percipi
    └── self_reference/
        └── lisp_metacircular.py              ✓ Interpretation legal, truth illegal (Tarski's gap)
```

✓ = pure Python, runs anywhere (`python3 <file>`). Others need their toolchains:
`swipl` (Prolog), `clingo` (ASP), `lean` (Lean 4), `runghc` (Haskell),
`erl` (Erlang), `rustc` (Rust). Each file's header has its run command.

## The five theses (short form)

1. **Negation is the deepest fault line.** Failure-to-prove, known-falsehood,
   refutation-function, non-explosive contradiction, and banned-destruction are
   five different things that the classical boolean fused into one operator.
   The fusion is the hidden assumption.
2. **Every language trades expressiveness against self-knowledge**
   (Gödel/Turing/Tarski, appearing as a design constraint).
3. **Purity is always breached, and the breach is the data**: cut, unsafePerformIO,
   `unsafe`, `noncomputable`, postulates. Map the escape hatches and you map
   reality's pressure on each worldview.
4. **Negation, identity, and time are not independent axes** — choose one and
   the others follow. Languages are coherent metaphysical systems, not feature-bags.
5. **Every language is a theory of what can be safely ignored** — and its
   characteristic bugs are exactly the return of the repressed.

## The gaps (what no language yet says well)

Graded source-tracked belief as ambient semantics · continuous time ·
speakable emergence · principled forgetting · outputs that carry their own
reading instructions · calibrated self-models honest about their incompleteness.

---

*Programming languages are the only philosophical tradition whose arguments
are executed.*
