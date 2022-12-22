import tkinter

canvas=tkinter.Canvas()
canvas.pack()


def prva_uloha(x, y):
    #Zadanie: V txt súbore máme n počet farieb a podľa počtu farieb vykreslíme toľko štvorčekov.
    
    subor = open("subor.txt", "r")
    cvicenie = subor.read().split("\n")

    for farbicka in cvicenie:
        if x >= 100:
            x = 20
            y += 20

        canvas.create_rectangle(x -10,y - 10,x + 10,y + 10, fill = farbicka)
        x +=20

prva_uloha(20, 20)


def druha_uloha(color):
    #Zadanie: Z txt súbora sa ti vypíšu všetky farby z jednej premennej.

    subor = open("subor.txt", "r")
    cvicenie = subor.read()

    color += cvicenie.replace("\n",", ")
    print("Všetky farbičky: ", color)

druha_uloha(str())
