hour = int(input())
day = input()
work_day = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or \
           day == 'Thursday' or day == 'Friday' or day == 'Saturday'
work_hour = 10 <= hour <= 18
if work_day and work_hour:
    print('open')
else:
    print('closed')
