import math

guests = int(input())
budget = int(input())

price_cake = 4
price_egg = 0.45

number_of_cakes = math.ceil(guests / 3)
total_price_cakes = number_of_cakes * price_cake
number_of_eggs = guests * 2
total_price_eggs = price_egg * number_of_eggs

total_bills = total_price_eggs + total_price_cakes
left_money = abs(budget - total_bills)
if budget >= total_bills:
    print(f"Lyubo bought {number_of_cakes} Easter bread and {number_of_eggs} eggs.")
    print(f'He has {left_money:.2f} lv. left.')
else:
    print(f"Lyubo doesn't have enough money.\nHe needs {left_money:.2f} lv. more.")
