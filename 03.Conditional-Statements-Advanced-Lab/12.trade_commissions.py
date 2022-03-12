city = input()
sold = float(input())
price = 0

if sold < 0 or not city == 'Sofia' and not city == 'Varna' and not city == 'Plovdiv':
    print('error')
elif city == 'Sofia':
    if 0 <= sold <= 500:
        price = sold * 0.05
    elif 500 <= sold <= 1000:
        price = sold * 0.07
    elif 1000 <= sold <= 10000:
        price = sold * 0.08
    elif sold > 10000:
        price = sold * 0.12
    print(f'{price:.2f}')
elif city == 'Varna':
    if 0 <= sold <= 500:
        price = sold * 0.045
    elif 500 <= sold <= 1000:
        price = sold * 0.075
    elif 1000 <= sold <= 10000:
        price = sold * 0.10
    elif sold > 10000:
        price = sold * 0.13
    print(f'{price:.2f}')
elif city == 'Plovdiv':
    if 0 <= sold <= 500:
        price = sold * 0.055
    elif 500 <= sold <= 1000:
        price = sold * 0.08
    elif 1000 <= sold <= 10000:
        price = sold * 0.12
    elif sold > 10000:
        price = sold * 0.145
    print(f'{price:.2f}')
