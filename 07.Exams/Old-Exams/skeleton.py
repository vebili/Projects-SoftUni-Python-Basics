control_minutes = int(input())
control_seconds = int(input())
length_meters = float(input())
seconds_per_100_meters = int(input())

control_minutes *= 60
control_time = control_minutes + control_seconds
marin_time = (length_meters / 100) * seconds_per_100_meters - (length_meters / 120) * 2.5

if control_time < marin_time:
    print(f'No, Marin failed! He was {abs(control_time - marin_time):.3f} second slower.')
else:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
