quantity_eggs = int(input())
command = input()
flag = False
counter = 0

while command != 'Close':
    number_of_eggs_to_buy = int(input())
    if command == "Buy":
        if number_of_eggs_to_buy > quantity_eggs:
            print("Not enough eggs in store!")
            print(f"You can buy only {quantity_eggs}.")
            flag = True
            break
        else:
            quantity_eggs -= number_of_eggs_to_buy
            counter += number_of_eggs_to_buy
    elif command == 'Fill':
        quantity_eggs += number_of_eggs_to_buy
    if flag is True:
        break
    command = input()

if flag is False:
    print(f"Store is closed!")
    print(f'{counter} eggs sold.')
