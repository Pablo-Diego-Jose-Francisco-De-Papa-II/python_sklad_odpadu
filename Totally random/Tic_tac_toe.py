def tic_tac_toe(xoxo, used_indexes, player):
    game_round = 0
    
    while len(used_indexes) < 10:
        print(*["\n{} | {} | {}".format(xoxo[0], xoxo[1], xoxo[2])])
        print(*["--|---|--"])
        print(*["{} | {} | {}".format(xoxo[3], xoxo[4], xoxo[5])])
        print(*["--|---|--"])
        print(*["{} | {} | {}\n".format(xoxo[6], xoxo[7], xoxo[8])])

        if xoxo[0] == xoxo[1] == xoxo[2] or xoxo[3] == xoxo[4] == xoxo[5] or xoxo[6] == xoxo[7] == xoxo[8] or xoxo[0] == xoxo[4] == xoxo[8] or xoxo[2] == xoxo[4] == xoxo[6] or xoxo[0] == xoxo[3] == xoxo[6] or xoxo[1] == xoxo[4] == xoxo[7] or xoxo[2] == xoxo[5] == xoxo[8]:
            return print(f'Player "{player[game_round % 2]}" wins!')
        elif game_round == 9:
            return print("Nobody wins! :(")

        if game_round % 2 == 0:
            player_1 = int(input("Player x: "))

            if player_1 not in used_indexes:
                xoxo[player_1 - 1] = "x"
                used_indexes.append(player_1)
                game_round += 1
            else:
                pass
              
        else:
            player_2 = int(input("Player o: "))

            if player_2 not in used_indexes:
                xoxo[player_2 - 1] = "o"
                used_indexes.append(player_2)
                game_round += 1
            else:
                pass

tic_tac_toe([1, 2, 3, 4, 5, 6, 7, 8, 9], [], ["o", "x"])
