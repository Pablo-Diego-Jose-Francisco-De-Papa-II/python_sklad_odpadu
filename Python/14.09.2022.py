def prva_uloha(od, po, aby_sa_rovnalo, num2):
    #Zadanie: Vypiste a spocitajte vsetky trojficerne cisla, ktorych sucet cifier je 12.

    while od < po:
        num = list(str(od))
        num = [eval(i) for i in num]
        od += 1

        if sum(num) == aby_sa_rovnalo:
            num2.append(od - 1)
    return print("Počet čísel, ktorých súčet číslic je {} je {}.".format(aby_sa_rovnalo, len(num2)))

prva_uloha(int(input("Od: ")),int(input("Po: ")), int(input("Zadaj číslo, ktoré by malo byť výsledkom: ")), [])


def druha_uloha():
    # Zadanie: Hadzeme 3 kocky naraz, spocitajte kolko pokusov treba aby padli 3 rovnake cisla a pokusy vypiseme.

    import random
    import tkinter

    canvas=tkinter.Canvas(width = 400, height = 150, bg = "silver")
    canvas.pack()

    def kocky(pokus):
        kocka_A,  kocka_B, kocka_C =  1, 2, 3
        color = ["white", "purple", "red", "green", "blue", "gold"]

        while kocka_A != kocka_B or kocka_A != kocka_C:
            kocka_A = random.randint(1,6)
            kocka_B = random.randint(1,6)
            kocka_C = random.randint(1,6)

            pokus += 1

            #Kocka A
            canvas.create_rectangle(25, 25, 125, 125, width = 5, fill = color[kocka_A - 1])
            x = canvas.create_text(75, 75, text = kocka_A, font = ("Arial", "20", "bold"))

            #Kocka B
            canvas.create_rectangle(150, 25, 250, 125, width = 5, fill = color[kocka_B - 1])
            y = canvas.create_text(200, 75, text = kocka_B, font = ("Arial", "20", "bold"))

            #Kocka C
            canvas.create_rectangle(275, 25, 375, 125, width = 5, fill = color[kocka_C - 1])
            z = canvas.create_text(325, 75, text = kocka_C, font = ("Arial", "20", "bold"))

            print("Padlo -> {} - {} - {}".format(kocka_A, kocka_B, kocka_C))

            canvas.update()
            canvas.delete(x, y, z)
            canvas.after(500)

        print("Hodil si 3 rovnaké čísla na {} pokus!".format(pokus))

        #Final screen
        canvas.create_rectangle(0, 0, 444, 222, fill = color[kocka_C - 1])
        canvas.create_text(200, 50, text = "Hodil si 3 rovnaké čísla!", font = ("Arial", "20", "bold"))
        canvas.create_text(200, 75, text = "{} - {} - {}".format(kocka_A, kocka_B, kocka_C), font = ("Arial", "15", "bold"))
        canvas.create_text(200, 100, text = "Pokusy: {}".format(pokus), font = ("Arial", "15", "bold"))

    kocky(0)
    canvas.mainloop()

druha_uloha()
