number = int(input())
counter = 0
for x in range(1, number + 1):
    if counter > number:
        break
    for y in range(1, x + 1):
        counter += 1
        if counter > number:
            break
        else:
            print(counter, end=' ')
    print()
