budget = float(input())
destination = input()
season = input()
days = int(input())

price_per_day = 0
percent_discount = 1

if season == 'Winter':
    if destination == 'Dubai':
        price_per_day = 45000
        percent_discount = 0.7
    elif destination == 'Sofia':
        percent_discount = 1.25
        price_per_day = 17000
    else:
        price_per_day = 24000
else:
    if destination == 'Dubai':
        price_per_day = 40000
        percent_discount = 0.7
    elif destination == 'Sofia':
        percent_discount = 1.25
        price_per_day = 12500
    else:
        price_per_day = 20250

total_bill = days * price_per_day
discount = total_bill * percent_discount
area = abs(budget - discount)

if budget > discount:
    print(f"The budget for the movie is enough! We have {area:.2f} leva left!")
else:
    print(f"The director needs {area:.2f} leva more!")
