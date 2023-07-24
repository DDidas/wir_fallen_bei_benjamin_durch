import ggT
from decoding import *
import decoding


def phi(n, primfaktorzerl):
    for p in primfaktorzerl:
        n *= (1 - 1 / p)
    return n


def phiprime(P, Q):
    return (P - 1) * (Q - 1)


def exp_mod(base, exponent, mod):  # for big numbers , but basicly the same as (base ** exponent) % mod
    import gdi.numberConverter as gdi
    out = 1
    bin = gdi.dez2bin(exponent)
    print(exponent, "=")
    for i in range(len(bin)):
        if bin[-1 - i]:
            print(f"2^{i}+", end="")
        e = (2 ** i) * bin[-1 - i]
        out *= base ** e % mod
        out %= mod
    print()
    return out


def generate_keys(p=47, q=61):
    PHI = phiprime(p, q)
    N = p * q
    e = 13
    # wähle e < phi(p, q) wobei e Teiler fremd zu N
    while True:
        if ggT.ggT(e, PHI) == 1:
            break
        e += 1  # +2 eigentlich wenn p,q != 2

    _, (__, d) = ggT.erweiterter_euklid(PHI, e)

    d = d % PHI
    print("p", p, "    q", q, "  N", N, "   phi", PHI, "    e", e, "   d", d)
    return e, d, N


def decodeString(_e, _N, wort, split=2):
    nums = str2nums(wort, split)
    test = nums2str(nums)
    print(nums, test, wort)
    return decode(_e, _N, nums)


def decode(_e, _N, m):
    # 3*11067 %33200
    chiffrats = [exp_mod(num, _e, _N) for num in m]
    print(chiffrats, "[num**e % N for num in nums]")
    return chiffrats


if __name__ == '__main__':
    _split = 2
    MESSAGE = "MEIN WORT "
    e, d, N = generate_keys(p=47, q=61)
    if N < 27*10**_split:
        raise Exception("N to small\n mach den _split kleiner")
    if len(MESSAGE) % _split != 0:
        raise Exception("Message is bad, \nfolgendes muss gelten: länge des worts mod _split = 0, verlängere das Wort oder änder _split")
    chiffrates = decodeString(e, N, MESSAGE, _split) # folgendes muss gelten: länge des worts mod _split = 0
    plaintextNumbers = decode(d, N, chiffrates)
    m = nums2str(plaintextNumbers)
    print(m)