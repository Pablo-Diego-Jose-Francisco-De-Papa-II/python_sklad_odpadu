import random


#veta retazec
#pismeno
#ci sa nachadza
def prva_uloha():
    o = 0
    x = input("Napíš slovo/ vetu: ")
    y = input("Napíš pismeno ,ktoré chceš nájsť: ")

    for i in range(len(x)):
        z = x[i]
        if y == z:
            o += 1
    print(o)
#prva_uloha()

def druha_uloha_len_zle():      
    x = input("Napíš slovo: ")
    o = 0

    for i in range(len(x)):
        o = o - 1
        print(x[o])
#druha_uloha_len_zle()


def tretia_uloha():
    x = input("Napíš slovo: ")

    for i in range(len(x)):
        if x == x[::-1]:
            print("same")
        else:
            print("not same")
#tretia_uloha()

def me_when_born():
    x = "274519/9632"
    print(x[0:6], x[7:12])
me_when_born()
