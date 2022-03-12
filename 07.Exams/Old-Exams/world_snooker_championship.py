tournament_stage = input()
type_of_ticket = input()
tickets = int(input())
picture = input()
price = 0

if tournament_stage == 'Quarter final':
    if type_of_ticket == 'Standard':
        price = 55.50
    elif type_of_ticket == 'Premium':
        price = 105.2
    else:
        price = 118.9
elif tournament_stage == 'Semi final':
    if type_of_ticket == 'Standard':
        price = 75.88
    elif type_of_ticket == 'Premium':
        price = 125.22
    else:
        price = 300.40
else:
    if type_of_ticket == 'Standard':
        price = 110.10
    elif type_of_ticket == 'Premium':
        price = 160.66
    else:
        price = 400

price = tickets * price

if price > 4000:
    price *= 0.75
elif price > 2500:
    price *= 0.9
    if picture == 'Y':
        price += (tickets * 40)
else:
    if picture == 'Y':
        price += (tickets * 40)

print(f'{price:.2f}')
