def prva_uloha(cislo, spocitane_cisla):
    #Zadanie: Z n-čísla vypíšeš koľko krát sa daná číslica v danom čísle nachádza.

    for num in range(10):
        spocitane_cisla += [num, cislo.count(str(num))],
    return print(spocitane_cisla)

prva_uloha(list(input("Zadaj číslo v ktorom sa ti spočítajú koľko krát sa v tom čísle nachádzajú: ")), ())


def druha_uloha(cislo):
    #Zadanie: Usporiadaj číslice v n-čísle podľa ich prvého výskytu. [1, 2, 1, 3, 2] -> [1, 1, 2, 2, 3]

    new_list, all_nums, count_num = [], [], []

    for item in cislo:
        if item not in all_nums:
            all_nums.append(item)
            count_num.append(cislo.count(str(item)))

    for i in range(len(all_nums)):
        new_list.append(all_nums[i] * count_num[i])
        answer = "".join(new_list)

    return print("Zadané číslo:   ", ", ".join(cislo), "\n" "Upravené číslo: ", ", ".join(answer))

druha_uloha(list(input("Zadaj číslo: ")))
