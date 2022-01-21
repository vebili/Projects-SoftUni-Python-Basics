player_name = input()
field = input()

start_points = 301
success = 0
fail = 0

while field != 'Retire':
    points = int(input())
    if field == 'Double':
        points *= 2
    elif field == 'Triple':
        points *= 3
    if points <= start_points:
        success += 1
        start_points -= points
    else:
        fail += 1
    if start_points == 0:
        print(f"{player_name} won the leg with {success} shots.")
        break
    field = input()
else:
    print(f"{player_name} retired after {fail} unsuccessful shots.")
