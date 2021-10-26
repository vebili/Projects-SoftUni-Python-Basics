change = float(input())
change = int(change * 100)
coins_counter = 0
while change > 0:
    if change - 200 >= 0:
        coins_counter += 1
        change -= 200
        continue
    elif change - 100 >= 0:
        coins_counter += 1
        change -= 100
        continue
    elif change - 50 >= 0:
        coins_counter += 1
        change -= 50
        continue
    elif change - 20 >= 0:
        coins_counter += 1
        change -= 20
        continue
    elif change - 10 >= 0:
        coins_counter += 1
        change -= 10
        continue
    elif change - 5 >= 0:
        coins_counter += 1
        change -= 5
        continue
    elif change - 2 >= 0:
        coins_counter += 1
        change -= 2
        continue
    elif change - 1 >= 0:
        coins_counter += 1
        change -= 1
        continue
    else:
        break
print(coins_counter)