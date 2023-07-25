import scipy.stats as stats

def confidence_interval_sigma_square(x, s_square, n, gamma):
    # Berechnung der Freiheitsgrade
    df = n - 1

    # Berechnung der Vertrauensgrenzen c1 und c2
    c1 = stats.chi2.ppf((1 - gamma) / 2, df)
    c2 = stats.chi2.ppf(1 - (1 - gamma) / 2, df)

    # Berechnung des Konfidenzintervalls für sigma^2
    lower_bound = (n - 1) * s_square / c2
    upper_bound = (n - 1) * s_square / c1

    return lower_bound, upper_bound

if __name__ == "__main__":
    x = float(input("Geben Sie den Stichprobenmittelwert x ein: "))
    s_square = float(input("Geben Sie die empirische Varianz s^2 ein: "))
    n = int(input("Geben Sie die Stichprobengröße n ein: "))
    gamma = float(input("Geben Sie das Konfidenzniveau gamma (z.B. 0.9 für 90%): "))

    lower_bound, upper_bound = confidence_interval_sigma_square(x, s_square, n, gamma)

    print(f"Das Konfidenzintervall für sigma^2 ist: [{lower_bound}, {upper_bound}]")
