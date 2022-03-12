start_number_points = int(input())

bonus_points = 0

if start_number_points <= 100:
    bonus_points = 5
elif start_number_points > 1000:
    bonus_points = start_number_points * 0.1
else:
    bonus_points = start_number_points * 0.2

if start_number_points % 2 == 0:
    bonus_points = bonus_points + 1
elif start_number_points % 10 == 5:
    bonus_points = bonus_points + 2

print(bonus_points)
print(start_number_points + bonus_points)
