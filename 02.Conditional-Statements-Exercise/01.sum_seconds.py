from math import floor

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time / 60
second = total_time % 60

minutes = floor(minutes)

if second < 10:
    print(f'{minutes}:0{second}')
else:
    print(f'{minutes}:{second}')
