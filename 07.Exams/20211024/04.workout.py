from math import ceil

N_days = int(input())
M_kilometers = float(input())

sum_kilometers = + M_kilometers
sum_all_kilometers = sum_kilometers

for N_days in range(1, N_days + 1):
    Percent = int(input())
    sum_kilometers += 1.00 * Percent / 100 * sum_kilometers
    sum_all_kilometers += sum_kilometers

if sum_all_kilometers >= 1000:
    print(f"You've done a great job running {ceil(sum_all_kilometers - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000 - sum_all_kilometers)} more kilometers")
