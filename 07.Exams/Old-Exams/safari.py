budget = float(input())
fuel = float(input())
day = str(input())
price_fuel = fuel * 2.1
guide = 100
total_price = price_fuel + guide
if day == 'Saturday':
    total_price *= 0.9
else:
    total_price *= 0.8
total = abs(budget - total_price)
if budget >= total_price:
    print(f'Safari time! Money left: {total:.2f} lv.')
else:
    print(f"Not enough money! Money needed: {total:.2f} lv.")
