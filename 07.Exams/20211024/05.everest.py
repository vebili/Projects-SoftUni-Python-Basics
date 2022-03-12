command = input()
initial_meters = 5364
peak_height = 8848
days = 1

while command != "END":
    meters_to_hike = int(input())

    if command == "Yes":
        days += 1
        if days > 5:
            print("Failed!")
            print(f"{initial_meters}")
            break
        initial_meters += meters_to_hike
    else:
        initial_meters += meters_to_hike
    if initial_meters >= peak_height:
        print(f"Goal reached for {days} days!")
        break

    command = input()

if command == "END":
    if initial_meters >= peak_height:
        print(f"Goal reached for {days} days!")
    else:
        print("Failed!")
        print(f"{initial_meters}")
