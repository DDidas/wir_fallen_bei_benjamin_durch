def f(x, c):
    if -1/2 <= x <= 3/2:
        return c * (-x**2 + x + 34)
    else:
        return 0

def calculate_c():
    from scipy.integrate import quad
    from functools import partial

    # Definieren der Funktion, die integriert werden soll
    integrand = partial(f, c=1)  # Parameter c vorübergehend als 1 setzen

    # Integriere die Funktion von -1/2 bis 3/2 und setze das Ergebnis gleich 1 (Bedingung für Wahrscheinlichkeitsdichte)
    c, _ = quad(integrand, -1/2, 3/2, points=[-1/2, 3/2], weight='sin')
    return 1 / c

def probability_X_equals_1(c):
    return f(1, c)

def probability_X_greater_than_minus_326(c):
    from scipy.integrate import quad
    from functools import partial

    # Definieren der Funktion, die integriert werden soll
    integrand = partial(f, c=c)

    # Integriere die Funktion von -∞ bis -326, um die Wahrscheinlichkeit P(X >= -326) zu berechnen
    probability, _ = quad(integrand, float('-inf'), -326)
    return probability

def expected_value(c):
    from scipy.integrate import quad
    from functools import partial

    # Definieren der Funktion, die integriert werden soll
    integrand = partial(lambda x, c: x * f(x, c), c=c)

    # Integriere die Funktion von -∞ bis ∞, um den Erwartungswert zu berechnen
    expectation, _ = quad(integrand, float('-inf'), float('inf'))
    return expectation

if __name__ == "__main__":
    c = calculate_c()

    probability_X_equals_1_result = probability_X_equals_1(c)
    probability_X_greater_than_minus_326_result = probability_X_greater_than_minus_326(c)
    expected_value_result = expected_value(c)

    print("𝑃(𝑋=1) =", probability_X_equals_1_result)
    print("𝑃(𝑋≥−326) =", probability_X_greater_than_minus_326_result)
    print("𝜇𝑋 =", expected_value_result)
