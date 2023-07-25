import numpy as np

# Eingabe der Daten über die Konsole
input_data = input("Bitte geben Sie die Werte ein, getrennt durch '&': ")

# Umwandlung der Eingabe in eine Liste von Zahlen
delta_t = np.array([int(i) for i in input_data.split('&')])

# Eingabe des Quantils über die Konsole
quantile_value = float(input("Bitte geben Sie den Wert für das Quantil ein (z.B. 0.65): "))

# Berechnung des Mittelwerts
mean_delta_t = np.mean(delta_t)
print(f"Mittelwert \overline{{\Delta t}} = {mean_delta_t}")

# Berechnung des gewünschten Quantils
quantile = np.quantile(delta_t, quantile_value)
print(f"{quantile_value}-Quantil \Delta t_{{{quantile_value}}} = {quantile}, zur eingabe runden auf ganze Zahlen!")

# Berechnung des Schätzwertes für den Parameter lambda
lambda_hat = 1 / mean_delta_t
print(f"Schätzwert \hat\lambda = {lambda_hat}")
