def hangman(base, pole, upper_wood, support, rope, end, head, body, left_arm, right_arm, left_leg, right_leg):
    import random

    guessing_word = ["Body", "soil", "owl", "fit", "cup", "helmet", "marsh", "smash", "career", "warm", "discipline", "lean", "suffering", "quality", "population", "harmony", "eagle", "feather", "origin", "manage", "reproduction", "scatter", "certain", "healthy", "dismiss", "introduce", "flock", "pasture", "office", "attractive", "cheap", "linen", "relieve", "habitat", "cassette", "difference", "strain", "lift", "operational", "gasp", "environmental", "soup", "colorblind", "chain", "feminine", "shoot", "tank", "rock", "abbey", "mosquito", "zoophobia", "mario je gay", "reluctance", "abundant", "strange", "expenditure", "trench", "execution", "dollar", "monster", "community", "factor", "functional", "vegetable", "abolish", "falsify", "memorandum", "forestry", "evening", "residence", "glasses", "calculation", "favour", "production", "requirement", "continuation", "partnership", "implication", "preoccupation", "personality", "headquarters", "performance", "association"]
    num = random.randint(0, len(guessing_word))
    word = list(guessing_word[num].upper())

    guess = []
    attempt = 0
    used_letters = []

    for i in word:
        if i.isalpha():
            guess += "".join("_")
        else:
            guess += "".join(i)

    while word != guess:
        print(*guess)
        letter = input("Guess the letter: ").upper()
        if len(letter) > 1:
            print("LETTER!")
        else:

            if letter in word:
                for index in [index for index, char in enumerate(word) if char == letter]:
                    guess[index] = word[index]

            else:
                if letter not in word:
                    if letter not in used_letters:
                        used_letters += letter
                        attempt += 1

            if attempt == 0:
                pass
            elif attempt == 1:
                base = "A"
            elif attempt == 2:
                pole = "|"
            elif attempt == 3:
                upper_wood = "_"
            elif attempt == 4:
                support = "/"
            elif attempt == 5:
                rope = "|"
            elif attempt == 6:
                head = "o"
            elif attempt == 7:
                body = "|"
            elif attempt == 8:
                left_arm = "/"
            elif attempt == 9:
                right_arm = "\\"
            elif attempt == 10:
                left_leg = "/"
            elif attempt == 11:
                right_leg = "\\"
                end = "END"

            print("\n+---------------+")
            print("|   {}{}{}{}{}{}{}{}{}   |".format(upper_wood, upper_wood, upper_wood, upper_wood, upper_wood, upper_wood, upper_wood, upper_wood, upper_wood))
            print("|   {}{}      {}   |".format(pole, support, rope))
            print("|   {}  {}  {}   |".format(pole, end, head))
            print("|   {}      {}{}{}  |".format(pole, left_arm, body, right_arm))
            print("|   {}      {} {}  |".format(pole, left_leg, right_leg))
            print("|   {}           |".format(base))
            print("+---------------+")

            if attempt == 11:
                print("Word you were guessing was: ", "".join([name for name in word if name.isalpha]))
                return print(*guess)

        print("\nAlready used letters: ", *used_letters, "\n")

    else:
        return print("Word you were guessing was indeed","".join([name for name in word if name.isalpha]), "\nGOOD JOB! YOU GUESSED IT RIGHT!")
hangman(" ", " ", " ", " ", " ", "   ", " ", " ", " ", " ", " ", " ")
