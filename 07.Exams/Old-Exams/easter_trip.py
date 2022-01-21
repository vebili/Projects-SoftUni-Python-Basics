destination = input()
dates = input()
days = int(input())
price_of_day = 0

if destination == 'France':
    if dates == '21-23':
        price_of_day = 30
    elif dates == '24-27':
        price_of_day = 35
    elif dates == '28-31':
        price_of_day = 40
elif destination == 'Italy':
    if dates == '21-23':
        price_of_day = 28
    elif dates == '24-27':
        price_of_day = 32
    elif dates == '28-31':
        price_of_day = 39
elif destination == 'Germany':
    if dates == '21-23':
        price_of_day = 32
    elif dates == '24-27':
        price_of_day = 37
    elif dates == '28-31':
        price_of_day = 43

needed_money = days * price_of_day

print(f"Easter trip to {destination} : {needed_money:.2f} leva.")
