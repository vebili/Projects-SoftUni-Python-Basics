days = int(input())
hour = int(input())
price = 0
day_counter = 0
total_counter = 0
for day in range(1, days + 1):
    day_counter = 0
    for hours in range(1, hour + 1):
        if day % 2 == 0 and hours % 2 != 0:
            price = 2.5
        elif day % 2 != 0 and hours % 2 == 0:
            price = 1.25
        else:
            price = 1
        day_counter += price
    total_counter += day_counter
    print(f"Day: {day} - {day_counter:.2f} leva")
print(f"Total: {total_counter:.2f} leva")
