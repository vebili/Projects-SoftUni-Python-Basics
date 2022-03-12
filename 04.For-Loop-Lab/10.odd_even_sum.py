n = int(input())
even = 0
odd = 0

for x in range(1, n + 1):
    number = int(input())
    if x % 2 == 0:
        even += number
    else:
        odd += number
if even == odd:
    print(f'Yes\nSum = {odd}')
else:
    print(f'No\nDiff = {abs(odd - even)}')
