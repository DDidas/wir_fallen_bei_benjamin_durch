def F(x, verteilung):
    out = 0
    for i in verteilung:
        if i > x: break
        out += verteilung[i] * i
    print(f"F({x})=",out)
    return out

def erwartungswert_mü(verteilung,gx=None):
    # mü , u
    out = 0
    for i in verteilung:
        out += i * (1/len(verteilung) if not gx else gx(i))
    return out

def varianz_sigmaQuadrat(verteilung):  # mü , u

    erwartWert = erwartungswert_mü(verteilung)
    print("Erwartungswert mü = ", erwartWert)
    out = erwartungswert_mü(verteilung, lambda x: (x - erwartWert) ** 2)
    print("Varianz sigma^2=", out)

    return out

def standartabweichung_sigma(verteilung):
    t = varianz_sigmaQuadrat(verteilung)

    print("Standartabweichung sigma=", t ** 0.5)

    return t ** 0.5


if __name__ == '__main__':
    F(8.5, {0: 4 / 5, 3: 0.1, 8: 1 / 20, 11: 1 / 20})
    standartabweichung_sigma([7.74 ,9.16, 4.95, 6.61 ,6.28 ,8.59 ,5.26 ,6.47])