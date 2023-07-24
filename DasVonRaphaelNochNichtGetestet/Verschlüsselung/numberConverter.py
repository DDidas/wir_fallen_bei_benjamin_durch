def dez2bin(num):
    out = []
    while num > 0:
        out.append(num & 1)
        num >>= 1
    if not out:
        out.append(0)
    out.reverse()
    print(out)
    return out


def bin2dez(bits):
    out = 0
    for bit in bits:
        out <<= 1
        out += bit

    return out

if __name__ == '__main__':
    B = dez2bin(122)
    print(bin2dez(B))