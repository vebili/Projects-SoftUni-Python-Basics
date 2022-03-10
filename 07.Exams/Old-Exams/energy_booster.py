fruit = input()
size = input()
sets = int(input())

if size == 'small':
    sets *= 2
    if fruit == 'Watermelon':
        price = 56
    elif fruit == 'Mango':
        price = 36.66
    elif fruit == 'Pineapple':
        price = 42.10
    else:
        price = 20
else:
    sets *= 5
    if fruit == 'Watermelon':
        price = 28.7
    elif fruit == 'Mango':
        price = 19.6
    elif fruit == 'Pineapple':
        price = 24.80
    else:
        price = 15.2
# •	от 400 лв. до 1000 лв. включително има 15% отстъпка
# •	над 1000 лв. има 50% отстъпка
total_price = sets * price
if total_price > 1000:
    total_price /= 2
elif 1000 >= total_price >= 400:
    total_price *= 0.85

print(f'{total_price:.2f} lv.')
