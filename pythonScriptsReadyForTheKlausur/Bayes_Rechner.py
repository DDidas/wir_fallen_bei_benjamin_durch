def bayes_theorem():
    # Benutzereingabe
    P_B = float(input("Geben Sie die Wahrscheinlichkeit für A ein (in Dezimalform): "))
    P_E = float(input("Geben Sie die Wahrscheinlichkeit für B ein (in Dezimalform): "))
    P_K_B = float(input("Geben Sie die Wahrscheinlichkeit für C in Relation zu A ein (in Dezimalform): "))
    P_K_E = float(input("Geben Sie die Wahrscheinlichkeit für C in Relation zu B ein (in Dezimalform): "))
    P_K_G = float(input("Geben Sie die Wahrscheinlichkeit für C in Relation zu D ein (in Dezimalform): "))

    # Die verbleibende Wahrscheinlichkeit P(G) muss addiert zu den anderen beiden 1 ergeben
    P_G = 1 - P_B - P_E

    # Berechnung der Wahrscheinlichkeiten nach dem Satz von Bayes
    P_B_K = (P_B * P_K_B) / ((P_B * P_K_B) + (P_E * P_K_E) + (P_G * P_K_G))
    P_E_K = (P_E * P_K_E) / ((P_B * P_K_B) + (P_E * P_K_E) + (P_G * P_K_G))
    P_G_K = (P_G * P_K_G) / ((P_B * P_K_B) + (P_E * P_K_E) + (P_G * P_K_G))

    print("Die Wahrscheinlichkeit, dass Holger Borreliose hat, gegeben, dass er Kopfschmerzen hat, ist: ", P_B_K)
    print("Die Wahrscheinlichkeit, dass Holger eine Erkältung hat, gegeben, dass er Kopfschmerzen hat, ist: ", P_E_K)
    print("Die Wahrscheinlichkeit, dass Holger zu wenig getrunken hat, gegeben, dass er Kopfschmerzen hat, ist: ", P_G_K)

# Aufruf der Funktion
bayes_theorem()

#ACHTUNG DER RECHNER IST NICHT ALLGEMEINGÜLTIG