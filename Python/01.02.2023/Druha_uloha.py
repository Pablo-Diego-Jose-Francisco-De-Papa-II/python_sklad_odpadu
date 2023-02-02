import turtle as tu
import random as rd

t = tu.Turtle()


#t.clear() -> #poszicia zostane
#t.reset() -> #pozicia sa vrati na 0, 0


def prva_uloha():
    #Zadanie: Vykreslia sa ti stvorce na korytnica a budu mat random velkost, poziciu, farbu...

    for pocet in range(30):
        t.penup()
        uhol = rd.randint(0, 90)
        velkost = rd.randint(10, 50)
        farba = rd.choice(["red", "blue", "lime", "yellow", "silver", "black"])
        x_pos = rd.randint(-400, 400)
        y_pos = rd.randint(-400, 400)
        t.setpos(x_pos, y_pos)
        t.pensize(velkost + 1)
        t.pendown()
        t.pencolor(farba)
        t.left(uhol)
        for i in range(4):
            t.forward(velkost)
            t.left(90)
prva_uloha()


def druha_uloha():
    #Zadanie: Budes vykreslovat random stvorce a trojuholniky

    for pocet in range(30):
        t.penup()
        uhol = rd.randint(0, 90)
        x_pos = rd.randint(-400, 400)
        y_pos = rd.randint(-400, 400)
        utvar = rd.choice(["stvorec", "trojuholnik"])
        t.setpos(x_pos, y_pos)
        t.pensize(50 + 1)
        t.pendown()
        t.left(uhol)
        if utvar == "stvorec":
            for i in range(4):
                t.pencolor("red")
                t.forward(50)
                t.left(90)
        if utvar == "trojuholnik":
            t.pencolor("blue")
            t.forward(50)
            t.left(120)
            t.forward(50)
            t.left(120)
            t.forward(50)
druha_uloha()


def tretia_uloha():
    #Zadanie: Vykresli od 3-uholnika po 16-uholnik

    for pocet in range(3, 19):
        for i in range(pocet):
            t.forward(50)
            t.left(360 / pocet)
tretia_uloha()
tu.mainloop()
