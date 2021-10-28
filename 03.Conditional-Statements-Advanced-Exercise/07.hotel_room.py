month = input()
sleep_days = int(input())
stuio = 0
apartment = 0
if month == 'May' or month == 'October':
    stuio = sleep_days * 50
    apartment = sleep_days * 65
    if 14 >= sleep_days > 7:
        stuio *= 0.95
    elif 14 < sleep_days:
        stuio *= 0.7
elif month == 'June' or month == 'September':
    stuio = sleep_days * 75.20
    apartment = sleep_days * 68.70
    if 14 < sleep_days:
        stuio *= 0.8
elif month == 'July' or month == 'August':
    stuio = sleep_days * 76
    apartment = sleep_days * 77
if 14 < sleep_days:
    apartment *= 0.9
print(f'Apartment: {apartment:.2f} lv.\nStudio: {stuio:.2f} lv.')