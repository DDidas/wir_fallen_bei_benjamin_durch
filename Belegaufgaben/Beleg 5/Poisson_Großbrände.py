from math import exp, factorial

def calculate_poisson_probabilities():
    # Benutzereingabe
    lambda_ = float(input("Geben Sie den Erwartungswert ein (durchschnittliche Anzahl von Großbränden pro Jahr): "))
    x = int(input("Geben Sie den Wert für 'P(X<=x)' ein: "))
    z = int(input("Geben Sie den Wert für 'P(X>z)' ein: "))
    operator_x = input("Geben Sie den Operator für P(X op x) ein (>=, =, <=, >, <): ")
    operator_z = input("Geben Sie den Operator für P(X op z) ein (>=, =, <=, >, <): ")

    # Berechnung der Wahrscheinlichkeiten
    P_less_than_or_equal_to_x = sum((lambda_**k * exp(-lambda_)) / factorial(k) for k in range(x+1))
    P_greater_than_z = 1 - sum((lambda_**k * exp(-lambda_)) / factorial(k) for k in range(z+1))

    # Anpassung der Wahrscheinlichkeiten basierend auf den Operatoren
    if operator_x in ['>=', '>']:
        P_less_than_or_equal_to_x = 1 - P_less_than_or_equal_to_x
    if operator_z in ['<=', '<']:
        P_greater_than_z = 1 - P_greater_than_z

    print("P(X", operator_x, x, ") = ", P_less_than_or_equal_to_x)
    print("P(X", operator_z, z, ") = ", P_greater_than_z)

# Aufruf der Funktion
calculate_poisson_probabilities()