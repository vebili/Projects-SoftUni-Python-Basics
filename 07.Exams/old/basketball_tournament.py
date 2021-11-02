tournament = input()

wins = 0
loses = 0
games = 0

while tournament != 'End of tournaments':
    matches = int(input())
    for mach in range(1, matches + 1):
        desy_team = int(input())
        other_team = int(input())
        games += 1
        if desy_team > other_team:
            print(f"Game {mach} of tournament {tournament}: win with {abs(other_team - desy_team)} points.")
            wins += 1
        else:
            print(f'Game {mach} of tournament {tournament}: lost with {abs(other_team - desy_team)} points.')
            loses += 1
    tournament = input()

percent_wins = wins / games * 100
percent_loses = loses / games * 100

print(f'{percent_wins:.2f}% matches win')
print(f'{percent_loses:.2f}% matches lost')
