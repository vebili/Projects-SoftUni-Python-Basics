clients = int(input())

money = 0
number_products = 0
total_money = 0

for client in range(clients):
    product = input()
    while product != 'Finish':
        number_products += 1
        if product == 'basket':
            money += 1.5
        elif product == 'wreath':
            money += 3.8
        else:
            money += 7
        product = input()
    if number_products % 2 == 0:
        money *= 0.8
    total_money += money
    print(f"You purchased {number_products} items for {money:.2f} leva.")
    money = 0
    number_products = 0

print(f"Average bill per client is: {total_money / clients:.2f} leva.")
