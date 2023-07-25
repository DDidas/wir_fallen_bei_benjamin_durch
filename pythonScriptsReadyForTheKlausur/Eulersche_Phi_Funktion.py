def gcd(p, q):
    # Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p % q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1, x) if is_coprime(x, y)]
        return len(n)

while True:
    # Eingabe für Eulersche Phi Funktion
    x = int(input("Bitte geben Sie eine Zahl für die Eulersche Phi-Funktion ein: "))
    print(phi_func(x))

    fortsetzen = input('Möchten Sie fortfahren? (y/n): ')
    if fortsetzen.lower() != 'y':
        break
