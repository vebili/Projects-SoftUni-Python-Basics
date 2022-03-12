import sys

n = int(input())
min_number = sys.maxsize
max_number = -sys.maxsize

for x in range(n):
    num = int(input())
    if min_number > num:
        min_number = num
    if max_number < num:
        max_number = num
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
