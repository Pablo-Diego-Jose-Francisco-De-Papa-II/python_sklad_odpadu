def rock_paper_scissors() -> None:
    import random

    player_score, bot_score = 0, 0
    print("Pravidlá:\n "
          "1. kys\n "
          "2. ma rock paper scissors aj nejake pravidla?\n"
          "3. AK CHCES UKONCIT HRU SKOREJ NAPIS \"END\"")
    total_rounds = int(input("How many rounds do you want to play: "))

    for kolo in range(1, total_rounds + 1):
        player = input().lower()
        bot = random.choice(["rock", "paper", "scissors"])

        if player == "rock" and bot == "scissors" or player == "paper" and bot == "rock" or player == "scissors" and bot == "paper":
            print(kolo, "round wins Player!")
            player_score += 1

        elif bot == "rock" and player == "scissors" or bot == "paper" and player == "rock" or bot == "scissors" and player == "paper":
            print(kolo, "round wins Bot!")
            bot_score += 1

        elif player == bot:
            print(kolo, "round is a draw!")

        elif player == "end":
            break

        else:
            print("Invalid input.")


    print(f"Nahral si {player_score} bodov! \nBot nahral {bot_score} bodov!")

rock_paper_scissors()
