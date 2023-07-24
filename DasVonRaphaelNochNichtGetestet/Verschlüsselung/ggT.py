def ggT(a, b):  # a=3 b = 31
    gr = max((a, b))
    kl = min((a, b))

    q = gr // kl
    r = gr % kl
    # print(f"{gr} = {q} * {kl} + {r}")
    return kl if r == 0 else ggT(kl, r)


def erweiterter_euklid(a, b, history=None):  # ! a >= b
    q = a // b
    r = a % b

    if r == 0:
        return b, history[1]
    if history is None:
        history = [[0, 1], [1, -q]]
        print(f"{a}={q}*{b}+{r} | {r}={a}-{q}*{b} | s={history[1][0]} t={history[1][1]}")
        return erweiterter_euklid(b, r, history)

    a1, a2 = history[0]
    history[0] = history[1].copy()

    history[1][0] *= -q
    history[1][1] *= -q

    history[1][0] += a1
    history[1][1] += a2
    print(f"{a}={q}*{b}+{r} | {r}={a}-{q}*{b} | s={history[1][0]} t={history[1][1]}")
    return erweiterter_euklid(b, r, history)


if __name__ == '__main__':
    a, b = 2760, 13
    ggt, (s, t) = erweiterter_euklid(a, b)
    print(f"{ggt} = {s}*{a} + {t}*{b} = {s * a + t * b}")
