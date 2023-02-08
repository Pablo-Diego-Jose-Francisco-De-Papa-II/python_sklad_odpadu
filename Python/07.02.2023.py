import turtle
import random

turtli = turtle.Turtle()


def prva_uloha():
    turtli.fillcolor("red")
    turtli.begin_fill()
    for i in range(360):
        turtli.fd(1)
        turtli.left(1)
    turtli.end_fill()
prva_uloha()


def druha_uloha():
    for x in range(5):
        turtli.fillcolor("red")
        turtli.begin_fill()
        for i in range(4):
            turtli.fd(50)
            turtli.left(90)
        turtli.end_fill()
        turtli.penup()
        turtli.fd(60)
        turtli.pendown()
druha_uloha()


def tretia_uloha():
    n = 5
    turtli.pensize(2)
    
    for x in range(n):
        colors = random.randint(100000, 999999)
        turtli.fillcolor("#" + str(colors))
        turtli.begin_fill()

        for y in range(9):
            turtli.fd(10)
            turtli.left(10)

        turtli.left(90)

        for y in range(9):
            turtli.fd(10)
            turtli.left(10)
            
        turtli.end_fill()
        turtli.left(90)
        turtli.left(360 / n)
tretia_uloha()
turtle.mainloop()
