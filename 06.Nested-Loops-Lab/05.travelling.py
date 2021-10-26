current_sum = 0

while True:
    destination = input()
    if destination == "End":
        break
    needed_money = float(input())

    while current_sum < needed_money:
        money = float(input())
        current_sum += money

    print(f"Going to {destination}!")
    current_sum = 0