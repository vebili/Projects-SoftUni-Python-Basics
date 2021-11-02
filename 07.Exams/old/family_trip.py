budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_costs = int(input())

if nights > 7:
    price_per_night *= 0.95
total_price = nights * price_per_night + budget * percent_costs / 100
total = abs(budget - total_price)

if budget >= total_price:
    print(f"Ivanovi will be left with {total:.2f} leva after vacation.")
else:
    print(f"{total:.2f} leva needed.")
