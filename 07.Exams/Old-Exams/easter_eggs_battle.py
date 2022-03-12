number_of_eggs_player_one = int(input())
number_of_eggs_player_two = int(input())
winner = input()
flag = False

while winner != 'End of battle':
    if winner == 'one':
        number_of_eggs_player_two -= 1
    elif winner == 'two':
        number_of_eggs_player_one -= 1
    if number_of_eggs_player_one == 0:
        print(f"Player one is out of eggs. Player two has {number_of_eggs_player_two} eggs left.")
        flag = True
        break
    elif number_of_eggs_player_two == 0:
        print(f"Player two is out of eggs. Player one has {number_of_eggs_player_one} eggs left.")
        flag = True
        break
    winner = input()

if winner == 'End of battle':
    print(
        f"Player one has {number_of_eggs_player_one} eggs left.\n"
        f"Player two has {number_of_eggs_player_two} eggs left.")
