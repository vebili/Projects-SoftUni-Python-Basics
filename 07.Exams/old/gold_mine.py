number_of_locations = int(input())

for locations in range(1, number_of_locations + 1):
    expected_gold_per_day = float(input())
    number_days_of_digging = int(input())
    sum_gold = 0
    for days_of_digging in range(1, number_days_of_digging + 1):
        gold_per_day = float(input())
        sum_gold += gold_per_day
    average_gold_per_day = sum_gold / number_days_of_digging
    if average_gold_per_day >= expected_gold_per_day:
        print(f'Good job! Average gold per day: {average_gold_per_day:.2f}.')
        continue
    else:
        difference = expected_gold_per_day - average_gold_per_day
        print(f'You need {difference:.2f} gold.')
        continue
