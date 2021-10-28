product = input()
city = input()
count = float(input())
price = 0
if city == 'Sofia':
    if product == 'coffee':
        price = count * 0.5
    elif product == 'water':
        price = count * 0.80
    elif product == 'beer':
        price = count * 1.20
    elif product == 'sweets':
        price = count * 1.45
    elif product == 'peanuts':
        price = count * 1.60
elif city == 'Plovdiv':
    if product == 'coffee':
        price = count * 0.4
    elif product == 'water':
        price = count * 0.70
    elif product == 'beer':
        price = count * 1.15
    elif product == 'sweets':
        price = count * 1.30
    elif product == 'peanuts':
        price = count * 1.50
elif city == 'Varna':
    if product == 'coffee':
        price = count * 0.45
    elif product == 'water':
        price = count * 0.70
    elif product == 'beer':
        price = count * 1.10
    elif product == 'sweets':
        price = count * 1.35
    elif product == 'peanuts':
        price = count * 1.55
print(price)