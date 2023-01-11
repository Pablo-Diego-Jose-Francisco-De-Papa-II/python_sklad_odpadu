import tkinter

canvas=tkinter.Canvas(width = 500, height = 500, bg = "silver")
canvas.pack()

def prva_uloha():
    #Zadanie: mas sa zabit a zomriet... :)

    canvas.create_rectangle(25, 25, 100, 75, fill="red", tags = "p")

    def click(mouse):
        canvas.move("p", 10, 10)

    canvas.bind("<Button-1>", click)

    def click(mouse):
        canvas.move("p", -10, -10)

    canvas.bind("<Button-3>", click)

prva_uloha()


def druha_uloha(zoznam):
    #Zadanie: sprav volaco
    
    canvas.create_rectangle(-20, -20, 20, 20, fill="red", width = 2, tags="stvorec")
    canvas.create_rectangle(250,250, 250,250)
    def click(mouse):
        zoznam.extend([mouse.x, mouse.y])
        canvas.move("stvorec", mouse.x - zoznam[-4], mouse.y - zoznam[-3])

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
        elif mouse.x and mouse.y == 250:
            canvas.itemconfig("stvorec", fill = "red")

        if len(zoznam) > 4:
            zoznam.pop(0)
            zoznam.pop(1)

    canvas.bind("<Button-1>", click)

druha_uloha([0, 0])


def tretia_uloha(zoznam):
    canvas.create_line(zoznam, tags = "lajna")

    def click(mouse):
        zoznam.extend([mouse.x, mouse.y])
        canvas.coords("lajna", zoznam)
    canvas.bind("<Button-1>", click)

tretia_uloha([10, 10, 60, 200])


def stvrta_uloha():
    color = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "A", "B", "C", "D", "E", "F"]
    def happy_face(mouse):
        canvas.create_oval(mouse.x - 10, mouse.y - 10, mouse.x + 10, mouse.y + 10)

    canvas.bind("<B1-Motion>", happy_face)
stvrta_uloha()

def piata_uloha(zoznam):

    def happy_face(mouse):
        zoznam.extend([mouse.x, mouse.y])
        canvas.create_line(zoznam)

    canvas.bind("<B1-Motion>", happy_face)

piata_uloha([])
