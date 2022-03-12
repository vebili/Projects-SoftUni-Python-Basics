hours = int(input())
minutes = int(input())

time_in_minutes = hours * 60 + minutes
time_after_in_minutes = time_in_minutes + 15

final_hour = time_after_in_minutes // 60
final_minutes = time_after_in_minutes % 60

if final_hour == 24:
    final_hour = 0

if final_minutes < 10:
    print(f"{final_hour}:0{final_minutes}")
else:
    print(f"{final_hour}:{final_minutes}")
