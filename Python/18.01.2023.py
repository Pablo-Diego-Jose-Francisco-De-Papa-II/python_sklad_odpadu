import tkinter as tk

root = tk.Tk()
root.title("I wanna die")
canvas = tk.Canvas(root, width = 500, height = 500, bd = 10, bg = "silver")
canvas.pack()

def press_event(event):
    print(event.keysym)
    if event.keysym == "Right":
        canvas.create_text(50, 70, text = "Walter White")
    elif event.keysym == "Left":
        canvas.create_text(200, 160, text = "308 Negra Arroyo Lane Albarquqie New Mexico")
canvas.bind_all("<Left>", press_event)
canvas.bind_all("<Right>", press_event)

canvas.create_rectangle(50, 50, 100, 100, tags = "cube")

def press_event2(event):
    print(event.keysym)
    if event.keysym == "Right":
        canvas.move("cube", 10, 0)
    elif event.keysym == "Left":
        canvas.move("cube", -10, 0)

canvas.bind_all("<Left>", press_event2)
canvas.bind_all("<Right>", press_event2)
