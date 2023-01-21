import tkinter as tk
import random as rd

root = tk.Tk()
root.title("Downgraded skicar.exe")
canvas = tk.Canvas(root, width = 500, height = 500, bd = 10, bg = "silver")
canvas.pack()


cords = []

def prva_uloha():
    def ctrl_v(x, y):
        global line, cords
        color = rd.choice(["blue", "red", "green", "yellow", "cyan", "pink"])
        cords = [x, y]
        line = canvas.create_polygon(0, 0, 0, 0, width = 4, fill = color)

    def ctrl_c(x, y):
        cords.extend([x, y])
        canvas.coords(line, cords)

    def click(mouse):
        ctrl_v(mouse.x, mouse.y)

    def move(mouse):
        ctrl_c(mouse.x, mouse.y)

    canvas.bind("<Button-1>", click)
    canvas.bind("<B1-Motion>", move)
prva_uloha()



suradnice_move = None
line = canvas.create_line(0, 0, 0, 0)
suradnice_click = []

def druha_uloha():
    def click(m):
        global suradnice_move, suradnice_click, line

        suradnice_move = m.x, m.y
        line = canvas.create_line(0, 0, 0, 0)
        suradnice_click.extend([suradnice_move])
        canvas.coords(suradnice_click)


    def move(m):
        global suradnice_move, line

        if suradnice_move is None: return

        canvas.delete(line)
        canvas.update()
        line = canvas.create_rectangle(suradnice_move, m.x, m.y)


    canvas.bind("<Motion>", move)
    canvas.bind("<Button-1>", click)
druha_uloha()



velkost = 25
sur = [250, 250, 250, 250]
stvorcek = canvas.create_rectangle(sur[0] - velkost, sur[1] - velkost, sur[2] + velkost, sur[3] + velkost, fill = "red", width = 5)
grab = False

def tretia_uloha():
    def click(mouse):
        global grab, sur

        if mouse.x >= sur[-4] - velkost and mouse.y >= sur[-3] - velkost and mouse.x <= sur[-2] + velkost and mouse.y <= sur[-1] + velkost:
            grab = True

    def motion(mouse):
        global grab, velkost, stvorcek, sur

        if not grab:
            return

        canvas.delete(stvorcek)
        sur.extend([mouse.x - velkost, mouse.y - velkost, mouse.x + velkost, mouse.y + velkost])
        stvorcek = canvas.create_rectangle(sur[-4], sur[-3], sur[-2], sur[-1], fill = "red", width = 5)
        canvas.update()

    def unclick(x):
        global grab

        grab = False

    canvas.bind("<Button-1>", click)
    canvas.bind("<B1-Motion>", motion)
    canvas.bind("<ButtonRelease>", unclick)
tretia_uloha()
