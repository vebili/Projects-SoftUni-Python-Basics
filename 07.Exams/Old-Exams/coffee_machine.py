drink = input()
sugar = input()
number_drinks = int(input())
price = 0
if drink == 'Espresso':
    if sugar == 'Without':
        price = 0.9
        price *= 0.65
    elif sugar == 'Normal':
        price = 1.0
    else:
        price = 1.20
    if number_drinks >= 5:
        price *= 0.75
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = 1.0
        price *= 0.65
    elif sugar == 'Normal':
        price = 1.2
    else:
        price = 1.60
else:
    if sugar == 'Without':
        price = 0.5
        price *= 0.65
    elif sugar == 'Normal':
        price = 0.6
    else:
        price = 0.7

total_price = number_drinks * price
if total_price > 15:
    total_price *= 0.8
print(f"You bought {number_drinks} cups of {drink} for {total_price:.2f} lv.")
