def prva_uloha(cislo, result):
    # Zadanie: Všetky čísla v liste vynásobíš.

    for num in cislo:
        result *= num
    return print(f"Výsledok po vynásobení listu je {result}.")

prva_uloha([3, 4, 2, 5], 1)


def druha_uloha(zoznam):
    #Zadanie: Vypíš itemy z listu na párnych pozíciach.

    return print(f"Na párnych pozíciach v liste sa nachádzajú tieto veci -> {zoznam[0::2]}")

druha_uloha([2, "A", 4, 6, "!", "T", 3, 4, 3, 2])


def tretia_uloha(od, po, umocnene):
    #Zadanie: Vypíš mocniny čísel od 1 po n.

    for num in range(od, po + 1, 1):
        umocnene.append(num ** 2)
    print(f"Mocniny od {od} po číslo {po} -> {umocnene}")

tretia_uloha(1, int(input("Zadaj číslo po ktoré chceš pracovať: ")), [])


def stvrta_uloha(zoznam, vymazat):
    #Zadanie: Z listu vymaž čísla, ktoré sám zadáš.

    vymazat = vymazat.split()

    for list in vymazat:
        for num in zoznam:
            if num == int(list):
                zoznam.remove(num)
    return print(zoznam)

stvrta_uloha([0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0], input("Aké číslo/ čísla by si chcel zmazať z listu? "))
