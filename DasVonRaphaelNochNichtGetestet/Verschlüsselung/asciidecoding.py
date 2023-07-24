start = ord("A")  # A = 0
ende = ord("z")
dif = ende - start + 1


def set(_start, _ende):
    global start, ende, dif
    start = _start
    ende = _ende
    dif = ende - start + 1


def key_value(c):
    return ord(c) - start


def value_key(k):
    return chr((k % dif) + start)


def str2nums(st, split):
    out = []
    for i in range(0, len(st), split):
        strblock = st[i:i + split]
        out.append(str2num(strblock))
    return out


def nums2str(nums):
    out = ""
    for num in nums:
        out += num2str(num)
    return out


def str2num(st):
    out = 0
    for w in st:
        o = key_value(w)
        out *= 10 ** 2
        out += o
    return out


def num2str(num):
    out = ""
    for i in range(2):
        tmp = num // 10 ** 2
        tmp *= 10 ** 2
        z = num - tmp
        c = value_key(z)
        out = c + out
        num //= 10 ** 2
    return out
