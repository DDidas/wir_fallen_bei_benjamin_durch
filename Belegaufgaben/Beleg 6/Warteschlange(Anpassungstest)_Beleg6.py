import numpy as np
import scipy.stats as stats
import pandas as pd

# Diese Anweisung weist Pandas an, alle Spalten anzuzeigen
pd.set_option('display.max_columns', None)

# Eingabe der Daten
n = int(input("Bitte geben Sie die Gesamtzahl der Beobachtungen ein: "))
mean_delta_t = float(input("Bitte geben Sie den Mittelwert ein: "))

# Eingabe der beobachteten Häufigkeiten
observed_freqs = np.array([int(i) for i in input("Bitte geben Sie die beobachteten Häufigkeiten ein, getrennt durch '&': ").split('&')])

# Eingabe der oberen Intervallgrenzen
intervals = [int(i) if i != 'inf' else np.inf for i in input("Bitte geben Sie die oberen Intervallgrenzen ein, getrennt durch '&', endend mit 'inf': ").split('&')]

# Berechnung der theoretischen Wahrscheinlichkeiten und Häufigkeiten
lambda_hat = 1 / mean_delta_t  # Schätzwert für Lambda
lower_bounds = [0] + intervals[:-1]
pi_theo = np.array([np.exp(-lambda_hat * lower_bounds[i]) - np.exp(-lambda_hat * intervals[i]) for i in range(len(intervals))])
ni_star_theo = n * pi_theo

# Erstellung der Tabelle
df = pd.DataFrame()
df['Klasse'] = [f"[{lower_bounds[i]},{intervals[i]})" for i in range(len(intervals))]
df['n_i (Stichprobe)'] = observed_freqs
df['p_i (theoretisch)'] = pi_theo
df['n_i* (theoretisch)'] = ni_star_theo
df['(n_i - n_i*)^2 / n_i*'] = np.power(observed_freqs - ni_star_theo, 2) / ni_star_theo

# Hinzufügen der Summenzeile
sum_row = pd.DataFrame(df.sum(numeric_only=True)).transpose()
sum_row["Klasse"] = "Σ"
df = pd.concat([df, sum_row], ignore_index=True)

print(df)

# Berechnung des Testwerts
test_value = np.sum(np.power(observed_freqs - ni_star_theo, 2) / ni_star_theo)

# Berechnung der Freiheitsgrade und der kritischen Grenze
df_ = len(observed_freqs) - 2  # Freiheitsgrade (Anzahl der Intervalle - 1 - Anzahl der geschätzten Parameter)
critical_value = stats.chi2.ppf(0.95, df_)  # Kritischer Wert bei einem Signifikanzniveau von 5%

# Ausgabe der Ergebnisse
print(f"\nSchätzwert \hat\lambda = {lambda_hat}")
print(f"\nTestwert = {test_value}")
print(f"\nKritische Grenze = {critical_value}")

if test_value <= critical_value:
    print("\nWir können davon ausgehen, dass die vorliegenden Ankunftsabstände exponentialverteilt sind.")
else:
    print("\nWir können davon NICHT ausgehen, dass die vorliegenden Ankunftsabstände exponentialverteilt sind.")
