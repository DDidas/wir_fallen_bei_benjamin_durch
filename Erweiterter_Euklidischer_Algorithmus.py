def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)

    gcd, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return (gcd, x, y)

def main():
    a = 132
    b = 12

    gcd, x, y = extended_gcd(a, b)

    print("The GCD is", gcd)
    print("x =", x, ", y =", y)

if __name__ == "__main__":
    main()