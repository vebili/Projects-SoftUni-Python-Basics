name = input()

student_class = 1
total_grade = 0
bad_grade = 0

while student_class <= 12 and bad_grade != 2:
    current_grade = float(input())
    if current_grade >= 4:
        total_grade += current_grade
        student_class += 1

    else:
        bad_grade += 1

if bad_grade == 2:
    print(f"{name} has been excluded at {student_class} grade")
else:
    average_grade = total_grade / 12
    print(f'{name} graduated. Average grade: {average_grade:.2f}')
