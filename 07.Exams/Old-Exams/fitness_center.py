people = int(input())

back_counter = 0
chest_counter = 0
legs_counter = 0
abs_counter = 0
shake_counter = 0
bar_counter = 0

for man in range(people):
    what_to_do = input()
    if what_to_do == 'Back':
        back_counter += 1
    elif what_to_do == 'Chest':
        chest_counter += 1
    elif what_to_do == 'Legs':
        legs_counter += 1
    elif what_to_do == 'Abs':
        abs_counter += 1
    elif what_to_do == 'Protein shake':
        shake_counter += 1
    else:
        bar_counter += 1

print(f"{back_counter} - back")
print(f"{chest_counter} - chest")
print(f"{legs_counter} - legs")
print(f"{abs_counter} - abs")
print(f"{shake_counter} - protein shake")
print(f"{bar_counter} - protein bar")

training = back_counter + chest_counter + legs_counter + abs_counter
protein = shake_counter + bar_counter
works_out = training / people * 100
proteins = protein / people * 100

print(f"{works_out:.2f}% - work out")
print(f"{proteins:.2f}% - protein")
