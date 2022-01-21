count_of_joinery = int(input())
type_of_joinery = input()
type_of_delivery = input()

joinery_price = 0

if type_of_joinery == '90X130':
    joinery_price = 110
    if count_of_joinery > 60:
        joinery_price *= 0.92
    elif count_of_joinery > 30:
        joinery_price *= 0.95
elif type_of_joinery == '100X150':
    joinery_price = 140
    if count_of_joinery > 80:
        joinery_price *= 0.90
    elif count_of_joinery > 40:
        joinery_price *= 0.94
elif type_of_joinery == '130X180':
    joinery_price = 190
    if count_of_joinery > 50:
        joinery_price *= 0.88
    elif count_of_joinery > 20:
        joinery_price *= 0.93
elif type_of_joinery == '200X300':
    joinery_price = 250
    if count_of_joinery > 50:
        joinery_price *= 0.86
    elif count_of_joinery > 25:
        joinery_price *= 0.91

total_price = joinery_price * count_of_joinery

if type_of_delivery == 'With delivery':
    total_price += 60

if count_of_joinery > 99:
    total_price *= 0.96

if count_of_joinery >= 10:
    print(f'{total_price:.2f} BGN')
else:
    print('Invalid order')
