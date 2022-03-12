n = int(input())

count = 0
a = ''
b = ''

for cat in range(1, n + 1):
    name = input()
    family = input()
    year = int(input())
    for i in name:
        a = i
        break
    for i in family:
        b = i
        break
    print(f'{year}{ord(a)}{ord(b)}{cat}')
