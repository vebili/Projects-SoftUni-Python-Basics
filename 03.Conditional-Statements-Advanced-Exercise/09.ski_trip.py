days_of_staying = int(input()) - 1
kind_of_room = input()
rating = input()
price = 0

if kind_of_room == 'room for one person':
    price = 18
elif kind_of_room == 'apartment':
    price = 25
    if days_of_staying > 15:
        price *= 0.50
    elif days_of_staying >= 10:
        price *= 0.65
    else:
        price *= 0.70
elif kind_of_room == 'president apartment':
    price = 35
    if days_of_staying > 15:
        price *= 0.80
    elif days_of_staying >= 10:
        price *= 0.85
    else:
        price *= 0.90

if rating == 'positive':
    price *= 1.25
elif rating == 'negative':
    price *= 0.90

total_price = price * days_of_staying

print(f'{total_price:.2f}')
