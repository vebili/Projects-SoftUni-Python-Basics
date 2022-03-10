player_name = input()

points = 0
best_player = 0
max_points = 0

while player_name != 'Stop':
    for num, letter in enumerate(player_name):
        number = int(input())
        if ord(letter) == number:
            points += 10
        else:
            points += 2
    if points >= max_points:
        max_points = points
        best_player = player_name
    points = 0
    player_name = input()
print(f"The winner is {best_player} with {max_points} points!")
