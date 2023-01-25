import tkinter as tk

root = tk.Tk()
root.title("Halooooooo. Kto tam?")
canvas = tk.Canvas(root, width=500, height=500, bg="silver")
canvas.pack()

position = [250, 250, 250, 250]
move = 10
canvas.create_line(position, tags="lajna", width=3)

def prva_uloha(event):
    global position, move
    if event.keysym == "Right":
        position.extend([position[-2] + move, position[-1]])
    elif event.keysym == "Left":
        position.extend([position[-2] - move, position[-1]])
    elif event.keysym == "Up":
        position.extend([position[-2], position[-1] - move])
    elif event.keysym == "Down":
        position.extend([position[-2], position[-1] + move])

    canvas.coords("lajna", position)
canvas.bind_all("<Key>", prva_uloha)


obr, move = tk.PhotoImage(file = "notmiguel.png"), 10
canvas.create_image(250, 250, image = obr, tags = "gato")

def kiten(key):
    name = key.keysym

    match name:
        case "Right": canvas.move("gato", move, 0)
        case "Left":  canvas.move("gato", -move, 0)
        case "Up":    canvas.move("gato", 0, -move)
        case "Down":  canvas.move("gato", 0, move)

canvas.bind_all("<Key>", kiten)
