numbers = int(input())
counter = 0
counter_1 = 0

for x in range(1111, 10000):
    for letter in str(x):
        counter_1 += 1
        if int(letter) == 0:
            counter = 0
            counter_1 = 0
            break
        if numbers % int(letter) == 0:
            counter += 1
        if counter_1 == 4 and counter != 4:
            counter_1 = 0
            counter = 0
        if counter_1 == 4 and counter == 4:
            print(x, end=' ')
            counter = 0
            counter_1 = 0
