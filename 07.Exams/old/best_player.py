command = input()

best_player = ''
best_score = 0

while command != 'END':
    player_name = command
    count_of_goals = int(input())
    if count_of_goals > best_score:
        best_score = count_of_goals
        best_player = player_name
    if count_of_goals >= 10:
        break
    command = input()

print(f'{best_player} is the best player!')

if best_score >= 3:
    print(f'He has scored {best_score} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_score} goals.')
