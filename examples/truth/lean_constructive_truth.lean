/- Constructive truth in Lean 4: negation as refutation machine,
   and the customs checkpoint between two truths.
   Check with: lean lean_constructive_truth.lean  (Lean 4) -/

-- Negation is DEFINED as a function into the absurd:
-- ¬P  :=  P → False
example (P : Prop) (hp : P) (hnp : ¬P) : False := hnp hp
-- To assert ¬P you must BUILD the machine that eats proofs of P.

-- P → ¬¬P is constructive (easy direction):
theorem dn_intro (P : Prop) : P → ¬¬P := fun hp hnp => hnp hp

-- ¬¬P → P is NOT provable constructively. Try it: there is no way
-- to extract a proof of P from a mere refutation-of-refutation.
-- theorem dn_elim (P : Prop) : ¬¬P → P := fun h => _   -- stuck forever

-- ...unless you cross the border into classical logic:
theorem dn_elim_classical (P : Prop) : ¬¬P → P := by
  intro h
  by_cases hp : P   -- uses Classical.em: the law of excluded middle
  · exact hp
  · exact absurd hp h

-- The border is MARKED. Definitions that lean on classical choice
-- must be declared `noncomputable`: they assert existence
-- without being able to produce the witness.
noncomputable def choose_something (h : ∃ n : Nat, n > 5) : Nat :=
  Classical.choose h
-- `noncomputable` is a metaphysical customs stamp:
-- beyond this point, truth no longer executes.

-- Constructive existence, by contrast, IS a program:
def concrete_witness : { n : Nat // n > 5 } := ⟨6, by decide⟩
#eval concrete_witness.val   -- 6. This truth runs.
