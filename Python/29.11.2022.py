def prva_uloha(origo_tuple, new_tuple):
    #Zadanie: Z tuple sa ti vypisu len int.

    for item in origo_tuple:
        if isinstance(item, int):
            new_tuple += item,
    return print(new_tuple)

prva_uloha((3, "A", 5.19, "text", [4, 8, 2], 7, 3, "B"), tuple())


def druha_uloha(origo_tuple, new_tuple):
    #Zadanie: do tuple v tuple sa ti bude postupne pridavat item na pozicii n a n+1.

    for item in range(len(origo_tuple) - 1):
        new_tuple += (origo_tuple[item], origo_tuple[item + 1]),
        print(new_tuple)

druha_uloha((3, "A", 5, "G", 7, 3, "B", 19, "x"), tuple())


def tretia_uloha(word, zoznam):
    #Zadanie: Zadane slovo ti rozkuskuje v tvare(pozicia, pismeno na tej pozicii).

    for num, letter in enumerate(word, 1):
        zoznam += [num, letter],
    return print(zoznam)

tretia_uloha(input("Zadaj slovo: "), ())


def stvrta_uloha(cisla):
    #Zadanie: Z oboch tuple sa spocitaju cisla na tych istych poziciach.

    for item in range(len(cisla[0])):
        print(cisla[0][item] +  cisla[1][item])

stvrta_uloha(((1,2,3, 4),(5.2, 3.8, 4.3, 5.23)))
