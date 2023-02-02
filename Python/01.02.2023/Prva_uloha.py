import tkinter as tk
import random as rd

root = tk.Tk()
root.title("brm brm auticka. Yippe!")
canvas = tk.Canvas(root, width=1480, height=444)
canvas.pack()


red_pos = 0
blue_pos = 1480

track = tk.PhotoImage(file="track.png")
canvas.create_image(740, 222, image=track)

red = tk.PhotoImage(file="red_car_no_bg.png")
canvas.create_image(red_pos, 222, image=red, tags="red_car")

blue = tk.PhotoImage(file="blue_car_no_bg.png")
canvas.create_image(blue_pos, 222, image=blue, tags="blue_car")

fire = tk.PhotoImage(file="fire.png")


def start(go):
    global red_pos, blue_pos, red_move, blue_move

    while red_pos + 100 <= blue_pos - 100:
        red_move = rd.randint(1,10)
        blue_move = rd.randint(1, 10)

        canvas.move("red_car", red_move, 0)
        canvas.move("blue_car", -blue_move, 0)

        red_pos += red_move
        blue_pos -= blue_move

        canvas.update()
        canvas.after(10)
    else:
        canvas.create_image(red_pos + 100, 210, image=fire)
        canvas.create_text(red_pos + 100, 150, text = "BUM BÁC", font="Arial 70 bold", fill="red")
canvas.bind("<Button-1>", start)
