slat = int(input())
start = slat - 30
fail = 0
counter = 0

while start <= slat:
    jump = int(input())
    counter += 1
    if jump > start:
        start += 5
        fail = 0
    else:
        fail += 1
    if fail == 3:
        print(f"Tihomir failed at {start}cm after {counter} jumps.")
        break
else:
    print(f"Tihomir succeeded, he jumped over {slat}cm after {counter} jumps.")
