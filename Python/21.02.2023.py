import turtle
import random as rd

turtli = turtle.Turtle()


def prva_uloha():
    # Zadanie: Budes tvorit spiralovy stvorec. Thats all

    move = 10
    for i in range(69):
        turtli.fd(move)
        turtli.left(90)
        move += 10
#prva_uloha()


def druha_uloha():
    # Zadanie: Upravit prve zadanie aby bol random uhol. KYS

    uhol = rd.randint(30, 170)
    move = 10

    for i in range(100):
        turtli.left(uhol)
        turtli.fd(move)
        move += 10
#druha_uloha()


def tretia_uloha():
    # Zadanie: Uprav druhe zadanie, ktore je upravene prve zadanie tak, ze pohyb je rovnaky a uhol je napriklad 8 a
    # zakazdym sa ti pripocita 1 v loope k nemu.

    uhol = 10

    for i in range(2000):
        turtli.left(uhol)
        turtli.fd(10)
        uhol += 1
#tretia_uloha()


def stvrta_uloha():
    #Zadanie: Nakresli picovinu cez turtle

    move = 10
    velkost = 200/2
    turtli.speed(0)

    while True:
        angle = rd.randint(30, 360)
        turtli.forward(move)

        if not -velkost <= turtli.xcor() <= velkost or not -velkost <= turtli.ycor() <= velkost:
            turtli.undo()
            turtli.right(angle)

            if turtli.xcor() > velkost:
                turtli.setx(velkost)
            elif turtli.xcor() < - velkost:
                turtli.setx(-velkost)
            if turtli.ycor() > velkost:
                turtli.sety(velkost)
            elif turtli.ycor() < -velkost:
                turtli.sety(-velkost)
        turtli.right(angle)
stvrta_uloha()
turtle.mainloop() #nice
