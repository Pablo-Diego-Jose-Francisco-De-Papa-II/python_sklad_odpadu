import turtle
import random as rd

turtli = turtle.Turtle()

turtli.speed(0)
turtle.delay(0)

def prva_uloha():
    turtli.penup()
    turtli.setx(-450)
    turtli.pendown()
    turtli.pensize(5)

    color = ["red", "blue", "yellow", "green", "cyan", "lime", "white"]

    for amount in range(20):
        lenght = rd.randint(50, 150)
        turtli.forward(lenght)
        turtli.fillcolor(rd.choice(color))
        turtli.begin_fill()
        for i in range(5):
            turtli.left(90)
            turtli.forward(lenght)
        turtli.left(30)
        turtli.forward(lenght)
        turtli.left(120)
        turtli.forward(lenght)
        turtli.left(30)
        turtli.forward(lenght)
        turtli.left(90)
        turtli.forward(lenght)
        turtli.end_fill()
prva_uloha()


def druha_uloha():
    for x in range(18):
        for y in range(36):
            turtli.fd(10)
            turtli.left(10)
        turtli.left(20)
druha_uloha()


def tretia_uloha():
    turtli.penup()
    turtli.setx(-450)
    turtli.pendown()

    for x in range(90):
        for y in range(36):
            turtli.fd(10)
            turtli.left(10)
        turtli.fd(10)
tretia_uloha()


def stvrta_uloha():
    for x in range(18):
        for y in range(36):
            turtli.fd(10)
            turtli.left(10)

        turtli.penup()
        turtli.fd(50)
        turtli.pendown()
        turtli.left(20)
stvrta_uloha()


def piata_uloha():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t4 = turtle.Turtle()

    t1.penup()
    t2.penup()
    t3.penup()
    t4.penup()

    t1.setpos(-200, 200)
    t2.setpos(200, 200)
    t3.setpos(200, -200)
    t4.setpos(-200, -200)

    t1.pendown()
    t2.pendown()
    t3.pendown()
    t4.pendown()

    turtle.delay(0)
    for i in range(360):
        t1.left(-1)
        t1.fd(-1)
        t2.left(1)
        t2.fd(1)
        t3.left(-1)
        t3.fd(1)
        t4.left(1)
        t4.fd(-1)


piata_uloha()
turtle.mainloop()
