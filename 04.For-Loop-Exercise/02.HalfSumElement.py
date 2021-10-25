import sys

n = int(input())

max_number = -sys.maxsize
sum_numbers = 0
for x in range(n):
    number = int(input())
    sum_numbers += number
    if number > max_number:
        max_number = number
if (sum_numbers - max_number) == max_number:
    print(f'Yes\nSum = {max_number}')
else:
    print(f'No\nDiff = {abs(max_number - (sum_numbers - max_number))}')