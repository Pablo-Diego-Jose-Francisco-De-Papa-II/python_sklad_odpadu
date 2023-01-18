import random
import tkinter

canvas=tkinter.Canvas(width = 500, height = 500, bg = "silver")
canvas.pack()

def prva_uloha():
    #Zadanie: kliknutin posunies obdlnik or something like that

    canvas.create_rectangle(25, 25, 100, 75, fill="red", tags = "obdlznik")

    def north_west(nw):
        canvas.move("obdlznik", 10, 10)

    def south_east(se):
        canvas.move("obdlznik", -10, -10)

    canvas.bind("<Button-1>", north_west)
    canvas.bind("<Button-3>", south_east)

#prva_uloha()


def druha_uloha(zoznam):
    #Zadanie: 1. stvorec sa vykresli tam kde kliknes
    #         2. rozdel GUI na 4 kvadranty, stred a v kazdom kvadrante sa ti vyfarbi stvorec inak

    canvas.create_rectangle(-20, -20, 20, 20, fill = "red", width = 2, tags = "stvorec")

    def move(mouse):
        canvas.move("stvorec", mouse.x - zoznam[-2], mouse.y - zoznam[-1])
        zoznam.extend([mouse.x, mouse.y])

        if mouse.x < 250:
            if mouse.y < 250:
                canvas.itemconfig("stvorec", fill = "yellow")
            elif mouse.y > 250:
                canvas.itemconfig("stvorec", fill = "lime")

        elif mouse.x > 250:
            if mouse.y < 250:
                canvas.itemconfig("stvorec", fill = "blue")
            elif mouse.y > 250:
                canvas.itemconfig("stvorec", fill = "orange")

        elif mouse.x == mouse.y == 250:
            canvas.itemconfig("stvorec", fill = "red")

        if len(zoznam) > 4:
            zoznam.pop(0)
            zoznam.pop(1)

    canvas.bind("<Button-1>", move)

#druha_uloha([0, 0])


def tretia_uloha(zoznam):
    #Zadanie: nemam tusaka

    canvas.create_line(zoznam, tags = "lajna")

    def click(mouse):
        zoznam.extend([mouse.x, mouse.y])
        canvas.coords("lajna", zoznam)
    canvas.bind("<Button-1>", click)

#tretia_uloha([10, 10, 60, 200])


def stvrta_uloha():
    #Zadanie: pri pohybe sa vykreslia kruhy

    def ring(mouse):
        color = random.randint(100000, 999999)
        canvas.create_oval(mouse.x - 10, mouse.y - 10, mouse.x + 10, mouse.y + 10, fill = "#" + str(color))

    canvas.bind("<B1-Motion>", ring)
#stvrta_uloha()


def piata_uloha(zoznam):
    #Zadanie: sprav volaco

    def click(mouse):
        global ciara
        zoznam[:] = [mouse.x, mouse.y]
        ciara = canvas.create_line(0, 0, 0, 0)

    def motion(mouse):
        zoznam.extend([mouse.x, mouse.y])
        canvas.coords(ciara, zoznam)

    canvas.bind("<Button-1>", click)
    canvas.bind("<B1-Motion>", motion)

piata_uloha([])
