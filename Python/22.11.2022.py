def prva_uloha(veta, odstup):
    #Zadanie: Vypíš text po riadkoch tak aby nepresiahlo n-pocet charakterov v ziadku.

    for i in range(0, len(veta), odstup):
        print(veta[i: i + odstup])

#prva_uloha("Čistím, čistím čižmičky,veď už nie som maličký.Do okna ich čisté dám,urobím to celkom sám.Počuj,milý Mikuláš,iste do nich niečo dáš?Celý rok som dobrý bol,dokonca som podrástol.Pomáhal som mamičke,nebral hračky sestričke,pomáhal som tatovi,nerobil zle bratovi.No a pani učiteľke,obrázky som kreslil veľké.Už sa teším,už to viem,že dnes niečo dostanem.", int(input("Zadaj aké chceš mať riadkovanie: ")))


def druha_uloha(veta, odstup):
    #Zadanie: Vypis vetu po riadkoch tak, ze riadok nepresiahne n pocet charakterov a zaroven sa nesplitnu slova.

    veta_split = veta.split()
    riadok = ""

    for word in veta_split:
        if len(riadok) + len(word) < odstup:
            riadok += word + " "

        else:
            riadok += word + " "
            print(riadok)
            riadok = ""

druha_uloha("Čistím, čistím čižmičky, veď už nie som maličký. Do okna ich čisté dám, urobím to celkom sám. Počuj, milý Mikuláš, iste do nich niečo dáš? Celý rok som dobrý bol, dokonca som podrástol. Pomáhal som mamičke, nebral hračky sestričke, pomáhal som tatovi, nerobil zle bratovi. No a pani učiteľke, obrázky som kreslil veľké. Už sa teším, už to viem, že dnes niečo dostanem.", int(input("Zadaj aké chceš mať riadkovanie: ")))
