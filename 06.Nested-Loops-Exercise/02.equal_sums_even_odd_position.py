number_one = int(input())
number_two = int(input())
odd_sum = 0
even_sum = 0
for x in range(number_one, number_two + 1):
    for y, number in enumerate(str(x)):
        if y % 2 == 0:
            odd_sum += int(number)
        else:
            even_sum += int(number)
    if odd_sum == even_sum:
        print(x, end=' ')
    odd_sum = 0
    even_sum = 0