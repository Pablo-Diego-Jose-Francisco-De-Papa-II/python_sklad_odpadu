import random

def hangman():
    guessing_word = ["Body", "soil", "owl", "fit", "cup", "helmet", "marsh", "smash", "career", "warm", "discipline", "lean", "suffering", "quality", "population", "harmony", "eagle", "feather", "origin", "manage", "reproduction", "scatter", "certain", "healthy", "dismiss", "introduce", "flock", "pasture", "office", "attractive", "cheap", "linen", "relieve", "habitat", "cassette", "difference", "strain", "lift", "operational", "gasp", "environmental", "soup", "colorblind", "chain", "feminine", "shoot", "tank", "rock", "abbey", "mosquito"]
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
                    else:
                        print("ALREADY USED")

            if attempt == 0:
                print("+---------------+")
                print("|               |")
                print("|               |")
                print("|               |")
                print("|               |")
                print("|               |")
                print("|               |")
                print("+---------------+")

            elif attempt == 1:
                print("+---------------+")
                print("|               |")
                print("|               |")
                print("|               |")
                print("|               |")
                print("|               |")
                print("|   A           |")
                print("+---------------+")

            elif attempt == 2:
                print("+---------------+")
                print("|               |")
                print("|   |           |")
                print("|   |           |")
                print("|   |           |")
                print("|   |           |")
                print("|   A           |")
                print("+---------------+")

            elif attempt == 3:
                print("+---------------+")
                print("|   _________   |")
                print("|   |           |")
                print("|   |           |")
                print("|   |           |")
                print("|   |           |")
                print("|   A           |")
                print("+---------------+")

            elif attempt == 4:
                print("+---------------+")
                print("|   _________   |")
                print("|   |/          |")
                print("|   |           |")
                print("|   |           |")
                print("|   |           |")
                print("|   A           |")
                print("+---------------+")

            elif attempt == 5:
                print("+---------------+")
                print("|   _________   |")
                print("|   |/      |   |")
                print("|   |           |")
                print("|   |           |")
                print("|   |           |")
                print("|   A           |")
                print("+---------------+")

            elif attempt == 6:
                print("+---------------+")
                print("|   _________   |")
                print("|   |/      |   |")
                print("|   |       o   |")
                print("|   |           |")
                print("|   |           |")
                print("|   A           |")
                print("+---------------+")

            elif attempt == 7:
                print("+---------------+")
                print("|   _________   |")
                print("|   |/      |   |")
                print("|   |       o   |")
                print("|   |       |   |")
                print("|   |           |")
                print("|   A           |")
                print("+---------------+")

            elif attempt == 8:
                print("+---------------+")
                print("|   _________   |")
                print("|   |/      |   |")
                print("|   |       o   |")
                print("|   |      /|   |")
                print("|   |           |")
                print("|   A           |")
                print("+---------------+")

            elif attempt == 9:
                print("+---------------+")
                print("|   _________   |")
                print("|   |/      |   |")
                print("|   |       o   |")
                print("|   |      /|\  |")
                print("|   |           |")
                print("|   A           |")
                print("+---------------+")

            elif attempt == 10:
                print("+---------------+")
                print("|   _________   |")
                print("|   |/      |   |")
                print("|   |       o   |")
                print("|   |      /|\  |")
                print("|   |      /    |")
                print("|   A           |")
                print("+---------------+")

            elif attempt == 11:
                print("+---------------+")
                print("|   _________   |")
                print("|   |/      |   |")
                print("|   |  END  o   |")
                print("|   |      /|\  |")
                print("|   |      / \  |")
                print("|   A           |")
                print("+---------------+")
                return print("Word you were guessing was: ", "".join([name for name in word if name.isalpha]))


        print("Already used letters: ", *used_letters)
        print(*guess,"\n\n")

    else:
        return print("GOOD JOB! YOU GUESSED IT RIGHT!")
hangman()
