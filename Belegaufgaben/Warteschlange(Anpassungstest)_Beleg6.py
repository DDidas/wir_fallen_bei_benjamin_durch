import numpy as np
import scipy.stats as stats
import re

# Eingabe der Daten
n = int(input("Bitte geben Sie die Gesamtzahl der Beobachtungen ein: "))
mean_delta_t = float(input("Bitte geben Sie den Mittelwert ein: "))

# Eingabe der beobachteten Häufigkeiten
observed_freqs = np.array([int(i) for i in input("Bitte geben Sie die beobachteten Häufigkeiten ein, getrennt durch '&': ").split('&')])

# Eingabe der oberen Intervallgrenzen
upper_bounds_input = input("Bitte geben Sie die oberen Intervallgrenzen ein, getrennt durch '&', endend mit 'inf': ")

# Extrahieren der Zahlen aus der Eingabe
upper_bounds = [float(i) if i != 'inf' else np.inf for i in re.findall(r'[\d\.inf]+', upper_bounds_input)]

# Erzeugung der Intervallgrenzen
intervals = [0] + upper_bounds

# Berechnung der theoretischen Wahrscheinlichkeiten für jedes Intervall
lambda_hat = 1 / mean_delta_t
theoretical_probs = [stats.expon.cdf(intervals[i+1], scale=1/lambda_hat) - stats.expon.cdf(intervals[i], scale=1/lambda_hat) for i in range(len(intervals)-1)]

# Berechnung der erwarteten Häufigkeiten
expected_freqs = n * np.array(theoretical_probs)

# Berechnung der Teststatistik
sq_diffs = (observed_freqs - expected_freqs)**2 / expected_freqs
test_statistic = np.sum(sq_diffs)

# Vergleich der Teststatistik mit der kritischen Grenze
critical_value = stats.chi2.ppf(0.99, df=len(observed_freqs)-2)

print(f"\nSchätzwert \hat\lambda = {lambda_hat}\n")
print(f"Testwert = {test_statistic}\n")
print(f"Kritische Grenze = {critical_value}\n")

if test_statistic <= critical_value:
    print("Wir können davon ausgehen, dass die vorliegenden Ankunftsabstände exponentialverteilt sind.")
else:
    print("Wir können nicht davon ausgehen, dass die vorliegenden Ankunftsabstände exponentialverteilt sind.")
