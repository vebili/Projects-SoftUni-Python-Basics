number_of_bake = int(input())

grade_counter = 0
max_grade_save = 0
name_of_best_baker = 0
total_grade = 0
name_counter = 0

for bake in range(number_of_bake):
    name_of_baker = input()
    grade_to_bake = input()
    while grade_to_bake != 'Stop':
        max_grade_save += int(grade_to_bake)
        grade_to_bake = input()
    print(f"{name_of_baker} has {max_grade_save} points.")
    if total_grade < max_grade_save:
        print(f"{name_of_baker} is the new number 1!")
        total_grade = max_grade_save
        name_counter = name_of_baker
    max_grade_save = 0

print(f"{name_counter} won competition with {total_grade} points!")
