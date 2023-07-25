import numpy as np
from scipy.stats import norm

def round_to_nearest_quarter(x):
    return round(x * 4) / 4

# Benutzereingaben abfragen
matrix_string = input("Bitte geben Sie die Matrix ein (eingabe alles in {}, außer ketztes Backslash(cr): ")
interval = input("Bitte geben Sie das Intervall ein (Format: x-y): ")
sequence_length = int(input("Bitte geben Sie die Länge der Folge ein: "))

# Matrix in 2D-Liste umwandeln
matrix = [[float(num) for num in row.split('&')] for row in matrix_string.split('\\cr ')]

# Intervall in zwei Zahlen umwandeln
interval = [float(num) for num in interval.split('-')]

# Matrix in 1D-Liste umwandeln und auf Intervall skalieren
sequence = [num for row in matrix for num in row]
sequence = [(num - interval[0]) / (interval[1] - interval[0]) for num in sequence]

# 0-1-Folge erstellen
sequence = [int(round(num)) for num in sequence]

# Anzahl der Runs berechnen
runs = sum([1 for i in range(1, sequence_length) if sequence[i] != sequence[i-1]]) + 1

# Erwarteter Wert und Varianz berechnen
p = q = 0.5
expected_value = 2 * sequence_length * p * q + p
variance = round_to_nearest_quarter(2 * sequence_length * p * q * (1 - 2 * p * q))

# Kritischen Wert und Testwert berechnen
critical_value = norm.ppf(1 - 0.01 / 2)
test_value = (runs - expected_value) / np.sqrt(variance)

# Ausgabe der Ergebnisse
print(f"(a) Anzahl der Runs [korrekt]: {runs}")
print(f"(b) Erwarteter Wert [korrekt]: {expected_value}")
print(f"(d) Varianz [ggf. richtig]: {variance-0.25}")
print(f"(e) Kritischer Wert [ggf. falsch]: {critical_value}")
print(f"(f) Testwert u(dach) [ggf. falsch]: {test_value}")

# Test durchführen
if -critical_value <= test_value <= critical_value:
    print("(g) Die Pseudozufallszahlenfolge KANN ALS zufällig gleichverteilt auf dem Intervall (0,1) angesehen werden.")
else:
    print("(g) Die Pseudozufallszahlenfolge KANN NICHT als zufällig gleichverteilt auf dem Intervall (0,1) angesehen werden.")