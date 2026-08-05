"""
A metacircular evaluator in ~60 lines: the legal form of self-reference.
Run: python3 lisp_metacircular.py

Tarski: a language cannot contain its own TRUTH predicate.
Nothing stops it containing its own INTERPRETER.
That gap -- interpretation legal, truth illegal -- is one of the
deepest facts about formal systems. Here is the legal side.
"""

def tokenize(s): return s.replace("(", " ( ").replace(")", " ) ").split()

def parse(tokens):
    t = tokens.pop(0)
    if t == "(":
        out = []
        while tokens[0] != ")": out.append(parse(tokens))
        tokens.pop(0)
        return out
    try: return int(t)
    except ValueError: return t

def read(s): return parse(tokenize(s))

def evaluate(x, env):
    if isinstance(x, str):  return env[x]
    if isinstance(x, int):  return x
    op, *args = x
    if op == "quote":  return args[0]              # code refuses to run: it is DATA
    if op == "if":     return evaluate(args[1] if evaluate(args[0], env) else args[2], env)
    if op == "lambda":
        params, body = args
        return lambda *vals: evaluate(body, {**env, **dict(zip(params, vals))})
    if op == "define":
        env[args[0]] = evaluate(args[1], env); return None
    f = evaluate(op, env)
    return f(*(evaluate(a, env) for a in args))

GLOBAL = {"+": lambda a,b: a+b, "-": lambda a,b: a-b, "*": lambda a,b: a*b,
          "=": lambda a,b: 1 if a==b else 0, "<": lambda a,b: 1 if a<b else 0}

if __name__ == "__main__":
    prog = """(define fact (lambda (n) (if (= n 0) 1 (* n (fact (- n 1))))))"""
    evaluate(read(prog), GLOBAL)
    print("fact 10 =", evaluate(read("(fact 10)"), GLOBAL))

    # code as data: the SAME s-expression, quoted vs evaluated
    print("quoted:   ", evaluate(read("(quote (fact 10))"), GLOBAL))
    print("evaluated:", evaluate(read("(fact 10)"), GLOBAL))

    # The strange loop: this evaluator, written in Python, could be
    # rewritten in its own Lisp; that Lisp-in-Lisp runs on this one.
    # Turtles all the way down -- until Gödel: the tower can interpret
    # itself but can never PROVE ITSELF consistent from inside.
    print("\ncode = data = code. The loop closes; the blind spot remains.")
