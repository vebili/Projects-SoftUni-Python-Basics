needed_money = float(input())
balance = float(input())
days = 0
spending_day = 0

while True:
    command = input()
    money_command = float(input())
    if command == "spend":
        days += 1
        spending_day += 1
        if money_command <= balance:
            balance -= money_command
        elif money_command > balance:
            balance = 0
        if spending_day == 5:
            print(f"You can't save the money.\n{days}")
            break
    elif command == "save":
        spending_day -= spending_day
        days += 1
        balance += money_command
    if balance >= needed_money:
        print(f"You saved the money for {days} days.")
        break
