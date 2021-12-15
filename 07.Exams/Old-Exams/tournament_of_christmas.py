tournament_days = int(input())
wins_counter = 0
loses_counter = 0
money = 0
win_day = 0
total_money = 0
for day in range(tournament_days):
    sport = input()
    while sport != 'Finish':
        result = input()
        if result == 'win':
            wins_counter += 1
            money += 20
        else:
            loses_counter += 1
        sport = input()
    if wins_counter > loses_counter:
        win_day += 1
        money *= 1.1
    total_money += money
    money = 0
    wins_counter = 0
    loses_counter = 0
if tournament_days - win_day < win_day:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
