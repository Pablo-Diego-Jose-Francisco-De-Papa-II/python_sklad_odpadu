import tkinter as tk
import random as rd

root = tk.Tk()
root.title("Downgraded skicar.exe")
canvas = tk.Canvas(root, width = 500, height = 500, bd = 10, bg = "silver")
canvas.pack()


cords = []

def stvrte_cvicenie_klik(x, y):
    global line, cords
    color = rd.choice(["blue", "red", "green", "yellow", "cyan", "pink"])
    cords = [x, y]
    line = canvas.create_polygon(0, 0, 0, 0, width = 4, fill = color)

def stvrte_cvicenie_motion(x, y):
    cords.extend([x, y])
    canvas.coords(line, cords)

def click(mouse):
    stvrte_cvicenie_klik(mouse.x, mouse.y)

def move(mouse):
    stvrte_cvicenie_motion(mouse.x, mouse.y)

canvas.bind("<Button-1>", click)
canvas.bind("<B1-Motion>", move)
