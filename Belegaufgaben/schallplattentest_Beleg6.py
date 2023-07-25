import math
from scipy.stats import t

# Werte von der Konsole nehmen
mu_0 = float(input("Geben Sie den Sollwert mu_0 ein: ")) # Sollwert
n = int(input("Geben Sie die Stichprobengröße n ein: ")) # Stichprobengröße
x_bar = float(input("Geben Sie die mittlere Masse x_bar ein: ")) # mittlere Masse
s = float(input("Geben Sie die Standardabweichung s ein: ")) # Standardabweichung
alpha = float(input("Geben Sie die Irrtumswahrscheinlichkeit alpha ein: ")) # Irrtumswahrscheinlichkeit

# Kritischer Wert
df = n - 1  # Freiheitsgrade
c = t.ppf(1 - alpha/2, df)  # Kritischer Wert aus der Quantiletabelle der Student-t-Verteilung
print("Der kritische Wert c ist:", c)

# Testwert
u_hat = (x_bar - mu_0) / (s / math.sqrt(n))  # Testwert
print("Der Testwert u_dach ist:", u_hat)

# Testentscheidung
if -c <= u_hat <= c:
    print("Die Nullhypothese wird nicht abgelehnt, weil u_hat innerhalb des Annahmebereichs [-c,c] liegt.")
else:
    print("Die Nullhypothese wird abgelehnt, weil u_hat außerhalb des Annahmebereichs [-c,c] liegt.")
