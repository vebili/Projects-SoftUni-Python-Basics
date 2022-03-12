flower = input()
number_flower = int(input())
budget = int(input())
price = 0
roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

if flower == 'Roses':
    price = roses_price * number_flower
    if number_flower > 80:
        price *= 0.9
elif flower == 'Dahlias':
    price = dahlias_price * number_flower
    if number_flower > 90:
        price *= 0.85
elif flower == 'Tulips':
    price = tulips_price * number_flower
    if number_flower > 80:
        price *= 0.85
elif flower == 'Narcissus':
    price = narcissus_price * number_flower
    if number_flower < 120:
        price *= 1.15
elif flower == 'Gladiolus':
    price = gladiolus_price * number_flower
    if number_flower < 80:
        price *= 1.20

if budget >= price:
    area = budget - price
    print(f'Hey, you have a great garden with {number_flower} {flower} and {area:.2f} leva left.')
else:
    area = price - budget
    print(f'Not enough money, you need {area:.2f} leva more.')
