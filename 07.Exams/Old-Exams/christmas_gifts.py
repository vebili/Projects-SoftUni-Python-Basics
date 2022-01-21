command = input()

number_of_kids = 0
number_of_adults = 0

number_of_toys = 0
number_of_christmas_sweaters = 0

while command != 'Christmas':
    age = int(command)
    if age <= 16:
        number_of_kids += 1
        number_of_toys += 1
    elif age > 16:
        number_of_adults += 1
        number_of_christmas_sweaters += 1
    command = input()

total_cost_of_toys = number_of_toys * 5
total_cost_of_christmas_sweaters = number_of_christmas_sweaters * 15

print(f'Number of adults: {number_of_adults}')
print(f'Number of kids: {number_of_kids}')
print(f'Money for toys: {total_cost_of_toys}')
print(f'Money for sweaters: {total_cost_of_christmas_sweaters}')
