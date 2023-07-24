from decoding import *


def ceasar(wort, schluessel):
    print(f'Cäser Verschlüsselung: {wort}, {schluessel}')
    out = ""
    debug = ""
    debug2 = ""
    for w in wort:
        o = key_value(w)
        debug += f"{w} {o} "
        z = value_key(o + schluessel)

        debug2 += f"{ord(z) - start} {z} "
        out += z
    print(debug)
    print(debug2)
    print(out)
    return out


def ceasar_inverse(wort, schluessel):
    return ceasar(wort, -schluessel)


def vigenere(wort, schluessel):
    print(f"Vigenere: {wort}, {schluessel}")
    le = len(schluessel)
    out = ""
    debug = ""
    debug2 = ""
    i = 0
    for w in wort:
        k = key_value(w)
        lv = key_value(schluessel[i % le])
        debug += f"{w} {k}+{lv} "
        z = value_key(k + lv)
        out += z
        debug2 += f"{z} {k + lv}%{dif} {(k + lv) % dif}  "
        i += 1
    print(debug)
    print(debug2)
    print(out)
    return out


def vigenere_inverse(wort, schluessel):
    print(f"Vigenere: {wort}, {schluessel}")
    le = len(schluessel)
    out = ""
    debug = ""
    debug2 = ""
    i = 0
    for w in wort:
        k = key_value(w)
        lv = key_value(schluessel[i % le])
        debug += f"{w} {k}-{lv} "
        z = value_key(k - lv)
        out += z
        debug2 += f"{z} {k + lv}%{dif} {(k + lv) % dif}  "
        i += 1
    print(debug)
    print(debug2)
    print(out)
    return out


if __name__ == '__main__':
    p = vigenere("AMEISE","ADRIAN")
    print(p)
    vigenere_inverse(p,"NUDELN")
    vigenere("NUDELN","NVSMHE")