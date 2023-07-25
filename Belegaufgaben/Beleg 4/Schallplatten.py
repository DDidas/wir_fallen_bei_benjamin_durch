def calculate_probabilities():
    # Benutzereingabe
    P1 = int(input("Geben Sie die Anzahl der auf P1 produzierten Platten ein: "))
    P2 = int(input("Geben Sie die Anzahl der auf P2 produzierten Platten ein: "))
    P3 = int(input("Geben Sie die Anzahl der auf P3 produzierten Platten ein: "))
    P4 = int(input("Geben Sie die Anzahl der auf P4 produzierten Platten ein: "))
    R1 = float(input("Geben Sie die Ausschussrate von P1 ein (in Dezimalform): "))
    R2 = float(input("Geben Sie die Ausschussrate von P2 ein (in Dezimalform): "))
    R3 = float(input("Geben Sie die Ausschussrate von P3 ein (in Dezimalform): "))
    R4 = float(input("Geben Sie die Ausschussrate von P4 ein (in Dezimalform): "))

    # Berechnung der Anzahl der Ausschussplatten von jeder Presse
    A1 = P1 * R1
    A2 = P2 * R2
    A3 = P3 * R3
    A4 = P4 * R4

    # Berechnung der Gesamtzahl der Ausschussplatten
    A_total = A1 + A2 + A3 + A4

    # Berechnung der Wahrscheinlichkeiten
    P_A1 = A1 / A_total
    P_A2 = A2 / A_total
    P_A3 = A3 / A_total
    P_A4 = A4 / A_total

    print("Die Wahrscheinlichkeit, dass eine Ausschussplatte von P1 stammt, liegt bei: ", P_A1)
    print("Die Wahrscheinlichkeit, dass eine Ausschussplatte von P2 stammt, liegt bei: ", P_A2)
    print("Die Wahrscheinlichkeit, dass eine Ausschussplatte von P3 stammt, liegt bei: ", P_A3)
    print("Die Wahrscheinlichkeit, dass eine Ausschussplatte von P4 stammt, liegt bei: ", P_A4)

    # Berechnung der Gesamtzahl der Ausschussplatten
    A_total = ( A1 + A2 + A3 + A4 )

    print("Die Gesamtzahl der Ausschussplatten an diesem Tag betrug: ", A_total)

# Aufruf der Funktion
calculate_probabilities()
