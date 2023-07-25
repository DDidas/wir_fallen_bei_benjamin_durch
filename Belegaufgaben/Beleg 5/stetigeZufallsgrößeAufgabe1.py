from scipy.integrate import quad
from scipy.optimize import fsolve
import math

def dichtefunktion(x, a):
    if 0 <= x <= 3:
        return x**2 / a + x / 22
    else:
        return 0

def verteilungsfunktion(x, a):
    if x < 0:
        return 0
    elif 0 <= x <= 3:
        return x**3 * 96 / (3 * 6336) + x**2 / (2 * 22)
    else:
        return 1

def wahrscheinlichkeit(a, b):
    result, _ = quad(lambda x: dichtefunktion(x, a), b, 2)
    return result

def erwartungswert(a):
    result, _ = quad(lambda x: x * dichtefunktion(x, a), 0, 3)
    return result

def varianz(a):
    e_x_squared, _ = quad(lambda x: x**2 * dichtefunktion(x, a), 0, 3)
    e_x = erwartungswert(a)
    return e_x_squared - e_x**2

def standardabweichung(a):
    return math.sqrt(varianz(a))

# Berechne Parameter a, damit die Funktion eine Dichtefunktion ist
a = fsolve(lambda a: quad(lambda x: dichtefunktion(x, a), 0, 3)[0] - 1, 22)[0]

# Wahrscheinlichkeit P(0.5 <= X <= 2)
wahrscheinlichkeit_ergebnis = wahrscheinlichkeit(a, 0.5)

# Erwartungswert
erwartungswert_ergebnis = erwartungswert(a)

# Varianz
varianz_ergebnis = varianz(a)

# Standardabweichung
standardabweichung_ergebnis = standardabweichung(a)

# Ergebnisse ausgeben
print("Parameter a: {:.5f}".format(a))
print("Wahrscheinlichkeit P(0.5 <= X <= 2) = {:.5f} %".format(wahrscheinlichkeit_ergebnis * 100))
print("Erwartungswert: {:.5f}".format(erwartungswert_ergebnis))
print("Varianz: {:.5f}".format(varianz_ergebnis))
print("Standardabweichung: {:.5f}".format(standardabweichung_ergebnis))
