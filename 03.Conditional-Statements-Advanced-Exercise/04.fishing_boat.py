budget_group = int(input())
season = input()
fishers = int(input())
price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if fishers <= 6:
    price *= 0.9
elif 7 < fishers <= 11:
    price *= 0.85
elif 12 < fishers:
    price *= 0.75

if fishers % 2 == 0 and not season == 'Autumn':
    price *= 0.95

if budget_group >= price:
    area = budget_group - price
    print(f'Yes! You have {area:.2f} leva left.')
else:
    area = price - budget_group
    print(f"Not enough money! You need {area:.2f} leva.")
