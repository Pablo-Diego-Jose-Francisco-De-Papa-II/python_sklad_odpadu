import tkinter as tk

root = tk.Tk()
root.title("Zadanie z 18.01.2023")
canvas = tk.Canvas(root, width = 500, height = 500, bd = 10, bg = "silver")
canvas.pack()


# Pôvodné zadanie:
# V ploche sa nachádza jeden červený štvorček velkosti 50x50. Ked’ klikneme do jeho vnútra (počíta sa aj obvod), môžeme
# ho ťahať, teda posúvať po ploche pomocou pohybov myši (inak ťahanie s kliknutím mimo štvorček nerobí nič).

def prva_uloha():
    global velkost, sur, stvorcek, grab

    velkost = 25
    sur = [250, 250, 250, 250]
    stvorcek = canvas.create_rectangle(sur[0] - velkost, sur[1] - velkost, sur[2] + velkost, sur[3] + velkost, fill = "red", width = 5)
    grab = False


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
prva_uloha()


# Rozšírenie:
# Predchádzajúci príklad upravte tak, aby fungoval aj pre 2 rôzne veľké štvorce: jeden červený veľkosti 50x50,
# druhý modrý veľkosti 100x100.


def druha_uloha():
    global velkost, red_sur, red_stvorcek, red_grab, blue_sur, blue_stvorcek, blue_grab

    velkost = 25

    red_sur = [150 - velkost, 250 - velkost, 150 + velkost, 250 + velkost]
    red_stvorcek = canvas.create_rectangle(red_sur[0], red_sur[1], red_sur[2], red_sur[3], fill="red", width=5)
    red_grab = False

    blue_sur = [350 - velkost * 2, 250 - velkost * 2, 350 + velkost * 2, 250 + velkost * 2]
    blue_stvorcek = canvas.create_rectangle(blue_sur[0], blue_sur[1], blue_sur[2], blue_sur[3], fill="blue", width=5)
    blue_grab = False

    def click(mouse):
        global red_grab, red_sur, blue_grab, blue_sur

        if mouse.x >= red_sur[-4] and mouse.y >= red_sur[-3] and mouse.x <= red_sur[-2] and mouse.y <= red_sur[-1]:
            red_grab = True
        elif mouse.x >= blue_sur[-4] and mouse.y >= blue_sur[-3] and mouse.x <= blue_sur[-2] and mouse.y <= blue_sur[-1]:
            blue_grab = True

    def motion(mouse):
        global red_grab, velkost, red_stvorcek, red_sur, blue_grab, blue_stvorcek, blue_sur

        if red_grab is True:
            canvas.delete(red_stvorcek)
            red_sur.extend([mouse.x - velkost, mouse.y - velkost, mouse.x + velkost, mouse.y + velkost])
            red_stvorcek = canvas.create_rectangle(red_sur[-4], red_sur[-3], red_sur[-2], red_sur[-1], fill="red", width=5)
            canvas.update()

        if blue_grab is True:
            canvas.delete(blue_stvorcek)
            blue_sur.extend(
                [mouse.x - velkost * 2, mouse.y - velkost * 2, mouse.x + velkost * 2, mouse.y + velkost * 2])
            blue_stvorcek = canvas.create_rectangle(blue_sur[-4], blue_sur[-3], blue_sur[-2], blue_sur[-1], fill="blue", width=5)
            canvas.update()

    def unclick(x):
        global red_grab, blue_grab

        blue_grab = red_grab = False

    canvas.bind("<Button-1>", click)
    canvas.bind("<B1-Motion>", motion)
    canvas.bind("<ButtonRelease>", unclick)
druha_uloha()
