

decodedict = {
    ' ': 0,
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}
lastvalue = list(decodedict.values())[-1]
dif = lastvalue +1
SPLIT = 2
print(dif)
def set(decoded):
    global decodedict
    decodedict = decoded


def key_value(c):
    return decodedict[c]


def value_key(value):
    if value == 0:
        return ' '
    for key in decodedict:
        if decodedict[key] == value:
            return key


def str2nums(st, split):
    global SPLIT
    SPLIT = split
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

ppp=0
def num2str(num):
    global ppp
    out = ""
    for i in range(SPLIT):
        tmp = num // 10 ** 2
        tmp *= 10 ** 2
        z = num - tmp
        c = value_key(z)
        out = c + out
        num //= 10 ** 2
    return out
