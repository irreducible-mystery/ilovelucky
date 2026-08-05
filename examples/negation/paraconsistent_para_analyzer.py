"""
Paraconsistent Annotated Evidential Logic Eτ: the para-analyzer.
Run: python3 paraconsistent_para_analyzer.py

Each proposition is annotated (mu, lam): favorable and contrary evidence,
varying INDEPENDENTLY. From these, two orthogonal readings:
  certainty      Gc  = mu - lam    (net verdict)
  contradiction  Gct = mu + lam - 1 (evidential health)
Used in real robot control (Emmy series, São Paulo school): high |Gct|
triggers behavior distinct from both 'true' and 'false' -- the conflict
itself is routed on. Booleans, fuzzy logic and probability all collapse
'nobody knows' and 'everybody disagrees'. This logic keeps them apart.
"""

def analyze(mu, lam, t=0.6):
    gc, gct = mu - lam, mu + lam - 1
    if   gc  >=  t: region = "TRUE            -> act on it"
    elif gc  <= -t: region = "FALSE           -> act on its negation"
    elif gct >=  t: region = "INCONSISTENT    -> audit your sources"
    elif gct <= -t: region = "PARACOMPLETE    -> gather more data"
    else:           region = "boundary        -> lean " + (
                     "true" if gc > 0 else "false" if gc < 0 else "nowhere")
    return gc, gct, region

if __name__ == "__main__":
    cases = [
        ("clear path (both sensors agree)",        0.9, 0.1),
        ("obstacle (both sensors agree)",          0.1, 0.9),
        ("SENSORS DISAGREE VIOLENTLY",             0.9, 0.9),
        ("no sensor data yet",                     0.1, 0.1),
        ("weak lean, thin evidence",               0.6, 0.4),
    ]
    print(f"{'situation':38s} {'mu':>4s} {'lam':>4s} {'Gc':>6s} {'Gct':>6s}  verdict")
    for name, mu, lam in cases:
        gc, gct, region = analyze(mu, lam)
        print(f"{name:38s} {mu:4.1f} {lam:4.1f} {gc:6.2f} {gct:6.2f}  {region}")
    print()
    print("Rows 3 and 4 both have Gc = 0 -- 'no net verdict' -- but for")
    print("OPPOSITE reasons, demanding OPPOSITE responses. That distinction")
    print("is what every boolean, and every plain probability, throws away.")
