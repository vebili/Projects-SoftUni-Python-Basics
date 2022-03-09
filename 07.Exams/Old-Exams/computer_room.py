month = input()
number_of_gaming_hours = int(input())
number_of_people = int(input())
time_of_day = input()

price_per_person = 0

if month == 'march' or month == 'april' or month == 'may':
    if time_of_day == 'day':
        price_per_person = 10.50
    elif time_of_day == 'night':
        price_per_person = 8.40
elif month == 'june' or month == 'july' or month == 'august':
    if time_of_day == 'day':
        price_per_person = 12.60
    elif time_of_day == 'night':
        price_per_person = 10.20

if number_of_people >= 4:
    price_per_person *= 0.90

if number_of_gaming_hours >= 5:
    price_per_person *= 0.50

total_sum = number_of_people * price_per_person * number_of_gaming_hours

print(f'Price per person for one hour: {price_per_person:.2f}')
print(f'Total cost of the visit: {total_sum:.2f}')
