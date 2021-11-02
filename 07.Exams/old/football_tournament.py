team_name = input()
games = int(input())

wins = 0
draws = 0
loses = 0
points = 0

for game in range(games):
    result = input()
    if result == 'W':
        wins += 1
        points += 3
    elif result == 'D':
        draws += 1
        points += 1
    else:
        loses += 1
if games > 0:
    print(f"{team_name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {wins / games * 100:.2f}%")
else:
    print(f"{team_name} hasn't played any games during this season.")
