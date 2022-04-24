start_hour = int(input())
check_hour = int(input())
check_minutes = int(input())
week_day = input()

bonus = 0

time = (check_hour - start_hour) * 60
time = time + check_minutes

if time < 0:
    bonus = 1.5
elif 0 <= time <= 30:
    bonus = 1
elif time > 30:
    bonus = 0.5

if week_day == 'Monday' or week_day == 'Wednesday' or week_day == 'Friday':
    bonus += 0.6
elif week_day == 'Tuesday' or week_day == 'Thursday' or week_day == 'Saturday':
    bonus += 0.8
elif week_day == 'Sunday':
    bonus += 2

print(f'{bonus:.2f}')
