contract = input()
type_contract = input()
mobile_internet = input()
months = int(input())
price_per_month = 0
price_per_net = 0
if contract == 'one':
    if type_contract == 'Small':
        price_per_month = 9.98
    elif type_contract == 'Middle':
        price_per_month = 18.99
    elif type_contract == 'Large':
        price_per_month = 25.98
    else:
        price_per_month = 35.99
else:
    if type_contract == 'Small':
        price_per_month = 8.58
    elif type_contract == 'Middle':
        price_per_month = 17.09
    elif type_contract == 'Large':
        price_per_month = 23.59
    else:
        price_per_month = 31.79
if mobile_internet == 'yes':
    if price_per_month <= 10:
        price_per_net = 5.5
    elif price_per_month <= 30:
        price_per_net = 4.35
    else:
        price_per_net = 3.85
tax = price_per_month + price_per_net
total_price = tax * months
if contract == 'two':
    total_price = total_price - ((total_price * 3.75) / 100)
print(f"{total_price:.2f} lv.")
