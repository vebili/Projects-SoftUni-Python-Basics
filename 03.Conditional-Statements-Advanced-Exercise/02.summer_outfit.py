temperature = int(input())
time_of_day = input()
outfit = 0
shoes = 0
if 10 <= temperature <= 18:
    if time_of_day == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    if time_of_day == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    if time_of_day == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < temperature <= 24:
    if time_of_day == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    if time_of_day == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    if time_of_day == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif temperature >= 25:
    if time_of_day == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    if time_of_day == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    if time_of_day == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")