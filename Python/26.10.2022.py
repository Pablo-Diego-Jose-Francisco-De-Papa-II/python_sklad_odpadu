import random
import tkinter

canvas=tkinter.Canvas(width = 500, height = 500, bg = "silver")
canvas.pack()


def nulta_uloha(num):
    #Zadanie: Zapíš do txt súboru ľubovoľnú vetu.

    subor = open("data.txt", "a")
    subor.write("\nToto je {}.ty zápis".format(num))

nulta_uloha(6)


def prva_uloha():
    #Zadanie: Zisti koľko riadkov ma txt súbor.

    subor = open("data.txt", "r")
    cvicenie = subor.readlines()
    return print("Počet riadkov: ",len(cvicenie))

prva_uloha()

def druha_uloha():
    #Zadanie: Zapíš do txt z ineho txt prvý riadok.

    subor = open("data.txt", "r")
    riadok = subor.readline()
    
    while riadok != "":
        subor2 = open("data2.txt", "w")
        subor2.write(riadok)
        riadok = subor.readline()

druha_uloha()


def tretia_uloha():
    #Zadanie: Zapíš do txt z ineho txt ale zapíše sa každý riadok 2x.

    subor = open("data.txt", "r")
    subor2 = open("data2.txt", "a")
    riadok = subor.readline()
    
    while riadok != "":
        subor2.write(riadok)
        subor2.write(riadok)
        riadok = subor.readline()

tretia_uloha()


def stvrta_uloha():
    #Zadanie: Z 2 txt zapíšeme oba do jedneho txt.

    subor1 = open("číslo.txt", "r")
    subor2 = open("písmeno.txt", "r")
    subor3 = open("numlet.txt", "a")

    num = subor1.readline()
    let = subor2.readline()
    
    for i in range(100):
        subor3.write(num)
        num = subor1.readline()

    subor3.write("\n")
   
    for y in range(5):
        subor3.write(let)
        let = subor2.readline()

stvrta_uloha()
        

def piata_uloha():
    #Zadanie: Z 2 txt zapíšeme oba do jedneho txt, ale striedame subory po jednom.

    subor1 = open("číslo.txt", "r")
    subor2 = open("písmeno.txt", "r")
    subor3 = open("letnum.txt", "a")

    num = subor1.readline()
    let = subor2.readline()
    
    while let or num != "":
        subor3.write(num)
        num = subor1.readline()

        subor3.write(let)
        let = subor2.readline()

piata_uloha()


def siesta_uloha():
    #Zadanie: V jednom txt mame napisanu vetu, ktorú napíšeme do druhého txt ale vymeníme velkosti písmen(AHoj -> ahOJ).

    subor1 = open("novy_subor.txt", "r")
    subor2 = open("novsi_subor.txt", "a")

    veta = subor1.readline()
    subor2.write(veta.swapcase())

siesta_uloha()


def siedma_uloha():
    #Zadanie: Z txt si vezme útvar, jeho velkosť, polohu, farbu a vykreslí to tak.
    
    subor = open("zaznam.txt", "r")

    for i in range(5):
        zaznam = subor.readline()
        idk = zaznam.split()

        if "oval" == idk[0]:
            canvas.create_oval(idk[1], idk[2], idk[3], idk[4], fill = idk[5])
            
        elif "line" == idk[0]:
            canvas.create_line(idk[1], idk[2], idk[3], idk[4], fill = idk[5])
            
        elif "rectangle" == idk[0]:
            canvas.create_rectangle(idk[1], idk[2], idk[3], idk[4], fill = idk[5])

siedma_uloha()
