"""
Binomial verteilung

Exponential verteilung



"""



class Kugel:

    def __init__(self, id, wahrscheinlichkeit):
        self.id = id
        self.wahrscheinlichkeit = wahrscheinlichkeit


class VersuchMitZurückLegen:
    def __init__(self, ziehungen, menge, focus):
        self.ziehungen = ziehungen
        self.menge = menge
        self.focus = focus

    def erwartungswert(self, focus=None):
        if focus is None: focus = self.focus
        print("mü von x")

    def varianz(self):
        pass

    def verschiebungssatz(self):
        pass

    def baum(self, b, p=1, n=0):
        if n > self.ziehungen: return b
        b[0] = p
        for o in self.menge:
            b.append(self.baum([], p * o.wahrscheinlichkeit, n + 1))
        return b

    def baumdurchsuchen(self, baum, tiefe, erwartung, ziel):
        baum


print("Possion Verteilung")

print("Wahrscheinlichkeitsdichtefunktion")


def häfuigkeit(liste):
    out = {}
    for i in liste:
        if not i in out.keys():
            out[i] = 1
        out[i] += 1
    return out


