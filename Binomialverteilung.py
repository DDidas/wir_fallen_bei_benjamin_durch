from scipy.stats import binom
#p=wahrscheinlichkeit
#k anzahl zutreffend
#n anzahl wiederholungen
# Binomialwahrscheinlichkeit berechnen
#genau k mal
binom.pmf(k=10, n=12, p=0.6)
# k mal oder weniger
binom.cdf(k=2, n=5, p=0.5)
#zwischen 4 und 6
binom.cdf(k=6, n=10, p=0.7) - binom.cdf(k=3, n=10, p=0.7)
