budget = float(input())
product = input()
counter = 0
product_counter = 0
money = 0
while product != "Stop":
    price = float(input())
    counter += 1
    if counter == 3:
        counter = 0
        price /= 2
    budget -= price
    if budget < 0:
        print(f"You don't have enough money!\n"
              f"You need {abs(budget):.2f} leva!")
        break
    money += price
    product_counter += 1
    product = input()
else:
    print(f"You bought {product_counter} products for {money:.2f} leva.")
