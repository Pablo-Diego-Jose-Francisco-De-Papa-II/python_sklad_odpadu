import tkinter

canvas=tkinter.Canvas()
canvas.pack()

def prva_uloha(x, y):
    #Zadanie: Vytvorte program, ktorý importne z txt súboru farby a vyfarbí 10 štvorčekov ľubovolnej velkosti, ktoré si vytvoríte. :)

    subor = open("farbicky.txt", "r")
    exercise = subor.readline()
    color = exercise.split()
    
    for farbicka in range(len(color)):
        canvas.create_rectangle(x, y, x + 30, y + 30, fill = color[farbicka])
        x += 30

prva_uloha(30, 30)


def druha_uloha():
    #Ak si ma vysmial za zapísanie 1 úlohy. Tak zaprvé kys a podruhé kys.
    #Zadanie: Vytvorte program, ktorý vykreslí 10 kruhov z txt súboru v ktorom budete mať zadané údaje(x pozícia, y pozícia, polomer, farbička).

    subor = open("kruh.txt", "r")
    kruh = subor.readline()
            
    while kruh != "":
        kruh2 = kruh.split()
        canvas.create_oval(kruh2[0], kruh2[1], int(kruh2[0]) + int(kruh2[2]), int(kruh2[1]) + int(kruh2[2]), fill = kruh2[3])    
        kruh = subor.readline()
        
druha_uloha()
canvas.mainloop()
