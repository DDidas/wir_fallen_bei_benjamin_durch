from math import comb

def calculate_binomial_probabilities_and_expectation():
    # Benutzereingabe
    n = int(input("Geben Sie die Anzahl der Versuche ein: "))
    p = eval(input("Geben Sie die Trefferwahrscheinlichkeit ein (als Bruchzahl): "))
    y1 = int(input("Geben Sie den Wert für 'P(X<y)' ein: "))
    y2 = int(input("Geben Sie den Wert für 'P(X>y)' ein: "))

    # Berechnung der Wahrscheinlichkeiten
    P_less_than_y1 = sum(comb(n, k) * p**k * (1-p)**(n-k) for k in range(y1))
    P_more_than_y2 = sum(comb(n, k) * p**k * (1-p)**(n-k) for k in range(y2+1, n+1))

    # Berechnung des Erwartungswerts
    mu = n * p

    print("P(X<", y1, ") = ", P_less_than_y1 * 100)
    print("P(X>", y2, ") = ", P_more_than_y2 * 100)
    print("mu = ", mu)

# Aufruf der Funktion
calculate_binomial_probabilities_and_expectation()