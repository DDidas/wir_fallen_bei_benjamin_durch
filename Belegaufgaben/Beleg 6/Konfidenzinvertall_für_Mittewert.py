import scipy.stats as stats
import math

def confidence_interval_mean(x, s_square, n, gamma):
    # Berechnung der Freiheitsgrade
    df = n - 1

    # Berechnung des Quantils c der Student-t-Verteilung
    c = stats.t.ppf((1 + gamma) / 2, df)
    print(f"Der Wert von c ist: {c}")

    # Berechnung des Konfidenzintervalls für den Mittelwert
    lower_bound = x - c * math.sqrt(s_square / n)
    upper_bound = x + c * math.sqrt(s_square / n)

    return lower_bound, upper_bound

if __name__ == "__main__":
    x = float(input("Geben Sie den Stichprobenmittelwert x ein: "))
    s_square = float(input("Geben Sie die empirische Varianz s^2 ein: "))
    n = int(input("Geben Sie die Stichprobengröße n ein: "))
    gamma = float(input("Geben Sie das Konfidenzniveau gamma (z.B. 0.9 für 90%): "))

    lower_bound, upper_bound = confidence_interval_mean(x, s_square, n, gamma)

    print(f"Das Konfidenzintervall für den Mittelwert ist: [{lower_bound}, {upper_bound}]")