import numpy as np
from scipy import stats


#Eingabe in diesem Script durch den Plain MAth Tabellenteil unten, mit den ganzen & getrennt und so, wie in probeklausur. u know?

# Apfelmasse Daten
data = list(map(int, input("Bitte geben Sie die Massen der Äpfel ein (getrennt durch '&'): ").split('&')))

# Mittelwert (Erwartungswert)
mean = np.mean(data)
print(f'Punktschätzungen für Erwartungswert, 𝑥̄ = {mean:.2f} g')

# Unverzerrte Stichprobenvarianz
variance = np.var(data, ddof=1)
print(f'Punktschätzungen für Varianz, 𝑠² = {variance:.2f} g²')

# Konfidenzniveau
alpha = 0.05 # für 95% Konfidenzintervall

# Konfidenzintervall für den Mittelwert
sem = stats.sem(data)
ci_mean = stats.t.interval(1-alpha, len(data)-1, loc=mean, scale=sem)
print(f'Konfidenzintervall für Erwartungswert, {ci_mean[0]:.2f} ≤ 𝜇 ≤ {ci_mean[1]:.2f}')

# Konfidenzintervall für die Varianz
df = len(data) - 1
ci_variance = [df * variance / stats.chi2.ppf(1 - alpha/2, df),
               df * variance / stats.chi2.ppf(alpha/2, df)]
print(f'Konfidenzintervall für Varianz, 𝜎² gilt {ci_variance[0]:.2f} ≤ 𝜎² ≤ {ci_variance[1]:.2f}')
