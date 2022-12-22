#Zadanie: Kde klikneš na plátne sa vytvorí kruh. Ked kliknes znova vytvori sa ti dalsi kruh a spojí sa s čiarov s prvým kruhom and so on...

import tkinter
import random

canvas = tkinter.Canvas(bg="silver")
canvas.pack()


posiiton = []
def prva_uloha(mouse):
    color = random.randint(100000, 999999)
    
    canvas.create_oval(mouse.x - 5, mouse.y - 5, mouse.x + 5, mouse.y + 5, fill = "#" + str(color))
    
    posiiton.append(mouse.x)
    posiiton.append(mouse.y)
    
    if len(posiiton) > 2:
        canvas.create_line(mouse.x, mouse.y, posiiton[-4], posiiton[-3])

canvas.bind('<Button-1>', prva_uloha)
canvas.mainloop()
