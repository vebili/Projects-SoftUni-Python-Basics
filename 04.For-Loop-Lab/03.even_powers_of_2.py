n = int(input())

for x in range(0, n + 1):
    if x % 2 == 0:
        print(f'{2 ** x}')
