def vereinigung(A,B):
    out = B[:]
    for a in A:
        if a not in B:
            out.append(a)
    return out


def schnitt(A,B):
    out = []
    for a in A:
        for b in B:
            if a == b:
                out.append(a)
    return out


