import tkinter as tk
import random as rd

root = tk.Tk()
root.title("Halooooooo. Kto tam?")
canvas = tk.Canvas(root, width=1480, height=444, bg="silver")
canvas.pack()


track = tk.PhotoImage(file="track.png")
canvas.create_image(740, 222, image=track)
red_pos = 0
blue_pos = 0

red = tk.PhotoImage(file="red_car_no_bg.png")
canvas.create_image(red_pos, 111, image=red, tags="red_car")

blue = tk.PhotoImage(file="blue_car_no_bg.png")
canvas.create_image(blue_pos, 333, image=blue, tags="blue_car")

while red_pos <= 1250 and blue_pos <= 1250:
    red_move = rd.randint(1, 10)
    blue_move = rd.randint(1, 10)

    canvas.move("red_car", red_move, 0)
    canvas.move("blue_car", blue_move, 0)

    red_pos += red_move
    blue_pos += blue_move
    canvas.update()
    canvas.after(5)
else:
    if red_pos >= 1250:
        print("red wins!")
    else:
        print("blue wins!")

    canvas.create_text(740, 222, text = "kys", font = "Arial 70 bold", fill = "red")
