"""
Diskrete Mathematik beschäftigt sich mit endlich bzw. höchstens abzählbar unendlichen Mengen und den auf ihnen
definierten Operationen.

- Kombinatorik, Zahlentheorie, Kryptographie, Graphentheorie, Algebra, Codierungstheorie

Axiome der Natürlichen Zahlen
1. Die Null ist eine natürliche Zahl
2. Jede natürliche Zahl n hat eine eindeutig bestimmte natürliche Zahl als Nachfolger
3. Die null ist kein Nachfolger einer natürlichen Zahl
4. Zwei unterschiedliche natürliche Zahlen haben auch unterschiedliche Nachfolger.
5. Enthält eine Teilmenge M der natürlichen Zahlen die Null und mit jeden n in M auch den Nachfolger von n, dann ist M
    gerade die Menge der natürlichen Zahlen


Prinzip der Vollständigen Induktion
Gegeben ist eine von der natürlichen Zahl n abhängige Aussage A(n).
Sind
    1. Induktionsanfang bzw. Verankerung: Die Aussage A gilt für eine natürliche Zahl n0, das heißt, es gilt A(n0)
    2. Induktionsschritt: Für jede natürliche Zahl n>=n0 folgt aus der Gültigkeit von A(n) auch die Gültigkeit von A(n+1).
erfüllt, dann gilt die Aussage A für alle natürlichen Zahlen n >= n0.


Axiome für q,p,r in Rationalenzahlen Q:
1. Es gibt neutrale Elemente 0,1 in Q für Addition und Multiplikation: q+0=q und q*1=q.
2. Es gelten die Kommutativgesetze p+q = q+p , p*q = q*p
3. Es gelten die Assoziativgesetze (p+q)+r = p+(q+r), (p*q)*r = p*(q*r)
4. Es gilt das Distributiv gesetz: p*(q+r) = p*q+p*r
5. Es gibt Inverse Elemente bezüglich der Addition und der Mulitiplikation:
    Addition q in Q => -q in Q
    Mulitplikation q in Q\0 => 1/q in Q




Definition Körper
Gegeben sind eine nichtleere Menge K und zwei Abbildungen + und *, wobei stets gitl, dass falls k1,k2 in K auch k1+k2 und
k1*k2 in K sind. Erfüllt K zusammen mit + und * die Axiome I-V, so nennt man (K,+,*) einen Körper.


Ein Element heißt Einheit, wenn es ein b in Zn gibt, sodass a*b=1 gilt bzw. a*b===1 mod n in Kongruenzschreibweise.
Man sagt dass b multiplikativ inverse zu a ist
"""


"""
Kryptographie ist der Versuch eine Nachricht sicher über einen unsicheren Kanal zu versenden.

Definition Kryptosystem:
Ein Tripel (P,C,K) heißt Kryptosystem, wobei
 P eine endliche Menge von Klartexten ist (plain texts),
 C eine endliche Menge von Geheimtexten (cipher texts),
 K eine endliche Menge von Schlüsseln (keys)
ist, wenn  für jedes Schlüsselpaar ke,kd in K eine Chiffrierungsregel (encryption rule) eke: P -> C und eine Dechiffrierungsregel 
(decryption rule) dkd: C->P existiert, sodass für ein KLartext m in P (message) die Bedingung dkd(eke(m))=m erfüllt ist.


Kerckhoffs Prinzip
Nach dem Prinzip von Auguste Kerckhoff (1835-1903) beruht die Sicherheit eines Verschlüsselungsverfahrens auf der 
Geheimhaltung des (mindestens eines) Schlüssels (private key) zwischen Sender und Empfänger bzw. mit anderen Worten:
Ein Geheimtext darf ohne Kenntnis des Schlüssels nicht effizient dechiffrierbar sein.

Vorteile: es müssen nur schlüssel geändert werden, algorithmen sind schwieriger geheimzuhalten als schlüssel

Das Kryptosystem (P,C,K) gilt als perfekt sicher, falls Kenntnis des Geheimtextes c in C nichts über die gesendete Message 
m in P verrät, also P(m|c) = P(m) gilt.
"""