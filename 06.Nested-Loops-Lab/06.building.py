number_of_floors = int(input())
number_of_rooms = int(input())
room_numbers = ""

for f in range(number_of_floors, 0, -1):
    for r in range(number_of_rooms):
        current_number_of_rooms = f * 10 + r
        if f == number_of_floors:
            print(f"L{current_number_of_rooms} ", end="")
        elif f % 2 != 0:
            room_numbers += f"A{current_number_of_rooms} "
        else:
            room_numbers += f"O{current_number_of_rooms} "

    print(room_numbers)
    room_numbers = ""
