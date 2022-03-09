sleeve = float(input())
front_part = float(input())
cloth = input()
tie = input()

price = 0

shirt_size = sleeve * 2 + front_part * 2
shirt_size *= 1.1
shirt_size /= 100

if cloth == 'Linen':
    price = shirt_size * 15
elif cloth == 'Cotton':
    price = shirt_size * 12
elif cloth == 'Denim':
    price = shirt_size * 20
elif cloth == 'Twill':
    price = shirt_size * 16
elif cloth == 'Flannel':
    price = shirt_size * 11

price += 10

if tie == 'Yes':
    price *= 1.2

print(f'The price of the shirt is: {price:.2f}lv.')
