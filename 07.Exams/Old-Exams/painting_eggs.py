size_eggs = input()
color_eggs = input()
number_of_parts = int(input())
price_per_egg = 0

if size_eggs == 'Large':
    if color_eggs == 'Red':
        price_per_egg = 16
    elif color_eggs == 'Green':
        price_per_egg = 12
    elif color_eggs == 'Yellow':
        price_per_egg = 9
elif size_eggs == 'Medium':
    if color_eggs == 'Red':
        price_per_egg = 13
    elif color_eggs == 'Green':
        price_per_egg = 9
    elif color_eggs == 'Yellow':
        price_per_egg = 7
elif size_eggs == 'Small':
    if color_eggs == 'Red':
        price_per_egg = 9
    elif color_eggs == 'Green':
        price_per_egg = 8
    elif color_eggs == 'Yellow':
        price_per_egg = 5

total_price = number_of_parts * price_per_egg
total_price *= 0.65

print(f'{total_price:.2f} leva.')
