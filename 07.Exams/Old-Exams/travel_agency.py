city = input()
packet = input()
vip = input()
days = int(input())
price = 0
flag = True
if city == 'Bansko' or city == 'Borovets':
    if packet == 'noEquipment':
        price = 80
        if vip == 'yes':
            price *= 0.95
    else:
        price = 100
        if vip == 'yes':
            price *= 0.90
else:
    if packet == 'noBreakfast':
        price = 100
        if vip == 'yes':
            price *= 0.93
    else:
        price = 130
        if vip == 'yes':
            price *= 0.88
if days > 7:
    days -= 1
total = days * price
if city != "Bansko" and city != "Borovets" and city != "Varna" and city != "Burgas" \
        or packet != 'noEquipment' and packet != "withEquipment" and packet != "noBreakfast" \
        and packet != "withBreakfast":
    flag = False
    print("Invalid input!")
if days < 1:
    flag = False
    print("Days must be positive number!")
if flag is True:
    print(f"The price is {total:.2f}lv! Have a nice time!")
