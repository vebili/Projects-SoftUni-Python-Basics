k = int(input())
l = int(input())
m = int(input())
n = int(input())

count = 0

for num1 in range(k, 8+1):
    for num2 in range(9, l-1, -1):
        for num3 in range(m, 8+1):
            for num4 in range(9, n-1, -1):
                if count == 6:
                    break
                if (num1 % 2 == 0 and num2 % 2 == 1) and (num3 % 2 == 0 and num4 % 2 == 1):
                    if num1 == num3 and num2 == num4:
                        print('Cannot change the same player.')

                    else:
                        print(f'{num1}{num2} - {num3}{num4}')
                        count += 1