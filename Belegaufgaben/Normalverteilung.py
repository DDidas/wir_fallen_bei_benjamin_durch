from scipy.stats import norm

def calculate_normal_probabilities_and_quantile():
    # Benutzereingabe
    mu = float(input("Geben Sie den Mittelwert ein: "))
    sigma = float(input("Geben Sie die Standardabweichung ein: "))
    p = float(input("Geben Sie den Wert für p ein (für die Berechnung von k): "))

    while True:
        # Abfrage, ob ein einseitiger Test oder ein Bereich verwendet werden soll
        test_type = input("Möchten Sie einen einseitigen Test oder einen Bereich angeben? (E/B): ")
        if test_type.lower() == 'e':
            operator = input("Geben Sie den Operator für P(X op x) ein (<, >, >=, =, <=): ")
            x = float(input("Geben Sie den Wert für x ein: "))

            # Berechnung der Wahrscheinlichkeit
            if operator == '<':
                P = norm.cdf(x, mu, sigma)
            elif operator == '>':
                P = 1 - norm.cdf(x, mu, sigma)
            elif operator == '<=':
                P = norm.cdf(x, mu, sigma)
            elif operator == '>=':
                P = 1 - norm.cdf(x, mu, sigma)
            elif operator == '=':
                P = norm.pdf(x, mu, sigma)

            print("P(X", operator, x, ") = ", P*100)

        elif test_type.lower() == 'b':
            x1 = float(input("Geben Sie den unteren Wert für x ein: "))
            x2 = float(input("Geben Sie den oberen Wert für x ein: "))

            # Berechnung der Wahrscheinlichkeit
            P = norm.cdf(x2, mu, sigma) - norm.cdf(x1, mu, sigma)

            print("P(", x1, "<= X <= ", x2, ") = ", P*100)

        # Abfrage, ob der Benutzer fortfahren möchte
        continue_ = input("Möchten Sie eine weitere Berechnung durchführen? (J/N): ")
        if continue_.lower() != 'j':
            break

    # Berechnung von k
    k = norm.ppf((1 + p) / 2, mu, sigma) - mu
    print("Für k = ", k, "gilt P(mu - k <= X <= mu + k) = ", p)

# Aufruf der Funktion
calculate_normal_probabilities_and_quantile()