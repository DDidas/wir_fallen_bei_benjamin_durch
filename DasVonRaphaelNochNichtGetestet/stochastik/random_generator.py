"""
c und m muss teiler fremd sein

für alle primteiler p von m ist a -1 durch p teilbar

falls m und durch 4 teilbar ist a-1 (mod 4) = 0


a und c in {1,2,...,m-1}
    m > 2


"""


def f(x, a, c):
    o = (a * x + c) % m
    print(f"( {a}* {x} + {c} ) % {m} =", o)

    return o


a = 5
c = 3
m = 8

xn = 1
zahlen = []
for i in range(m):
    next = f(xn, a, c)
    zahlen.append(next)
    xn = next
print(zahlen)



def zufallstest():
    """
    es soll eine zufallszahl Z zwischen a-b
    überprüft werden

    z von x soll = (x-a)/(b-a)
    daraus folg x = a+z*(b-a)

    eine Normal verteilung sollte  sein 1-e^(-cx)

    das heißt 1-e^(-cx) = a+z*(b-a)

    :return:
    """