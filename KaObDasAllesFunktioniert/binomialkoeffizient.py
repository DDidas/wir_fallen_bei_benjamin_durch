from math import factorial as fac


def x_aus_n(x,n):
    return fac(n)/(fac(x)*fac(n-x))
