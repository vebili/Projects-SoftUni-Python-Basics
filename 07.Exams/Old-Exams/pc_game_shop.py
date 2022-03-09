sale_game = int(input())

others_counter = 0
fornite_counter = 0
hearthstone_counter = 0
overwatch_counter = 0
for game in range(sale_game):
    game_name = input()
    if game_name == 'Hearthstone':
        hearthstone_counter += 1
    elif game_name == 'Fornite':
        fornite_counter += 1
    elif game_name == 'Overwatch':
        overwatch_counter += 1
    else:
        others_counter += 1

print(f'Hearthstone - {hearthstone_counter / sale_game * 100:.2f}%')
print(f'Fornite - {fornite_counter / sale_game * 100:.2f}%')
print(f'Overwatch - {overwatch_counter / sale_game * 100:.2f}%')
print(f'Others - {others_counter / sale_game * 100:.2f}%')
