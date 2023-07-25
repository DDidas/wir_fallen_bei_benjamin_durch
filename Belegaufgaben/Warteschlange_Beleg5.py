from scipy.stats import expon

def calculate_exponential_probabilities():
    # Benutzereingabe
    mu = float(input("Geben Sie die durchschnittliche Wartezeit in Minuten ein: "))
    y = float(input("Geben Sie den Wert für y ein (mindestens y Minuten warten): "))
    z = float(input("Geben Sie den Wert für z ein (höchstens z Minuten warten): "))

    # Berechnung der Wahrscheinlichkeiten
    P_at_least_y = expon.sf(y, scale=mu)
    P_at_most_z = expon.cdf(z, scale=mu)

    print("Die Wahrscheinlichkeit, mindestens ", y, " Minuten zu warten, beträgt ", P_at_least_y)
    print("Die Wahrscheinlichkeit, höchstens ", z, " Minuten zu warten, beträgt ", P_at_most_z)

# Aufruf der Funktion
calculate_exponential_probabilities()