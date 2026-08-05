# The Triple Convergence: Linear Logic, Quantum Mechanics, and Rust

## 1. Three fields, one discovery

Between 1987 and 2015, three communities with almost no overlap — proof theorists, quantum physicists, and systems programmers — independently converged on the same structural insight: **classical logic's treatment of truth as infinitely copyable and freely discardable is a special case, not the ground truth.** The general case is that *stuff is conserved*.

## 2. Girard: deleting the structural rules

Classical and intuitionistic logic share two "structural rules" so ingrained they were barely noticed for two millennia:

- **Contraction**: from `A, A ⊢ B` infer `A ⊢ B` — you may use an assumption as many times as you like. Truths are copyable.
- **Weakening**: from `⊢ B` infer `A ⊢ B` — you may ignore assumptions. Truths are discardable.

Girard's **linear logic** (1987) deletes both. Now `A ⊢ A ⊗ A` is *not derivable*: having A does not give you two A's. Propositions behave like resources — a dollar, not a fact about dollars. The conjunctions split in two (`⊗` "both, resources combined" vs `&` "your choice of either, but only one"), the disjunctions split (`⊕` vs `⅋`), and negation `A⊥` becomes **role reversal**: the consumer's view of the producer's resource, debt as the negation of credit. Not falsity — *duality of perspective in an exchange*.

Critically, Girard didn't abolish classical logic; he *caged* it. The exponential modality `!A` means "A, with unlimited copying and discarding re-enabled." Classical logic is linear logic restricted to `!`-ed propositions. Copyability becomes a *marked privilege* instead of an invisible assumption.

## 3. Physics: the universe was already linear

Quantum mechanics enforces the same regime physically:

- **No-cloning theorem** (Wootters–Zurek 1982): there is no physical operation taking an unknown quantum state `|ψ⟩` to `|ψ⟩⊗|ψ⟩`. Contraction is *physically impossible*.
- **No-deleting theorem**: unknown states can't be discarded against a copy. Weakening fails too.
- Unitary evolution is reversible — information conserved — until **measurement**, the one irreversible, classicalizing act.

So the type system a quantum programming language *needs* is exactly linear: every qubit used exactly once per operation, no duplication, no silent discard. And indeed Selinger's QPL, the Proto-Quipper line, and Silq all use linear or affine typing for quantum data, with classical (copyable) data marked separately — a literal implementation of Girard's `!` boundary as the quantum/classical membrane. The deep reading: **classical information is `!`-quantum information** — what survives decoherence is precisely what became copyable.

## 4. Rust: linearity as memory safety

Rust's ownership system is affine logic (linear logic plus weakening — you may drop values, you may not duplicate them):

```rust
let x = String::from("hello");
let y = x;          // move: x is now unusable
println!("{}", x);  // COMPILE ERROR: value borrowed after move
```

`String` cannot be copied implicitly because it owns heap memory; ownership transfer invalidates the source. This is contraction-failure as a *borrow checker error message*. And Rust rebuilt Girard's cage exactly, without (initially) knowing it:

| Linear logic | Rust |
|---|---|
| linear proposition | owned value |
| `!A` (exponential) | `Copy` types / `Rc<A>` / `Arc<A>` |
| dereliction (use `!A` once) | `Rc::deref` |
| explicit duplication of `!A` | `Rc::clone` (visible, counted) |
| `A ⊸ B` (consume A, produce B) | `fn(A) -> B` by-value |
| borrowed access without consumption | `&A` / `&mut A` (fractional/exclusive) |

What Rust proved at industrial scale: the linear regime is not an academic curiosity — it is *the* discipline that makes manual memory management safe and data races impossible (`&mut` exclusivity is contraction-denial applied to aliasing). Millions of programmers now think in conservation-of-stuff daily, without knowing they're running Girard's proof theory.

## 5. Why the convergence had to happen

All three fields hit the same wall: **aliasing of the unique**. In logic: resource-sensitive reasoning (Girard came via semantics of computation). In physics: quantum states are unclonable *because amplitudes aren't probabilities* — copying would let you violate uncertainty. In systems: two writers to one address is the root of nearly all memory unsafety and race conditions. Each field discovered that its pathology came from an unexamined classical assumption — that having a thing means being able to have it twice — and each built the same cure: **typed conservation**.

The metaphysical statement underneath: *facts* are the copyable shadows of *things*, and a logic of things must precede the logic of facts. Classical logic did it backwards for two thousand years because logicians worked with sentences (freely copyable ink) rather than with the referents of sentences. Computation — where the sentence and the thing coincide — forced the correction.

## 6. What's still missing

- Full linear logic's `⅋` (par) and classical linear duality have no mainstream programming counterpart; session types (typed conversations, where duality = my-send-is-your-receive) are the closest and remain niche.
- No language spans the full gradient: quantum-linear at the bottom, affine (Rust) in the middle, classical-copyable (`!`) at the top, *with typed passage between all three levels*. Each existing language freezes one level.
- Erasure remains untheorized: Rust's `drop` is weakening, quantum forbids it, thermodynamics *prices* it (Landauer: erasing a bit costs kT·ln2 of entropy). A language where discarding data has a *typed cost* would unify the triangle — and would incidentally be the first language able to express privacy deletion (GDPR) as semantics instead of policy.
