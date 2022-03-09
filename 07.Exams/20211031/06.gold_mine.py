locations = int(input())
for each_location in range(locations):
    gold_per_day_expected = float(input())
    workdays = int(input())
    total_gold = 0
    for gold in range(workdays):
        gold_per_day = float(input())
        total_gold += gold_per_day
    average = total_gold / workdays
    if average >= gold_per_day_expected:
        print(f"Good job! Average gold per day: {average:.2f}.")
    else:
        print(f"You need {(gold_per_day_expected - average):.2f} gold.")
