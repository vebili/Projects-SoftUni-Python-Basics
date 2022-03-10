import math

price_of_rocket = float(input())
number_of_rockets = int(input())
number_of_sneakers = int(input())

price_of_sneakers = price_of_rocket / 6

money = (price_of_sneakers * number_of_sneakers + number_of_rockets * price_of_rocket)
equipment = (price_of_sneakers * number_of_sneakers + number_of_rockets * price_of_rocket) * 0.2
total_money = money + equipment

sponsor_must_pay = math.ceil(total_money * 7 / 8)
djokovic_to_pay = math.floor(total_money / 8)

print(f"Price to be paid by Djokovic {djokovic_to_pay}")
print(f"Price to be paid by sponsors {sponsor_must_pay}")
