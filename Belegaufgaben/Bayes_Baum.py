def calculate_probabilities():
    # Benutzereingabe
    P_B = float(input("Geben Sie die Wahrscheinlichkeit für Borreliose ein (in Dezimalform): "))
    P_E = float(input("Geben Sie die Wahrscheinlichkeit für eine Erkältung ein (in Dezimalform): "))
    P_K_B = float(input("Geben Sie die Wahrscheinlichkeit für Kopfschmerzen gegeben Borreliose ein (in Dezimalform): "))

    # Berechnung der Wahrscheinlichkeiten
    P_not_K_B = 1 - P_K_B
    P_G = 1 - P_B - P_E

    print("Die Wahrscheinlichkeit der Kante von B zu nicht K ist: ", P_not_K_B)
    print("Die Wahrscheinlichkeit der Kante vom Startknoten zu G ist: ", P_G)

# Aufruf der Funktion
calculate_probabilities()