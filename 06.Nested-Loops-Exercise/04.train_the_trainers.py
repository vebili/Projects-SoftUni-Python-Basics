jury = int(input())
presentation = input()
presentation_counter = 0
average = 0
total = 0
counter = 0
while presentation != 'Finish':
    counter += 1
    for grades in range(jury):
        grade = float(input())
        presentation_counter += grade
    average += presentation_counter / jury
    total += average
    print(f'{presentation} - {average:.2f}.')
    average = 0
    presentation_counter = 0
    presentation = input()
print(f"Student's final assessment is {total / counter:.2f}.")
