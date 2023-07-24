from scipy.stats import poisson

#Wahrscheinlichkeit gleich einem Wert
poisson.pmf(k=5, mu=3)
#Wahrscheinlichkeit kleiner als irgendein Wert
poisson.cdf(k=4, mu=7)
#Wahrscheinlichkeit größer als irgendein wert
1-poisson.cdf(k=20, mu=15)
