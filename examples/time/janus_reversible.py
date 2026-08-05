"""
A micro-Janus: reversible computation, where forgetting is forbidden.
Run: python3 janus_reversible.py

Janus's rules, embodied:
 - only invertible statements exist (x += e, x -= e, x ^= e, swap)
 - plain assignment x = e is BANNED: it would destroy x's past
 - every `if` needs a JOIN CONDITION: a post-hoc test revealing
   which branch ran, or the program cannot be reversed.
Every decision must leave a trace sufficient to un-decide it.
"""

class Reversible:
    """Programs are lists of invertible steps; run them either direction."""
    def __init__(self): self.steps = []
    def add(self, var, expr):      self.steps.append(("add", var, expr))
    def sub(self, var, expr):      self.steps.append(("sub", var, expr))
    def swap(self, a, b):          self.steps.append(("swap", a, b))
    # def assign(self, var, expr): raise TypeError("FORBIDDEN: destroys information")

    def run(self, state, backward=False):
        state = dict(state)
        steps = reversed(self.steps) if backward else self.steps
        inv = {"add": "sub", "sub": "add", "swap": "swap"}
        for op, a, b in steps:
            if backward: op = inv[op]
            if   op == "add":  state[a] += b(state) if callable(b) else b
            elif op == "sub":  state[a] -= b(state) if callable(b) else b
            elif op == "swap": state[a], state[b] = state[b], state[a]
        return state

if __name__ == "__main__":
    # Fibonacci, reversibly (the classic Janus demo):
    fib = Reversible()
    for _ in range(10):                    # 10 reversible iterations
        fib.add("a", lambda s: s["b"])     # a += b
        fib.swap("a", "b")

    start = {"a": 0, "b": 1}
    end = fib.run(start)
    back = fib.run(end, backward=True)
    print(f"forward : {start} -> {end}")
    print(f"backward: {end} -> {back}")
    assert back == start, "time reversal failed!"
    print("\nThe past was reconstructed mechanically. Nothing was ever forgotten.")
    print("Now note what we COULDN'T write: `a = 0` (reset) is inexpressible --")
    print("erasure is the one operation this universe lacks. (Landauer smiles.)")
