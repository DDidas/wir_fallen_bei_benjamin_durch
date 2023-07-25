import random

def miller_rabin(n, a):
    # Berechne m und k
    m = n - 1
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1

    # Berechne die Liste der Potenzen
    powers = [pow(a, (2**i)*m, n) for i in range(k+1)]

    # Führe den Miller-Rabin-Test durch
    x = pow(a, m, n)
    if x == 1 or x == n - 1:
        return True, powers
    for _ in range(k - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True, powers
    return False, powers

def run_test():
    n = int(input("Geben Sie n ein: "))
    a = int(input("Geben Sie a ein: "))
    is_prime, powers = miller_rabin(n, a)
    print(f"Die Zahl {n} {'ist wahrscheinlich eine Primzahl' if is_prime else 'ist keine Primzahl'} bei Basis {a}.")
    print(f"Die Liste der Potenzen ist: {powers}")

if __name__ == "__main__":
    run_test()