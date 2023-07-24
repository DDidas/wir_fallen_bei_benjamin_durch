import Zufallsexperiment
import Unserd.binomialkoeffizient as bk


class Binomial(Zufallsexperiment.Zufallsexperiment):

    def __init__(self, züge, WS_für_positiv, p=None, zufallsgröße=None):
        super().__init__(elementarWS={"p": WS_für_positiv, "n": 1 - WS_für_positiv}, p=p, zufallsgröße=zufallsgröße,
                         max_zufallsgr=züge)
        self.züge = züge

    def zufallsgröße(self,x):
        out = 0
        for i in x:
            if i == "p":
                out += 1
        return out

    def punktWSzufallsGröße(self, x):
        p = self.elemWSvon("p")
        p2 = self.elemWSvon("n")
        n = self.züge
        out = (p ** x) * (p2 ** (n - x)) * bk.x_aus_n(x, n)
        return out



if __name__ == '__main__':



    exp = Binomial(züge=39,WS_für_positiv=1/365)
    exp.standartabweichung_sigma()
    exp.verteilFunkZufallsGrößeAb(2)

