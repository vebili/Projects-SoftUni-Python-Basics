hour_test = int(input())
minutes_test = int(input())
hour_income = int(input())
minutes_income = int(input())
test = hour_test * 60 + minutes_test
income = hour_income * 60 + minutes_income
if test == income:
    print("On time")
elif 0 < test - income <= 30:
    print("On time")
elif test - income > 30:
    print("Early")
else:
    print('Late')
if 0 < test - income < 60:
    print(f"{abs(income - test)} minutes before the start")
elif test - income >= 60:
    print(f"{abs(income - test) // 60}:{abs(income - test) % 60:02d} hours before the start")
elif 0 > test - income > -60:
    print(f'{abs(income - test)} minutes after the start')
elif test - income <= -60:
    print(f"{abs(income - test) // 60}:{abs(income - test) % 60:02d} hours after the start")