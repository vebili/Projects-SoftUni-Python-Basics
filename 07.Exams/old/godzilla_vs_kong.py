budget = float(input())
statists = int(input())
price_per_wear = float(input())

if statists > 150:
    price_per_wear *= 0.9
decor = budget * 0.1
total_money_needed = statists * price_per_wear + decor
money = abs(budget - total_money_needed)
if budget < total_money_needed:
    print("Not enough money!")
    print(f"Wingard needs {money:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {money:.2f} leva left.")
