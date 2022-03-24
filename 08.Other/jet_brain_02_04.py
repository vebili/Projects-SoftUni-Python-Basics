number = int(input("Въведете число: "))
k = 1
while k <= number // 2:
    if number % k == 0:
        print("Дели се на", k)
    k = k + 1
print("Дели се на", number)
