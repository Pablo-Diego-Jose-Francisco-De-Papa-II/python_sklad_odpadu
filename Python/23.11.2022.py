def prva_uloha(anagram, maybe_anagram):
    #Zadanie: Zisti či slovo je anagram or not.
    
    if sorted(anagram) == sorted(maybe_anagram):
        print("Slovo {} je anagram!".format(anagram))

#prva_uloha(input("Zadaj slovo (maybe anagram!): "), input("Zadaj 2. slovo a možno to bude fakt anagram: "))


def druha_uloha(num, neopakovane_num):
    #Zadanie: Vypíš koľko krát sa čislo opakuje ak sa nachádza v liste viac ako 1x.

    for i in num:
        opakovane = num.count(i)
        
        if opakovane > 1 and i not in neopakovane_num:
            neopakovane_num.append(i)
            print("Číslo {} sa opakuje {} krát.".format(i, opakovane))

druha_uloha([8, 3, 2, 8, 5, 4, 3, 1, 0], [])
