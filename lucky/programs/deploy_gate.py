"""
deploy_gate.py -- ONE real program, written to answer one question:
    what would make one real program want the 300 lines?

This is USE of the existing kernel, not kernel architecture. No new
registers, no new instruments, no v8. It imports lucky3 and consumes it.

The program: a CI deploy gate. Test suites report results; the gate
decides what happens to the release. This is among the most common
programs in the world, and it is almost always written over `bool`.

The hypothesis under test:
    a program wants the four corners exactly when its ACTION SPACE is
    finer than its CONDITION TYPE. A deploy gate has (at least) five
    distinct correct next actions:
        DEPLOY            -- ship it
        BLOCK + FILE BUG  -- the code is bad, someone must fix it
        RERUN / QUARANTINE-- the suites DISAGREE; the tests are the
                             problem, not (yet) the code
        CHECK CI INFRA    -- there are NO results; the pipeline is the
                             problem, not the code
        CANARY            -- the pass is real but fragile; ship to 1%
    `bool` has two values. The collapse is not hypothetical: the
    boolean gate below contains a real, famous bug class, exhibited
    live in scenario 3.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "kernel"))

from lucky1 import Testimony
from lucky3 import testify3, verdict3

# ---------------------------------------------------------------- Gate A
# The gate as it is actually written in the world. Two actions.

def gate_bool(results: dict[str, bool]) -> str:
    """results: suite name -> passed?  Missing suites simply absent."""
    if all(results.values()):          # <- the standard idiom
        return "DEPLOY"
    return "BLOCK"

# ---------------------------------------------------------------- Gate B
# The same gate consuming the kernel. Suites become testimony; the
# verdict's REGION routes the action; flip_distance grades commitment.

def gate_lucky(results: dict[str, bool]) -> str:
    ts = []
    for suite, passed in results.items():
        ts.append(Testimony(suite, "for" if passed else "against", 0.9))
    ev = testify3(*ts)
    v = verdict3(ev)
    if v.region == "true":
        return "CANARY (fragile pass)" if v.flip_distance < 0.10 else "DEPLOY"
    if v.region == "false":
        return "BLOCK + FILE BUG"
    if v.region == "inconsistent":
        return "RERUN / QUARANTINE FLAKY SUITES (suites disagree; "\
               "investigate the tests, not the code)"
    if v.region == "paracomplete":
        return "HOLD + CHECK CI INFRA (no evidence either way; "\
               "the pipeline is the problem, not the code)"
    return f"GATHER MORE (blur, {v.tendency})"

# ---------------------------------------------------------------- scenarios
SCENARIOS = [
    ("1. clean pass",
     {"unit": True, "integration": True, "e2e": True}),
    ("2. suites disagree (unit passes, integration fails)",
     {"unit": True, "integration": False}),
    ("3. CI outage: NO results arrived",
     {}),
    ("4. code is bad (everything fails)",
     {"unit": False, "integration": False, "e2e": False}),
]

if __name__ == "__main__":
    print(f"{'scenario':<52} {'bool gate':<10} kernel gate")
    print("-" * 110)
    for name, results in SCENARIOS:
        print(f"{name:<52} {gate_bool(results):<10} {gate_lucky(results)}")
    print()
    print("the buried floor in Gate A, exhibited:")
    print(f"  all([]) == {all([])}   "
          "<- Python's vacuous-truth convention: a drawn floor,")
    print("     forgotten so thoroughly it is invisible in the source. "
          "On a CI outage,")
    print("     Gate A DEPLOYS. The fourth corner (neither p nor not-p) "
          "had no place")
    print("     in bool, so the language silently assigned it to p.")
