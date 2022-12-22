def prva_uloha():
    #Zadanie: Vypíš mená a priezviská ľudí zo txt súboru.

    subor = open("žiaci.txt", "r")
    riadok = subor.readline()

    while riadok != "":
        slovo = riadok.split()
        print("Meno:        {} \nPriezvisko:  {}\n".format(slovo[0], slovo[1]))
        riadok = subor.readline()

prva_uloha()


def druha_uloha():
    #Zadanie: Vypíš mená a priezviská ľudí zo txt súboru, ale bez pouzitia commandu split.

    subor = open("žiaci.txt", "r")
    riadok = subor.readline()

    while riadok != "":
        medzera = riadok.find(" ")
        print("MENO:        ", riadok[0:medzera])
        print("PRIEZVISKO: ", riadok[medzera:])
        riadok = subor.readline()
druha_uloha()


def tretia_uloha():
    #Zadanie: Vypíš priemer žiakov. 

    subor = open('Známky.txt')
    list_ziakov = subor.read().split("\n")

    for riadok in list_ziakov:
        info_list = riadok.split()
        meno = info_list[0]
        znamky_list, znamky = list(info_list[1]), 0

        for str in znamky_list:
            znamky += int(str)

        priemer = znamky / len(znamky_list)
        print("{} má priemer známok {}".format(meno, priemer))

tretia_uloha()
