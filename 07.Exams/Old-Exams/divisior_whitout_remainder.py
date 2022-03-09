numbers = int(input())
p_1 = 0
p_2 = 0
p_3 = 0
for number in range(numbers):
    p = int(input())
    if p % 2 == 0:
        p_1 += 1
    if p % 3 == 0:
        p_2 += 1
    if p % 4 == 0:
        p_3 += 1
p_1 = p_1 / numbers * 100
p_2 = p_2 / numbers * 100
p_3 = p_3 / numbers * 100
print(f'{p_1:.2f}%')
print(f'{p_2:.2f}%')
print(f'{p_3:.2f}%')
