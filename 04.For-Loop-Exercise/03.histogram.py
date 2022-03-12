n = int(input())
number_to_200 = 0
number_to_399 = 0
number_to_599 = 0
number_to_799 = 0
number_big_than_800 = 0

for x in range(n):
    number = int(input())
    if number < 200:
        number_to_200 += 1
    elif 200 <= number <= 399:
        number_to_399 += 1
    elif 400 <= number <= 599:
        number_to_599 += 1
    elif 600 <= number <= 799:
        number_to_799 += 1
    else:
        number_big_than_800 += 1
number_to_200 = number_to_200 / n * 100
number_to_399 = number_to_399 / n * 100
number_to_599 = number_to_599 / n * 100
number_to_799 = number_to_799 / n * 100
number_big_than_800 = number_big_than_800 / n * 100
print(f'{number_to_200:.2f}%')
print(f'{number_to_399:.2f}%')
print(f'{number_to_599:.2f}%')
print(f'{number_to_799:.2f}%')
print(f'{number_big_than_800:.2f}%')
