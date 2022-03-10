strawberry_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberry_kg = float(input())

raspberries_price = strawberry_price / 2
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

needed_money = (strawberry_kg * strawberry_price) + (bananas_kg * bananas_price) + \
               (oranges_kg * oranges_price) + (raspberries_kg * raspberries_price)

print(f'{needed_money:.2f}')
