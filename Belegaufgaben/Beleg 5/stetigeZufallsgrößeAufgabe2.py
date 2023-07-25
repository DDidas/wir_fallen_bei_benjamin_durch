import sympy as sp

def main():
    print("Geben Sie den LaTeX-Code ein:")

    a = sp.symbols('a')  # Platzhalter 'a' erstellen

    F_X_expr = sp.Piecewise(
        (0, sp.Symbol('x') < -1),
        (a*(-sp.Symbol('x')**3/3+sp.Symbol('x')**2+3*sp.Symbol('x')+5/3), sp.And(-1 <= sp.Symbol('x'), sp.Symbol('x') <= 3)),
        (1, sp.Symbol('x') > 3)
    )

    # Berechnungen
    a_val = sp.solveset(F_X_expr.subs(sp.Symbol('x'), 3) - 1, a).args[0]  # Parameter a
    F_X_expr = F_X_expr.subs(a, a_val)

    # Wahrscheinlichkeiten
    P_X_geq_1 = 1 - F_X_expr.subs(sp.Symbol('x'), 1)  # P(X>=1)
    P_neg2_leq_X_leq_1 = F_X_expr.subs(sp.Symbol('x'), 1) - F_X_expr.subs(sp.Symbol('x'), -2)  # P(-2<=X<=1)

    # Wahrscheinlichkeitsdichtefunktion
    f_X_expr = sp.diff(F_X_expr, sp.Symbol('x'))

    # Erwartungswert
    mu = sp.integrate(sp.Symbol('x')*f_X_expr, (sp.Symbol('x'), -sp.oo, sp.oo))  # Erwartungswert µ

    # Ausgabe der Ergebnisse
    print(f"Der Parameter a= {a_val}")
    print(f"Die Wahrscheinlichkeit für P(X>=1)= {P_X_geq_1}")
    print(f"Die Wahrscheinlichkeit für P(-2<=X<=1)= {P_neg2_leq_X_leq_1}")
    print(f"Der Erwartungswert µ= {mu}")

if __name__ == "__main__":
    main()
