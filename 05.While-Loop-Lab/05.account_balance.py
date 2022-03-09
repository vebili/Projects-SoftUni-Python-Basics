balance = 0

while True:
    number = input()

    if number == "NoMoreMoney":
        break
    elif float(number) < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {float(number):.2f}')
    balance += float(number)

print(f'Total: {balance:.2f}')
