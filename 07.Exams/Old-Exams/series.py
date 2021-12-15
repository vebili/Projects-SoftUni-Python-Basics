budget = float(input())
serials = int(input())
money = 0

for x in range(serials):
    movie_name = input()
    price = float(input())
    if movie_name == 'Thrones':
        price *= 0.5
    elif movie_name == 'Lucifer':
        price *= 0.6
    elif movie_name == 'Protector':
        price *= 0.7
    elif movie_name == 'TotalDrama':
        price *= 0.8
    elif movie_name == 'Area':
        price *= 0.9
    money += price

if budget >= money:
    print(f"You bought all the series and left with {budget - money:.2f} lv.")
else:
    print(f"You need {money - budget:.2f} lv. more to buy the series!")
