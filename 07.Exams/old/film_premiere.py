movie_name = input()
pocket_for_movie = input()
tickets = int(input())

price_per_ticket = 0
discount = 0

if movie_name == 'John Wick':
    if pocket_for_movie == 'Drink':
        price_per_ticket = 12
    elif pocket_for_movie == "Popcorn":
        price_per_ticket = 15
    else:
        price_per_ticket = 19
elif movie_name == "Star Wars":
    if tickets >= 4:
        discount = 0.30
    if pocket_for_movie == 'Drink':
        price_per_ticket = 18
    elif pocket_for_movie == "Popcorn":
        price_per_ticket = 25
    else:
        price_per_ticket = 30
else:
    if tickets == 2:
        discount = 0.15
    if pocket_for_movie == 'Drink':
        price_per_ticket = 9
    elif pocket_for_movie == "Popcorn":
        price_per_ticket = 11
    else:
        price_per_ticket = 14

total_bill = (tickets * price_per_ticket) - (tickets * price_per_ticket) * discount

print(f"Your bill is {total_bill:.2f} leva.")
