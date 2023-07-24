"""
Kardinalität einer Menge ist die

Definition Zufallsexperiment
1. lassen sich unter gleichen äußeren Bedingungen beliebig oft wiederholen
2. haben mehrere sich ausschließende Ergebnisse
3. Ergebnisse sind nicht sicher vorhersagbar

Ein Zufallsexperiment habe endlich viele bzw. allenfalls abzählbar unendlich viele sich gegenseitig ausschließende
 Ergebnisse w1,w2,... die sogenannten Elementarereignisse.

w1,w2,... sind in der Menge Omega, Omega ist die Ergebnismenge des Zufallsexperiments und für eine Abbildung
   p: Omega -> [0,1] (Intervall von 0 bis 1) mit der Eigenschaft
   sum(p(w) for w in Omega) = 1 heißt das Tupel (Omega, p) diskreter Wahrscheinlichkeitsraum. Teilmengen A aus Omega
   nennen wir Ereignisse und bezeichnen A insbesondere als
    1. unmögliches Ereignis, falls A=Leer gilt
    2. Elementarereignis, falls |A| = 1 gilt
    3. Sicheres Ereignis. falls A = Omega gilt

Wahrscheinlichkeit nach den Kolmogorov-Axiomen
1. P(A) ist eine nichtnegative Zahl kleiner oder gleich 1, 0<=P(A)<=1
2. Für Fall A = Omega (sicheres Ereignis) gilt P(A)=1
3. für parweise disjunkte Ereignisse A1, A2,... gilt
P(A1 u A2 u ...) = P(A1)+P(A2)+...


Die Wahrscheinlichkeit für das Eintreten von B unter der Voraussetzung dass A bereitseinetreten ist heißt bedingte
  Wahrscheinlichkeit von B unter der Bedingung A, symbolisch P(B|A). Sie wird durch
       P(B|A)=P(A ^ B)/P(A)
  berechnet. Die Wahrscheinlichkeit für das gleichzeitige Eintreten von A und B ist dann durch
       P(A ^ B) = P(A) * P(B|A)
gegeben

Stochastisch unabhängig:
Gilt P(A ^ B) = P(A)*P(B) so heißen A und B stochastisch unabhängig


Definition Zufallsgröße
Eine Abbildung X:Omega-> Reelle Zahlen, die jedem Elementarereignis w des Ergebnisraums Omega eine reelle Zahl x duch
  x = X(w) zuordnet, heißt Zufallsgröße bzw. Zufallsvariable, und x nennt man Realisierung von X.

  Kann x dabei nur endlich viele oder abzählbar unendlich viele Werte annehmen, nennen wir X eine diskrete Zufallsgröße

Definition Verteilungsfunktion:
Die Funktion Fx: R-> [0,1], die für eine vorgegebene reelle Zahl x angibt wie groß die Wahrscheinlichkeit ist, dass
die Zufallsgröße X Werte annimmt, die kleiner oder gleich x sind, heißt Verteilungsfunktion von X,
   Fx(x)= P(X<=x)
Seien xi die Realisierung einer diskreten Zufallsgröße X mit pi = P(X=xi). Dann heißst durch
    fx(x)=P(X=x)= falls x==xi:pi sonst:0
  definierte Funktion auch Wahrscheinlichkeitsfunktion von X.

Kurz Definition Erwartungswert
Der Erwartungswert von X ist der über alle Realisierungen xi von X gemittelte Wert, wobei mit den jeweiligen
Punktwarscheinlichkeiten pi gewichtet wird

kurz Definition Varianz
Die Varianz von X zeigt an, wie stark die Zufallsgröße X im Durchschnitt von ihrem Erwartungswert abweicht


Sei X eine Diskrete Zufallsgröße mit Wahrschenlichkeitsfunktino fx. Dann heißen
  - mü_x= u = E(X)= Sum(mit i in N: xi*fx(xi)) Erwartungswert (auch Mittelwert) von X, wobei die absolute Konvergenz
  der rechts stehenden Reihe vorausgesetzt werden muss.

  - sigma_x^2 = ox^2 = Var(X) = Sum für i in N [ (xi-ux)^2 * fx(xi) ] die Varianz von X.
            Schneller Var(x) = E(X^2) - mü_x^2

  - sigma_x = ox = sqrt(Var(X)) die Standartabweichung von X.


Ist Y=g(X) eine von der Zufallsgröße X (mit Wahrscheinlichkeitsfunktion fx) abhängige Funktion, so ist der Erwartungswert
von Y duch E(Y)= für i in N sum(g(xi)*fx(xi))


Definition Verteilungen

Gleichverteilung
Eine Zufallsgröße X, bei der jede Realisierung x1,...,xn mit der Wahrscheinlichkeit 1/n eintritt, heißt gleichverteilt.
Ihre Wahrscheinlichkeits- und Verteilungsfunktion sind gemäß
 fx(x) = P(X=x) = 1/n falls x=xi für i = 1 bist n sonst 0
 Fx(x) = P(X<=x) = len(X[:i])/n

Binomialverteilung
Ein Bernoulli-Experiment mit den beiden sich gegenseitig ausschließenden Ergebnissen A und Â werden n-Fach ausgeführt.
Dann genügt die Zufallsgröße X, die die Anzahl der Versuche kennzeichnet, in denen A eintritt, der Binomialverteilung.
Ihre Wahrscheinlichkeits- und Verteilungsfunktion sind

f(x) = P(X=x) = (x aus N)* p^x * (1-p)^(n-x) falls x=0,1,2,...,n sonst 0
F(x) = P(X<=x) = floor(x) * f(x)

und man nennt n und p die Parameter der Binomialverteilung.



Poisson-Verteilung
sigma^2 = n*p*(1-p)
mü = n * p

Für Parameter lambda >0 heißt die Verteilung der Zufallsgröße X mit Wahrscheinlichkeits- und Verteilungsfunktion
 fx(x) = P(X=x) = (lambda)^x/x! * e^-lambda wenn x in N

 Fx(x) = P(X<=x) = e^-lambda * sum k=0 bis floor(x) (lambda^k /k!  )

 lambda = sigma^2 = mü





Normalverteilung
sigma^2 = n*p*(1-p)
mü = n * p

"""
