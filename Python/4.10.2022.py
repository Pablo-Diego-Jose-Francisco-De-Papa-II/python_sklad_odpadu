def prva_uloha(veta):
    #Zadanie: Zadas jednu samohlasku, ktore bude pouzite na miestach ostatych samohlaskach.

    only_samohlaska = input("Zadaj samohlásku, ktorú chceš nahradiť: ")

    if only_samohlaska in "aeiouyáéíóúý":
        for letter in "aeiouyáéíóúý":
            veta = veta.replace(letter, only_samohlaska)
        return print(veta)
    else:
        print("Vieš čo je to samohláska?")

prva_uloha("Sedí mucha na stene, na stene, na stene. Sedí mucha na stene, sedí a spí. Sedí a buvinká potvorka malinká. Sedí mucha na stene, sedí a spí Sede meche ne stene ne stene ne stene...")


def druha_uloha(word):
    #Zadanie: Zadas slovo/ vetu, ktore nasledne spocita ich unicode charactery.
    
    sucet = int()
    for letter in word.upper():
        sucet += ord(letter)
    return print(sucet)

druha_uloha(input("Zadaj slovo: "))


def tretia_uloha(prve_slovo, druhe_slovo):
    #Zadanie: V oboch slovach sa spocita pismeno, ktore sa v tom slove nachadza a ktore si zadal.
    
    pismeno = input("Zadaj písmeno, ktoré chceš nájsť v oboch slovách: ")

    return print('V slove "{}" sa pismeno "{}" nachádza {}x a v slove "{}" {}x.'.format(prve_slovo, pismeno, prve_slovo.count(pismeno), druhe_slovo, druhe_slovo.count(pismeno)))

tretia_uloha(input("Zadaj prvé slovo: "), input("Zadaj druhé slovo: "))
