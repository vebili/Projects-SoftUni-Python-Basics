import math

tournaments_number = int(input())
start_points = int(input())

total_points = 0
counter = 0

for tournaments in range(tournaments_number):
    result = input()
    if result == 'W':
        counter += 1
        total_points += 2000
        start_points += 2000
    elif result == 'F':
        total_points += 1200
        start_points += 1200
    else:
        start_points += 720
        total_points += 720

percent_wins = (counter / tournaments_number) * 100

print(f"Final points: {start_points}")
print(f"Average points: {math.floor(total_points / tournaments_number)}")
print(f"{percent_wins:.2f}%")
