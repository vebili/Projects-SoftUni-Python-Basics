minutes_walking_per_day = int(input())
walking_times_per_day = int(input())
take_calories_per_day = int(input())

total_burn_calories = (minutes_walking_per_day * walking_times_per_day) * 5
take_calories_per_day /= 2

if total_burn_calories >= take_calories_per_day:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burn_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burn_calories}.")
