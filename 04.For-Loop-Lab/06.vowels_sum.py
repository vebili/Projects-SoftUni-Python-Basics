text = input()
sums = 0

for x in text:
    if x == 'a':
        sums += 1
    elif x == 'e':
        sums += 2
    elif x == 'i':
        sums += 3
    elif x == 'o':
        sums += 4
    elif x == 'u':
        sums += 5
print(sums)
