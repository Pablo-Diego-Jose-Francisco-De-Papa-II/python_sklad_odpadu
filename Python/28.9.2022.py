def prva_uloha(word):
    #Zadanie: Zadáš slovo a vypíše sa ti to slovo kde sa medzi písmenami bude nachádzať písmeno "X".

    for item in word:
       answer = "X".join(word)
    return print(answer)

prva_uloha(input("Zadaj slovo: "))


def druha_uloha(word, new_word):
    #Zadanie: V zadanom slove sa každé písmeno vypíše 2x.

    for pismeno in word:
        new_word += pismeno * 2
    return print(new_word)
    
druha_uloha(input("Zadaj slovo: "), str())


def tretia_uloha(word, new_word):
    #Zadanie: Opakuje sa podla toho na akej pozicii sa nachadza Slovo sa ti upraví.

    for num, letter in enumerate(word, 1):
        new_word += letter * num
    return print('Tvoje zadané slovo "{}" sa zmenilo na "{}".'.format(word, new_word))
    
tretia_uloha(input("Zadaj slovo: "), str())


def stvrta_uloha(word):
    #Zadanie: Kazde druhe pismeno nahradime "X".

    for i in range(len(word)):
        if i % 2 == 1:
            word = word.replace(word[i], "X")
    return print(word)
    
stvrta_uloha(input("Zadaj slovo: ") )


def piata_uloha(word, sifra):
    #Zadanie: JETOZAKODOVANYTEXT -> TEJAZODOKAVOTYNTXE

    word = word.replace(" ", "")

    for i in range(0, len(word), 3):
        first_3_letters = word[i:i + 3][::-1]
        sifra += "".join(first_3_letters)
    return print(sifra)

piata_uloha(input('Zadaj slovo, ktoré chceš "Zašifrovať": '), str())
