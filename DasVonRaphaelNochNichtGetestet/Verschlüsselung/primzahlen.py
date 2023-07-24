import math


class Zerlegung:

    def __init__(self, zerleger, potenz, rest):
        self.rest = rest
        self.zerleger = zerleger
        self.potenz = potenz


def zerlegung_mit(zahl, zerlgr):
    potenz = 0
    while True:
        if zahl % zerlgr != 0:
            break
        potenz += 1
        zahl /= zerlgr

    return Zerlegung(zerlgr, potenz, zahl)


def generate_primzahlen(bis=100):
    all = [i for i in range(2, bis + 1)]
    locked = 0
    while locked + 1 < len(all):
        mabyprim = all[locked + 1]

    pass


def proof_prim(prim):
    goal = int(math.sqrt(prim))


"""Fermat Test Primzahltest"""


def fermatPrim(n, a):
    """
    n ist primzahl kandidat
    Wähle a teilerfremd zu n zufällig

    - Gilt p = ggt(a,n) > 1, dann ist p Teiler von n und n damit nicht prim.

    - überprüfe ob a^(n-1) === 1 mod n
       ja: Primzahlkanditat
       nein: n ist zusammen gesetzt
    :return:
    """
    print("primzahl", n, "a", a)
    import ggT
    if ggT.ggT(n, a) == 1:
        print(n, a, "Teilerfremd!")
        o = a ** (n - 1) % n
        print("a^(n-1) mod n === ", o)
        return o == 1
    return False


"""Miller Rabin Primzahltest"""


def millerrabintest(n, a):
    """
    - wähle a aus der menge der zu n teilerfremden zwischen [2,n-1]
    - zerlege n-1 = m*2^k mit k maximal (d.h. m ungerade)

    - betrachte Folge:
        (a^m,a^m*2,a^m*2^2,a^m*2^3,...a^m*2^k) mod n // mod n ist komponenten weise

        hinweis: a^m*2^k == a^(n-1)
    Basierend auf satz von vermat

    erfolgskriterium [...,n-1,1,...,1] die liste muss dieser form sein
    :param prim:
    :return:
    """
    print(f"millerrabintest({n},{a})")
    m = n - 1
    k = 0
    while True:
        b = m % 2
        if b == 1: break
        k += 1
        m //= 2

    print("n-1 = m*2^k", "n-1 =", n - 1, "m =", m, "k =", k)

    A = []
    for i in range(k + 1):
        A.append(a ** (m * 2 ** i) % n)
    print("A:", A)
    A.reverse()
    if A[0] != 1: return False
    for a in A:
        if a != 1:
            return a == n - 1


n = 18721
print("Kandidat", millerrabintest(n, 2))

print("Kandidat", millerrabintest(n, 3))
print("Kandidat", millerrabintest(n, 5))
