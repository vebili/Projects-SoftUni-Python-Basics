first_match = input()
second_match = input()
third_match = input()

a = 0
b = 0
wins = 0
draw = 0
lose = 0

for x, y in enumerate(first_match):
    if x == 0:
        a = y
    if x == 2:
        b = y
        a = int(a)
        b = int(b)
        if a > b:
            wins += 1
        elif a == b:
            draw += 1
        elif a < b:
            lose += 1
for x, y in enumerate(second_match):
    if x == 0:
        a = y
    if x == 2:
        b = y
        a = int(a)
        b = int(b)
        if a > b:
            wins += 1
        elif a == b:
            draw += 1
        elif a < b:
            lose += 1
for x, y in enumerate(third_match):
    if x == 0:
        a = y
    if x == 2:
        b = y
        a = int(a)
        b = int(b)
        if a > b:
            wins += 1
        elif a == b:
            draw += 1
        elif a < b:
            lose += 1
print(f"Team won {wins} games.")
print(f"Team lost {lose} games.")
print(f"Drawn games: {draw}")
