def erweiterter_euklidischer_algorithmus(a, b):
    if a == 0:
        return b, 0, 1
    else:
        ggt, x, y = erweiterter_euklidischer_algorithmus(b % a, a)
        return ggt, y - (b // a) * x, x

def multiplikatives_inverse(a, m):
    ggt, x, _ = erweiterter_euklidischer_algorithmus(a, m)
    if ggt != 1:
        raise Exception(f"{a} hat kein multiplikatives Inverses modulo {m}")
    else:
        return x % m

def main():
    a = int(input("Geben Sie den Wert für a ein (Multiplaktiv Inverses von _ ) 3: "))
    m = int(input("Geben Sie das Modul ein (!! Z !!): "))
    inverse = multiplikatives_inverse(a, m)
    print(f"Das multiplikative Inverse von {a} mod {m} ist {inverse}")

if __name__ == "__main__":
    main()