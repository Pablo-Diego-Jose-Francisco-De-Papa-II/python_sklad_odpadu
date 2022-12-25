def encryption(sifra, abeceda, posun, nove_slovo):
    for letter in sifra:
        num = abeceda.index(letter)
        nove_slovo += abeceda[num - posun]
    print(nove_slovo)

encryption("silneheslorazdvatri", "abcdefghijklmnopqrstuvwxyz", 5, str())

def dencryption(sifra, abeceda, posun, nove_slovo):
    for letter in sifra:
        num = abeceda.index(letter)
        nove_slovo += abeceda[num - posun]
    print(nove_slovo)

dencryption("ndgizczngjmvuyqvomd", "zyxwvutsrqponmlkjihgfedcba", 5, str())


def encryption(sifra, abeceda, abeceda_but_backwards, nove_slovo):
    what_will_do = int(input("Ak chceš zašifrovať tvoju správu tak napíš 1 ak chceš odkryptovať napíš 2. "))
    sifra = sifra.replace(" ", "")
    sifra = sifra.lower()
    smth = []

    if what_will_do == 1:
        posun = int(input("Zadaj o koľko pozícií chceš posúvať: "))

        for letter in sifra:
            num = abeceda.index(letter)
            nove_slovo += abeceda[num - posun]

    elif what_will_do == 2:
        vie_nevie = int(input("Vieš o koľko sa chceš posúváť? Ak hej napíš 1, ak nie napíš 2. "))

        if vie_nevie == 1:
            posun = int(input("Zadaj o koľko pozícií chceš posúvať: "))

            for letter in sifra:
                num = abeceda_but_backwards.index(letter)
                nove_slovo += abeceda_but_backwards[num - posun]

        elif vie_nevie == 2:

            for times in range(len(abeceda_but_backwards)):
                for letter in sifra:
                    num = abeceda_but_backwards.index(letter)
                    nove_slovo += abeceda_but_backwards[num - times]
                smth.append(nove_slovo)
                nove_slovo = str()
            nove_slovo = smth

    return print(nove_slovo)

encryption(input("Zadaj slovo, ktoré chceš zašifrovať alebo odšifrovať: "), "abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba", str())
