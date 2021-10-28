hour = int(input())
day = input()
if_work_day = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or \
              day == 'Thursday' or day == 'Friday' or day == 'Saturday'
if_work_hour = 10 <= hour <= 18
if if_work_day and if_work_hour:
    print('open')
else:
    print('closed')