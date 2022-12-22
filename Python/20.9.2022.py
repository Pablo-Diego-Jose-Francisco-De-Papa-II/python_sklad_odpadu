import random

def prva_uloha(word_or_sentence, letter):
    #Zadanie: Program ti spocita kolko krat sa zadane pismeno nachadza v zadanej vete/ slove.

    return print(word_or_sentence.count(letter))

prva_uloha(input("Zadaj slovo alebo vetu: "), input("Zadaj písmeno, ktorého chceš vedieť počet výskytov v danej vete/ slove: "))


def druha_uloha(word):
    #Zadanie:  Porovnaj či sa slovo a slovo len opačne napísané rovnajú.

    if word == word[::-1]:
        return print("Slová sú rovnaké z oboch strán! :)")
    else:
        return print("Slová nie sú rovnaké z oboch strán! :(")

druha_uloha(input("Zadaj slovo, ktoré chceš overiť či je rovnaké keď sa otočí: "))


def tretia_uloha(rodne_cislo):
    #Zadanie: Vypíš rodné číslo bez "/".

    return print("Tvoje rodné číslo {} bolo upravené na {}.".format(rodne_cislo, rodne_cislo.replace("/", "")))

tretia_uloha("274519/9632")
