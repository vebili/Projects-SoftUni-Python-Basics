locations = int(input())
for each_location in range (locations):
    total = 0
    gold_mined_for_the_day = float(input())
    number_of_days = int(input())
    for day in range (number_of_days):
        gold_per_day = float(input())
        total += gold_per_day
    real = total / number_of_days
    if gold_mined_for_the_day <= real:
        print(f"Good job! Average gold per day: {real:.2f}.")
    else:
        print(f"You need {gold_mined_for_the_day - real:.2f} gold.")