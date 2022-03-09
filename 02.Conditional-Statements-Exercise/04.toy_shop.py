price_of_trip = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

price_puzzles = num_puzzles * 2.60
price_dolls = num_dolls * 3
price_bears = num_bears * 4.10
price_minions = num_minions * 8.20
price_trucks = num_trucks * 2

sum_prices = price_bears + price_dolls + price_trucks + price_puzzles + price_minions

num_of_toys = num_puzzles + num_trucks + num_bears + num_dolls + num_minions

if num_of_toys >= 50:
    sum_prices = sum_prices * 0.75

profit_after_rent = sum_prices * 0.90

if profit_after_rent >= price_of_trip:
    money_left = profit_after_rent - price_of_trip
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_need = price_of_trip - profit_after_rent
    print(f"Not enough money! {money_need:.2f} lv needed.")
