sale_game = int(input())
others = 0
fornite = 0
hearthstone = 0
overwatch = 0
for game in range(sale_game):
    game_name = input()
    if game_name == 'Hearthstone':
        hearthstone += 1
    elif game_name == 'Fornite':
        fornite += 1
    elif game_name == 'Overwatch':
        overwatch += 1
    else:
        others += 1
hearthstone = hearthstone / sale_game * 100
fornite = fornite / sale_game * 100
overwatch = overwatch / sale_game * 100
others = others / sale_game * 100
print(f'Hearthstone - {hearthstone:.2f}%')
print(f'Fornite - {fornite:.2f}%')
print(f'Overwatch - {overwatch:.2f}%')
print(f'Others - {others:.2f}%')
