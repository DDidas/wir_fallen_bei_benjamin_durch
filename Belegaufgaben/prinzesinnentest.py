import math
from scipy.stats import t

# Werte von der Konsole nehmen
mu_0 = float(input("Geben Sie den Sollwert mu_0 ein: ")) # Sollwert
n = int(input("Geben Sie die Stichprobengröße n ein: ")) # Stichprobengröße
x_bar = float(input("Geben Sie den Mittelwert x_bar ein: ")) # Mittelwert
s = float(input("Geben Sie die Standardabweichung s ein: ")) # Standardabweichung
alpha = float(input("Geben Sie die Irrtumswahrscheinlichkeit alpha ein: ")) # Irrtumswahrscheinlichkeit

# Kritischer Wert
df = n - 1  # Freiheitsgrade
c = -t.ppf(1 - alpha, df)  # Kritischer Wert aus der Quantiletabelle der Student-t-Verteilung
print("Der kritische Wert c ist:", c)

# Testwert
t_hat = (x_bar - mu_0) / (s / math.sqrt(n))  # Testwert
print("Der Testwert t_dach ist:", t_hat)

# Testentscheidung
if t_hat < c:
    print("Die Nullhypothese wird abgelehnt, weil t_dach kleiner als c ist.")
else:
    print("Die Nullhypothese wird nicht abgelehnt, weil t_dach nicht kleiner als c ist.")
