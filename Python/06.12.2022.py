import tkinter
import random

canvas=tkinter.Canvas(width = 750, bg = "silver")
canvas.pack()


def prva_uloha(mouse):
    #Zadanie: Klikutím na plátno sa ti vykreslí 5 kruhov a každý bude mať inú farbu.

    num = 50

    for i in range(5):
        color = random.randint(100000, 999999)
        canvas.create_oval(mouse.x - num, mouse.y - num, mouse.x + num, mouse.y + num, fill = "#" + str(color))
        num -= 10

canvas.bind('<Button-1>', prva_uloha)


word = list("Python")
def druha_uloha(mouse):
    #Zadanie: Vypíš slovo po písmenkách na plátno.

    if len(word) == 0:
        canvas.create_rectangle(0, 0, 760, 280, fill = "red")
        canvas.create_text(375, 135, text = "STOP", font = ("Arial" ,"70", "bold"))
    else:
        canvas.create_text(mouse.x, mouse.y, text = word[0])
        word.pop(0)

canvas.bind('<Button-1>', druha_uloha)


def tretia_uloha():
    #Zadanie: Vytvor hlavolam. To ti stačí ni?
    
    max_cislo = int(input("Po aké číslo chceš hrať (max 12): "))
    if max_cislo < 13:
        zoznam = []

        for num in range(max_cislo + 1):
            zoznam.append(num)
        random.shuffle(zoznam)

        canvas.create_text(375, 135, text = "click to continue", font = ("Arial", "35", "bold"))

        def hlavolam(mouse):
            canvas.delete("all")

            if 100 < mouse.y < 150:
                policko = (mouse.x // 50) - 1

                if 50 < mouse.x < (max_cislo + 2) * 50:
                    zoznam[zoznam.index(0)] = zoznam[policko]
                    zoznam[policko] = 0

            velkost = 0
            for cislo in zoznam:
                canvas.create_rectangle(50 + velkost, 100, 100 + velkost, 150, width = 2)
                if cislo != 0:
                    canvas.create_text(velkost + 75, 125, text = cislo, font=("Arial", "15", "bold"))
                velkost += 50

            win = sorted(zoznam)
            win.remove(0)
            win.append(0)


            if zoznam == win:
                print("Yippe!")
                canvas.delete("all")
                canvas.create_text(375, 135, text = "YOU WON!", font = ("Arial", "35", "bold"))

        canvas.bind("<Button-1>", hlavolam)

    else:
        print("POVEDAL SOM MAX 12!")
        canvas.create_text(375, 135, text = "POVEDAL SOM MAX 12!", font = ("Arial", "35", "bold"))

tretia_uloha()
