pages_in_book = int(input())
pages_an_hour = int(input())
number_of_days = int(input())

hours_for_book = pages_in_book / pages_an_hour

needed_hours_reading = hours_for_book / number_of_days

print(int(needed_hours_reading))
