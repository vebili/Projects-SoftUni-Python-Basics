from math import floor

record = float(input())
distance_in_m = float(input())
sec_for_m = float(input())

time_for_swimming = distance_in_m * sec_for_m

resistance = distance_in_m / 15
resistance_floor = floor(resistance) * 12.5

total_time = time_for_swimming + resistance_floor

if record <= total_time:
    result = total_time - record
    print(f'No, he failed! He was {result:.2f} seconds slower.')
else:
    result = total_time
    print(f'Yes, he succeeded! The new world record is {result:.2f} seconds.')
