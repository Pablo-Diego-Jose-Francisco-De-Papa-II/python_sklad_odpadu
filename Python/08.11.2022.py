def prva_uloha(week):
    #Zadanie: Vypíš teplotu pre každý deň.
    
    for day, temp in enumerate(week, 1):
        print("{}. deň bola teplota {}°C.".format(day, temp))

    #Zadanie: Vyiš priemernú teplotu.
    print("\nPriemernná teplota celého týždňa je {}°C.".format(round(sum(week) / len((week)), 2)))

    #Zadanie: Vypíš najvyššiu a najnižšiu teplotu.
    print("\nNajvyššia teplota za posledný týždeň bolo {}°C a najnižšia {}°C.\n".format(max(week), min(week)))

    #Zadanie: Rozdel teploty podľa toho či sú pár alebo nepár.
    par =   [num for num in week if num % 2 == 0]
    nepar = [num for num in week if num % 2 == 1]

    print("Pár:   {}".format(par))
    print("Nepár: {}".format(nepar))

#prva_uloha([24, 5, 26, 0, 245, 15, 74])


def druha_uloha():
    #Zadanie: nwm

    subor = open("cisla.txt", "r")
    cvicenie = subor.read().split(",")

    yes = open("yes.txt", "w")
    no  = open("no.txt", "w")

    for num in cvicenie:
        if int(num) % 5 == 0:
            yes.write(num + " ")

        else:
            no.write(num + " ")

druha_uloha()
