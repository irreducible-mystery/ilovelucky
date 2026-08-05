"""
Belnap's four-valued logic FDE: "How a computer should think" (1977).
Run: python3 belnap_four_valued.py

Truth as the state of an evidence ledger fed by unreliable sources:
  T = told true only        F = told false only
  B = told BOTH             N = told nothing
Contradiction (B) is quarantined, not explosive: deriving B for p
does not infect q. Compare: one contradiction in classical logic
proves everything (ex contradictione quodlibet).
"""

T, F, B, N = "True", "False", "Both", "Neither"

# Belnap's logical lattice (truth ordering): F <= B,N <= T
AND = {  # meet in the truth ordering
    (T,T):T,(T,B):B,(T,N):N,(T,F):F,
    (B,T):B,(B,B):B,(B,N):F,(B,F):F,
    (N,T):N,(N,B):F,(N,N):N,(N,F):F,
    (F,T):F,(F,B):F,(F,N):F,(F,F):F,
}
OR  = {k:{T:F,F:T,B:N,N:B}[v] for k,v in
       {(a,b):AND[({T:F,F:T,B:N,N:B}[a],{T:F,F:T,B:N,N:B}[b])]
        for a in (T,F,B,N) for b in (T,F,B,N)}.items()}  # de Morgan dual
NOT = {T:F, F:T, B:B, N:N}   # negation swaps T/F, FIXES Both and Neither:
                             # contradictory evidence, negated, is still contradictory.

class Ledger:
    """Each proposition accumulates testimony independently."""
    def __init__(self): self.told = {}
    def tell(self, prop, polarity, source):
        s = self.told.setdefault(prop, set())
        s.add(polarity)
        print(f"  [{source}] says {prop} is {polarity}")
    def value(self, prop):
        s = self.told.get(prop, set())
        return {frozenset(): N, frozenset({'true'}): T,
                frozenset({'false'}): F,
                frozenset({'true','false'}): B}[frozenset(s)]

if __name__ == "__main__":
    db = Ledger()
    print("Testimony arrives:")
    db.tell("server_up",   "true",  "monitor-1")
    db.tell("server_up",   "false", "monitor-2")   # conflict!
    db.tell("disk_full",   "false", "monitor-1")
    # nobody says anything about 'backup_ok'

    print("\nLedger states:")
    for p in ("server_up", "disk_full", "backup_ok"):
        print(f"  {p:11s} = {db.value(p)}")

    su, df = db.value("server_up"), db.value("disk_full")
    print(f"\nserver_up AND disk_full = {AND[(su,df)]}")
    print(f"NOT server_up           = {NOT[su]}   <- contradiction survives negation")
    print(f"backup_ok               = {db.value('backup_ok')}  <- ignorance is not falsity")
    print("\nNote what NEVER happened: no explosion. The server_up conflict")
    print("tells us to audit monitors; it does not license believing anything.")
