def morse_code(slovo):
    end_product = str()

    morse_dict = {"A": ".-",
                  "B": "-...",
                  "C": "-.-.",
                  "D": "-..",
                  "E": ".",
                  "F": "..-.",
                  "G": "--.",
                  "H": "....",
                  "I": "..",
                  "J": ".---",
                  "K": "-.-",
                  "L": ".-..",
                  "M": "--",
                  "N": "-.",
                  "O": "---",
                  "P": ".--.",
                  "Q": "--.-",
                  "R": ".-.",
                  "S": "...",
                  "T": "-",
                  "U": "..-",
                  "V": "...-",
                  "W": ".--",
                  "X": "-..-",
                  "Y": "-.--",
                  "Z": "--.."}

    if slovo[0].isalpha():
        for letter in slovo:
            if letter.isalpha():
                end_product += morse_dict[letter] + "  "
            elif letter.isspace():
                end_product += "/  "

    else:
        morse_dict = {l: m for m, l in morse_dict.items()}
        slovo_list = slovo.split()

        for morse in slovo_list:
            if morse.isalnum():
                return print("dement")
            if morse != "/":
                end_product += morse_dict[morse]
            elif morse == "/":
                end_product += " "

    return print(end_product)

morse_code(input("Zadaj slovo alebo vetu, ktorú chceš preložiť do morse code: ").upper())
