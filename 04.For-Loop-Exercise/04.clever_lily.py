ages = int(input())
price_washmashine = float(input())
toy_price = int(input())
toy_counter = 0
money_counter = 0
money = 0
for age in range(1, ages + 1):
    if age % 2 != 0:
        toy_counter += 1
    else:
        money += 10
        money_counter += money - 1
total_money = toy_counter * toy_price + money_counter
area = abs(total_money - price_washmashine)
if total_money >= price_washmashine:
    print(f"Yes! {area:.2f}")
else:
    print(f"No! {area:.2f}")