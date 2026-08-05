# The Hermeneutics of Output: When Answers Need Interpreters

## 1. The naive contract

The unexamined contract of computing: *you ask, the machine answers, the answer is the answer*. Output is transparent — it means what it says, its meaning is exhausted by its content, and no interpretive act stands between the bytes and the truth. This contract holds for `2+2 ⇒ 4` and quietly fails almost everywhere else. The failures are not bugs; they are places where the output is a **text** — something demanding a reader with a theory.

## 2. A taxonomy of outputs that demand hermeneutics

**The sample pretending to be an answer (probabilistic programming).** An MCMC run in Stan returns numbers, but the numbers are *evidence about* the posterior, not the posterior. Between output and meaning stands an entire interpretive discipline: convergence diagnostics (R̂, effective sample size, divergent transitions), multimodality checks, sensitivity analysis. A Stan output read naively is routinely, silently wrong; the field's response was to build *diagnostics* — meta-outputs about the trustworthiness of outputs — which themselves require interpretation (what R̂ threshold? contested). The regress is real and is managed, never closed, by community hermeneutic tradition (Gelman et al.'s workflow papers are exegetical manuals).

**The plurality pretending to be a result (ASP, SAT, constraint solvers).** clingo returns three answer sets. What *is* that output? Not three answers to one question — it's the statement *your axioms underdetermine the world in exactly these three ways*. The correct response might be: pick any (they're interchangeable for your purpose), or add constraints (the plurality reveals an unstated requirement), or study the differences (the plurality is the finding). The solver cannot tell you which, because that depends on why you asked — the output's meaning lives in the question's pragmatics, which the language cannot see.

**The silence pretending to be falsity (Prolog).** `?- flies(tweety). false.` — this "false" means only *unprovable from what I was given*. Its correct interpretation depends on an assumption (closed world) that lives entirely outside the program text. The same output means "no" for a flight-schedule database and "unknown" for a zoology knowledge base — identical bytes, opposite meanings, disambiguated only by the reader's model of the database's completeness. Negation-as-failure outsources its soundness to the reader.

**The witness of absence (type errors, unification failures).** A Haskell or Rust type error is a *proof that no valid reading of your program exists* — but rendered as a linearized, often misplaced blame report. The error's location is where inference *detected* the conflict, not where the mistake *is*; experienced developers read type errors the way critics read symptoms — against the text's surface, toward a latent cause. Elm's celebrated error messages are a hermeneutic achievement, not a technical one: same information, curated for a reader.

**The number that carries its own doubt (NaN, and its absence elsewhere).** IEEE NaN propagates through pipelines as a contaminating trace — the output `NaN` means *somewhere upstream, an impossible operation occurred*, with all provenance destroyed. It's an interpretable symptom with the case file burned. Contrast what it could be: an error value carrying its origin (as in some effect systems). NaN is hermeneutics forced on the reader precisely because the machine discarded the evidence.

**The score pretending to be a judgment (ML model outputs).** Logits, similarities, confidences: numbers whose interpretation (threshold? calibrated? comparable across inputs?) is entirely conventional, revisable, and usually undocumented. And now: **LLM output** — the extreme case, where the output is literal natural-language text, interpretable by construction, with no accompanying theory of its own reliability. The oldest problem in the humanities (how to read testimony of uncertain authority) has become the newest problem in computing, and computing arrived without the humanities' three thousand years of tooling.

## 3. The structural reason the loop can't be closed from inside

Why can't the language just... include the interpretation? Three compounding barriers:

1. **Tarski**: a language cannot contain its own truth predicate; a system's outputs about its own reliability are themselves outputs, needing the same scrutiny (the diagnostics regress above).
2. **Pragmatics**: an output's meaning depends on the asker's purpose, which is not in the program. The three answer sets mean different things to different askers.
3. **Gödel/self-model incompleteness**: a system's calibrated self-assessment cannot be complete. But — the crucial opening — *it can be honest about where it is incomplete*. Incompleteness is forced; unmarked incompleteness is a design choice.

## 4. What partial closure would look like

The gap is not binary. Languages can carry *more* of their outputs' interpretation than they do:

- **Provenance-carrying values**: every output knows its data sources and the assumptions (closed-world? priors? thresholds?) it passed through. (Research systems exist — provenance semirings in databases — never mainstreamed.)
- **Assumption-indexed answers**: Prolog's `false` replaced by `false-under-CWA(these predicates)`; a query answer that names the axioms it leans on hardest.
- **Sensitivity as standard output**: not just the answer, but the smallest perturbation of inputs/assumptions that flips it. (A verdict that flips under a rounding error and a verdict robust to everything are currently *printed identically*.)
- **Typed epistemic status**: return types distinguishing proven / sampled / defaulted / testimony-derived — the ASP `not`/`-` distinction, and the paraconsistent (μ,λ) annotation, generalized to all outputs.

Each item exists somewhere in research. None is ambient. The composite vision — a language whose every output arrives wearing its own reading instructions: provenance, load-bearing assumptions, sensitivity, epistemic type — is, I think, the single most consequential unbuilt thing in programming language design. Not because it closes the hermeneutic loop (it can't), but because it would move the reader's burden from *reconstructing* the interpretation to *checking* it.

## 5. Coda: the reader was always part of the machine

The deepest revision this forces: a computation is not complete when the process halts. It is complete when the output has been *read* — and the reading is a second computation, running on humans, using theories (of the program's assumptions, of the domain, of the sources) that the program itself does not contain. Every deployed system is a human-machine hermeneutic circuit, and we have engineering disciplines for exactly half of it.
