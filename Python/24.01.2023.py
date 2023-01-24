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
canvas.mainloop()
