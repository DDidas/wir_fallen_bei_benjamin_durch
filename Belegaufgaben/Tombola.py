def calculate_expectation_and_decide():
    # Benutzereingabe
    x_values = eval(input("Geben Sie die Gewinne ein (in Form eines Tupels): "))
    p_values = eval(input("Geben Sie die Wahrscheinlichkeiten ein (in Form eines Tupels): "))
    ticket_price = float(input("Geben Sie den Preis des Loses ein: "))
    x = float(input("Geben Sie den Wert für F(x) ein: "))
    y = float(input("Geben Sie den Wert für F(y) ein: "))

    # Berechnung des Erwartungswerts
    mu = sum(x_values[i] * p_values[i] for i in range(len(x_values)))

    # Berechnung der Varianz
    variance = sum((x_values[i] - mu) ** 2 * p_values[i] for i in range(len(x_values)))

    # Berechnung der Standardabweichung
    sigma = variance ** 0.5

    # Berechnung der Verteilungsfunktionen F(x) und F(y)
    F_x = sum(p_values[i] for i in range(len(x_values)) if x_values[i] <= x)
    F_y = sum(p_values[i] for i in range(len(x_values)) if x_values[i] <= y)

    # Entscheidung, ob sich der Kauf des Loses lohnt
    is_worth_it = "Ja" if mu > ticket_price else "Nein"

    print("Erwartungswert mü: ", mu)
    print("Varianz sigma^2: ", variance)
    print("Standardabweichung sigma: ", sigma)
    print("F(", x, ") = ", F_x)
    print("F(", y, ") = ", F_y)
    print("Lohnt sich der Kauf eines Loses zum Preis von ", ticket_price, " €? ", is_worth_it)

# Aufruf der Funktion
calculate_expectation_and_decide()