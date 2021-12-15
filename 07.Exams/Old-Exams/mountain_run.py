import math

record = float(input())
distance_meters = float(input())
time_in_seconds_per_meter = float(input())
delay = math.floor(distance_meters / 50) * 30
georgi_total_time = distance_meters * time_in_seconds_per_meter + delay
time = abs(record - georgi_total_time)
if georgi_total_time < record:
    print(f"Yes! The new record is {georgi_total_time:.2f} seconds.")
else:
    print(f"No! He was {time:.2f} seconds slower.")
