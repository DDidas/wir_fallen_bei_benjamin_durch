import numpy as np
from scipy import stats

# Apfelmasse Daten
data = list(map(int, input("Bitte geben Sie die Massen der Äpfel ein (getrennt durch '&'): ").split('&')))

# Mittelwert (Erwartungswert)
mean = np.mean(data)
print(f'Punktschätzungen für Erwartungswert, 𝑥̄ = {mean:.2f} g')

# Unverzerrte Stichprobenvarianz
variance = np.var(data, ddof=1)
print(f'Punktschätzungen für Varianz, 𝑠² = {variance:.2f} g²')

# Eingabe des Konfidenzniveaus (alpha) von der Konsole
alpha = float(input("Geben Sie das Konfidenzniveau (z.B. 0.1 für 90% oder 0.05 für 95%): "))

# Konfidenzintervall für den Mittelwert
sem = stats.sem(data)
ci_mean = stats.t.interval(1-alpha, len(data)-1, loc=mean, scale=sem)
print(f'Konfidenzintervall für Erwartungswert, {ci_mean[0]:.2f} ≤ 𝜇 ≤ {ci_mean[1]:.2f}')

# Konfidenzintervall für die Varianz
df = len(data) - 1
ci_variance = [df * variance / stats.chi2.ppf(1 - alpha/2, df),
               df * variance / stats.chi2.ppf(alpha/2, df)]
print(f'Konfidenzintervall für Varianz, 𝜎² gilt {ci_variance[0]:.2f} ≤ 𝜎² ≤ {ci_variance[1]:.2f}')
