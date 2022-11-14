import string


def osszevonhato(minterm_1, minterm_2) -> list:
    minterm_1 = list(minterm_1)
    minterm_2 = list(minterm_2)
    eltero_bitek = 0
    elteres_helye = 0
    for i in range(0, len(minterm_1)):
        if minterm_1[i] != minterm_2[i]:
            eltero_bitek += 1
            elteres_helye = i
    if eltero_bitek == 1:
        return [True, elteres_helye]
    else:
        return [False, None]


def valtozokra_konvertal(binaris) -> string:
    ascii_karakterek = list(string.ascii_uppercase)
    binaris_alak = list(binaris)
    valtozokkal = ""
    for i in range(0, len(binaris_alak)):
        if binaris_alak[i] == '0':
            valtozokkal += "!" + ascii_karakterek[i]
        else:
            valtozokkal += ascii_karakterek[i]
    return valtozokkal


def tizesbol_kettesbe(minterm_sorszam, valtozok_szama) -> string:
    binarisan = bin(minterm_sorszam).replace("0b", "")
    if valtozok_szama > len(binarisan):
        bit_kulonbseg = valtozok_szama - len(binarisan)
        potol = '0' * bit_kulonbseg
        binarisan = potol + binarisan
    return binarisan


def sulyszam(minterm_sorszam, valtozok_szama) -> int:
    binarisan = list(tizesbol_kettesbe(minterm_sorszam, valtozok_szama))
    _sulyszam = 0
    for i in binarisan:
        if i == '1':
            _sulyszam += 1
    return _sulyszam


def szotarbol_lista(szotar_reszlet) -> list:
    seged = []
    for i in szotar_reszlet:
        seged.extend(szotar_reszlet[i])
    return seged


def visszafejt(minterm):
    hianyzo_bitek = minterm.count('-')
    if hianyzo_bitek == 0:
        return [str(int(minterm, 2))]
    lista = [bin(i)[2:].zfill(hianyzo_bitek) for i in range(pow(2, hianyzo_bitek))]
    seged = []
    for i in range(pow(2, hianyzo_bitek)):
        seged2 = minterm[:]
        a = -1
        for j in lista[0]:
            if a != -1:
                a = a + seged2[a + 1:].find('-') + 1
            else:
                a = seged2[a + 1:].find('-') + 1
            seged2 = seged2[:a] + j + seged2[a + 1:]
        seged.append(str(int(seged2, 2)))
        lista.pop()
    return seged


def quine_mccluskey(minterm_sorszamok, valtozok_szama) -> None:
    prim_implikansok = set()
    sulyszam_csoportok = dict()
    # Sulyszam szerint rendezzuk a mintermeket
    for minterm in minterm_sorszamok:
        try:
            sulyszam_csoportok[sulyszam(minterm, valtozok_szama)].append(tizesbol_kettesbe(minterm, valtozok_szama))
        except KeyError:
            sulyszam_csoportok[sulyszam(minterm, valtozok_szama)] = [tizesbol_kettesbe(minterm, valtozok_szama)]

    print("\n\n Sulycsoport\tMinterm sorszam\t\tBinarisan")
    print(47 * "-")
    for i in sorted(sulyszam_csoportok.keys()):
        print(f'\t{i}:')
        for j in sulyszam_csoportok[i]:
            print(f'\t\t\t\t\t{int(j, 2)}\t\t\t\t{j}')
        print(47 * "-")

    while True:
        seged = sulyszam_csoportok.copy()
        csoportok = dict()
        sorszam = 0
        megjeloltek = set()
        megallas = True
        kulcsok = sorted(list(seged.keys()))
        for i in range(0, len(kulcsok) - 1):
            for j in seged[kulcsok[i]]:
                for k in seged[kulcsok[i + 1]]:
                    _osszevonhato = osszevonhato(j, k)
                    if _osszevonhato[0]:
                        try:
                            sulyszam_csoportok[sorszam].append(j[:_osszevonhato[1]] + '-' + j[_osszevonhato[1] + 1:]) if j[:_osszevonhato[1]] + '-' + j[_osszevonhato[1] + 1:] not in sulyszam_csoportok[sorszam] else None
                        except KeyError:
                            sulyszam_csoportok[sorszam] = [j[:_osszevonhato[1]] + '-' + j[_osszevonhato[1] + 1:]]
                        megallas = False
                        megjeloltek.add(j)
                        megjeloltek.add(k)
            sorszam += 1
        jeloletlenek = set((szotarbol_lista(seged))).difference(megjeloltek)
        prim_implikansok = prim_implikansok.union(jeloletlenek)
        print("A tábla prímimplikánsai", None if len(jeloletlenek) == 0 else ', '.join(jeloletlenek))
        if megallas is True:
            print("\n\nÖsszes prímimplikáns ", None if len(prim_implikansok) == 0 else ', '.join(prim_implikansok))
            break

        print("\n\n Sulycsoport\tMinterm sorszam\t\tBinarisan")
        for z in sorted(sulyszam_csoportok.keys()):
            print(f'\t{z}:')
            for p in sulyszam_csoportok[z]:
                print(f'\t\t\t\t\t{p}\t\t\t\t{p}')
            print(47 * "-")


if __name__ == '__main__':
    """print("Q(ABC....F)=Σmi(i=m1,m2,m3....)")
    mintermek = input("Minterm szamok(i): ")
    valtozok_szama = int(input("Valtozok szama: "))

    mintermek = minterms.split(',')
    mintermek = [int(x) for x in minterms]
    minterek.sort()"""
    teszt_eset = [1, 3, 12, 13, 14, 15, 17, 19, 28, 29, 30, 31]
    teszt_valtozo_szam = 5
    quine_mccluskey(teszt_eset, teszt_valtozo_szam)
    vege = input("Nyomjon Enter-t a bezáráshoz...")
