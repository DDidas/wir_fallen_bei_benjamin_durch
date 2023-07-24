import collections
 
 
def prf_prim(ein):
    print("Ergebnis für die Zahl", ein)
    prim_arr = []
    di = 2
    while di ** 2 <= ein:
        while (ein % di) == 0:
            prim_arr.append(di)
            ein //= di
        di += 1
    if ein > 1:
        prim_arr.append(ein)
    print(prim_arr)
 
    for (basis, hochz) in collections.Counter(prim_arr).items():
        print(basis, "**", hochz)
 
 
def main():
    prf_prim(24)
    prf_prim(0)
    prf_prim(105)
 
 
if __name__ == '__main__':
    main()
