joinery = int(input())
type_joinery = input()
delivery = input()
price = 0
total_price = 0

if joinery >= 10:
    if type_joinery == "90X130":
        price = 110
        if 60 >= joinery > 30:
            price *= 0.95
        elif joinery > 60:
            price *= 0.92
    elif type_joinery == "100X150":
        price = 140
        if 80 >= joinery > 40:
            price *= 0.94
        elif joinery > 80:
            price *= 0.90
    elif type_joinery == "130X180":
        price = 190
        if 20 < joinery <= 50:
            price *= 0.93
        elif joinery > 50:
            price *= 0.88
    else:
        price = 250
        if 25 < joinery <= 50:
            price *= 0.91
        elif joinery > 50:
            price *= 0.86
    total_price = joinery * price
    if delivery == "With delivery":
        total_price += 60
    if joinery >= 100:
        total_price *= 0.96
    print(f'{total_price:.2f} BGN')
else:
    print("Invalid order")
