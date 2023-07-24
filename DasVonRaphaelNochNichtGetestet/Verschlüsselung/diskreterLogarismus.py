def diskreterLogarismus():
    """
    Bsp:
        Berechne:
            log_2(3) (mod 11)^p <=> Für welches k gilt 2^k === 3 mod(11)

    Eine Gruppe (G,°) ist eine Menge G zusammen mit einer Abbildung.
    °: GxG->G:
        - es gibt ein neutrales Element e, d.h. g°e = e°g = g für alle g in G
        - Abgeschlossenheit: Für alle g1,g2 in G ist g1°g2 in G
        - zu jedem g in G existiert ein Inverses g^-1 in G mit g°g^-1= g^-1°g = e  g^-1 ist g schlange
        - assoziativitätsgesetz gilt.
    Ist (Z_n,+,*) gewöhnlicher Restklassenring, dann ist (Z*_n,*) eine Gruppe, wenn n eine Primzahl ist,
        wobei  Z*_n = Z_n\{0}
    Das Element g in G (wobei (G,°) Gruppe ist) heißt Erzeuger von G, wenn
    G= {g^k: k in Z}
    g^0:= e, g^k:=g°g°...°g, g^-k:=h°h°...°h (wobei h inverse zu g)

    :return:
    """

    pass

def GruppeErzeuger(n):

    pass