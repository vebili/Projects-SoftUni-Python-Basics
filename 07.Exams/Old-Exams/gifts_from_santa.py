n = int(input())
m = int(input())
s = int(input())

for number in range(m, n - 1, -1):
    if number % 2 == 0 and number % 3 == 0:
        if number == s:
            break
        print(number, end=' ')
