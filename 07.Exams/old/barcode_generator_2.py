start_number = input()
end_number = input()
e_1 = 0
e_2 = 0
e_3 = 0
e_4 = 0
s_1 = 0
s_2 = 0
s_3 = 0
s_4 = 0
for x, start in enumerate(start_number):
    if x == 0:
        s_1 = int(start)
    elif x == 1:
        s_2 = int(start)
    elif x == 2:
        s_3 = int(start)
    elif x == 3:
        s_4 = int(start)
for y, end in enumerate(end_number):
    if y == 0:
        e_1 = int(end)
    elif y == 1:
        e_2 = int(end)
    elif y == 2:
        e_3 = int(end)
    elif y == 3:
        e_4 = int(end)
for a in range(s_1, e_1 + 1):
    for b in range(s_2, e_2 + 1):
        for c in range(s_3, e_3 + 1):
            for d in range(s_4, e_4 + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f'{a}{b}{c}{d}', end=' ')
