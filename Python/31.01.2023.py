import tkinter as tk
import random as rd

root = tk.Tk()
root.title("brm brm game where you cant do anything!")
canvas = tk.Canvas(root, width=1480, height=444, bg="silver")
canvas.pack()

track = tk.PhotoImage(file="track.png")
canvas.create_image(740, 222, image=track)

red_pos = 0
blue_pos = 0
red_time = 0
blue_time = 0

red = tk.PhotoImage(file="red_car_no_bg.png")
canvas.create_image(red_pos, 111, image=red, tags="red_car")

blue = tk.PhotoImage(file="blue_car_no_bg.png")
canvas.create_image(blue_pos, 333, image=blue, tags="blue_car")

while red_pos <= 1250 or blue_pos <= 1250:
    red_move = rd.randint(1, 10)
    blue_move = rd.randint(1, 10)

    canvas.move("red_car", red_move, 0)
    canvas.move("blue_car", blue_move, 0)

    red_pos += red_move
    blue_pos += blue_move

    blue_time += 0.01
    red_time += 0.01

    if red_pos < 1250:
        cas2 = canvas.create_text(1445, 111, text=round(red_time, 3), font="Arial 25 bold", fill = "white")
        cas4 = red_time
    else:
        canvas.create_text(1445, 111, text=round(cas4, 3), font="Arial 25 bold", fill="white")

    if blue_pos < 1250:
        cas1 = canvas.create_text(1445, 333, text=round(blue_time, 3), font="Arial 25 bold", fill = "white")
        cas3 = blue_time
    else:
        canvas.create_text(1445, 333, text=round(cas3, 3), font="Arial 25 bold", fill="white")

    canvas.update()
    canvas.after(1)

    if red_pos < 1250 or blue_pos < 1250:
        canvas.delete(cas1)
        canvas.delete(cas2)
else:
    if red_pos > blue_pos:
        print("RED WINS!")
        canvas.create_rectangle(440, 150, 1040, 294, fill="white", outline="#ff393a", width=10)
        canvas.create_text(740, 222, text="RED WINS!", font="Arial 70 bold", fill="#ff393a")
    elif red_pos == blue_pos:
        print("DRAW!")
        canvas.create_rectangle(440, 150, 1040, 294, fill="white", outline="#3270a9", width=10)
        canvas.create_text(740, 222, text="DRAW!", font="Arial 70 bold", fill="#ff393a")
    else:
        print("BLUE WINS!")
        canvas.create_rectangle(440, 150, 1040, 294, fill="white", outline="#3270a9", width=10)
        canvas.create_text(740, 222, text="BLUE WINS!", font="Arial 70 bold", fill="#3270a9")
