a_1 = int(input())
a_2 = int(input())
n = int(input())

for symbol_1 in range(a_1, a_2):
    for symbol_2 in range(1, n):
        a = int(n / 2)
        for symbol_3 in range(1, a):
            if symbol_1 % 2 != 0 and (symbol_2 + symbol_3 + symbol_1) % 2 != 0:
                print(f'{chr(symbol_1)}-{symbol_2}{symbol_3}{symbol_1}')
