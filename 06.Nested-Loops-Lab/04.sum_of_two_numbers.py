starting_number = int(input())
final_number = int(input())
magic_number = int(input())
combinations = 0
is_found = False
i = 0
j = 0

for i in range(starting_number, final_number + 1):
    for j in range(starting_number, final_number + 1):
        combinations += 1
        if i + j == magic_number:
            print(f"Combination N:{combinations} ({i} + {j} = {magic_number})")
            is_found = True
            break
    if is_found:
        break

if i + j != magic_number:
    print(f"{combinations} combinations - neither equals {magic_number}")
