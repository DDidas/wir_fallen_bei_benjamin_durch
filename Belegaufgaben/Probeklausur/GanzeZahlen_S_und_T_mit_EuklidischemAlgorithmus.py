def erweiterter_euklidischer_algorithmus(a, b):
    if a == 0:
        return b, 0, 1
    else:
        ggt, x, y = erweiterter_euklidischer_algorithmus(b % a, a)
        return ggt, y - (b // a) * x, x

def main():
    a = int(input("Geben Sie den ersten Wert des ggT ein: "))
    b = int(input("Geben Sie den zweiten Wert des ggT ein: "))
    ggt, s, t = erweiterter_euklidischer_algorithmus(a, b)
    print(f"ggT({a}, {b}) = {ggt} = {s}*{a} + {t}*{b}")

if __name__ == "__main__":
    main()