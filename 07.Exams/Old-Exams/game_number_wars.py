name_first_player = input()
name_second_player = input()
card_first_player = input()
card_second_player = input()

counter_first = 0
counter_second = 0
flag = False

while card_first_player != "End of game" or card_second_player != "End of game":
    card_first_player = int(card_first_player)
    card_second_player = int(card_second_player)
    if card_first_player == card_second_player:
        card_first_player = input()
        card_second_player = input()
        card_first_player = int(card_first_player)
        card_second_player = int(card_second_player)
        if card_first_player > card_second_player:
            print("Number wars!")
            print(f"{name_first_player} is winner with {counter_first} points")
            flag = True
            break
        else:
            print("Number wars!")
            print(f"{name_second_player} is winner with {counter_second} points")
            flag = True
            break
    if card_first_player > card_second_player:
        counter_first += card_first_player - card_second_player
    else:
        counter_second += card_second_player - card_first_player
    card_first_player = input()
    if card_first_player == 'End of game':
        break
    card_second_player = input()
    if card_second_player == 'End of game':
        break

if flag is False:
    print(f"{name_first_player} has {counter_first} points")
    print(f"{name_second_player} has {counter_second} points")
