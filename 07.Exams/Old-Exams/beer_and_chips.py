import math

fan_name = input()
budget = float(input())
number_of_beers = int(input())
number_of_chips_pockets = int(input())

cost_of_beers = number_of_beers * 1.20

cost_of_one_chips_pocket = cost_of_beers * 0.45

cost_of_all_chips_pockets = math.ceil(cost_of_one_chips_pocket * number_of_chips_pockets)

total_cost_of_goods = cost_of_beers + cost_of_all_chips_pockets

difference = abs(budget - total_cost_of_goods)

if budget >= total_cost_of_goods:
    print(f'{fan_name} bought a snack and has {difference:.2f} leva left.')
else:
    print(f'{fan_name} needs {difference:.2f} more leva!')
