from math import comb

def calculate_probabilities_and_expectation():
    # Gegebene Werte

    #Anzahl der Kreuzungen, an denen gewürfelt wird
    n = 7

    #Wert für Würfelentscheidungskriterium
    p = 4/20

    # Berechnung der Wahrscheinlichkeiten
    P_BBQ = comb(n, 2) * p**2 * (1-p)**(n-2)
    P_33rd = comb(n, 0) * p**0 * (1-p)**n

    # Berechnung des Erwartungswerts
    mu = n * p

    print("Die Wahrscheinlichkeit, dass wir bei Brother Jimmy's BBQ landen, liegt bei ", P_BBQ * 100)
    print("Die Wahrscheinlichkeit, dass wir in der 33. Straße herauskommen, liegt bei ", P_33rd * 100)
    print("Im Mittel laufen wir unter diesen Umständen ", mu, "mal nach rechts.")

# Aufruf der Funktion
calculate_probabilities_and_expectation()