"""
Truth as distribution: a tiny probabilistic program with rejection sampling.
Run: python3 probabilistic_truth.py

A probabilistic program denotes not a value but a DISTRIBUTION over values.
Running it = sampling a possible world.
`observe` = conditioning the multiverse: worlds inconsistent with
evidence are pruned. And the OUTPUT DEMANDS INTERPRETATION:
it is a sample, i.e. evidence about the answer, not the answer.
"""
import random

def flip(p): return random.random() < p

def model():
    """A possible world: is the lawn wet, and why?"""
    rain      = flip(0.2)
    sprinkler = flip(0.3)
    wet_lawn  = (rain and flip(0.9)) or (sprinkler and flip(0.8))
    return {"rain": rain, "sprinkler": sprinkler, "wet": wet_lawn}

def infer(evidence, query, n=200_000):
    """Rejection sampling: generate multiverse, keep worlds matching evidence."""
    kept = 0; hits = 0
    for _ in range(n):
        w = model()
        if all(w[k] == v for k, v in evidence.items()):   # observe
            kept += 1
            hits += w[query]
    return hits / kept, kept

if __name__ == "__main__":
    random.seed(42)
    prior, _        = infer({}, "rain")
    posterior, kept = infer({"wet": True}, "rain")
    print(f"P(rain)              = {prior:.3f}   (across all worlds)")
    print(f"P(rain | lawn wet)   = {posterior:.3f}   (across {kept} surviving worlds)")
    print()
    print("Interpretive burdens the language hands to YOU:")
    print(" - this is an ESTIMATE; its error shrinks as 1/sqrt(kept)")
    print(" - rerun with another seed: the 'answer' moves")
    print(" - the number is only as good as the model's assumptions,")
    print("   which appear nowhere in the output")
