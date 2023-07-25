def calculate_probabilities_and_expectation():
    # Benutzereingabe
    x = eval(input("Geben Sie die Werte ein (in Form eines Tupels) -> Zahlen durch ein Komma getrennt: "))
    p = list(eval(input("Geben Sie die Wahrscheinlichkeiten ein (in Form eines Tupels): -> Gesuchte Wahrscheinlichkeit = None ")))

    # Finden des Indexes von None (unbekannte Wahrscheinlichkeit)
    none_index = p.index(None)

    # Berechnung der unbekannten Wahrscheinlichkeit
    p[none_index] = 1 - sum([val for val in p if val is not None])

    # Berechnung des Erwartungswerts
    mu = sum(x[i] * p[i] for i in range(len(x)))

    print("Die unbekannte Wahrscheinlichkeit ist: ", p[none_index])
    print("Der Erwartungswert liegt bei mu = ", mu)

# Aufruf der Funktion
calculate_probabilities_and_expectation()