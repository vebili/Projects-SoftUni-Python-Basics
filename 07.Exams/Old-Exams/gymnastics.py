country = input()
device = input()

hardest = 0
do_it = 0

if country == "Russia":
    if device == "ribbon":
        hardest = 9.100
        do_it = 9.400
    elif device == "hoop":
        hardest = 9.300
        do_it = 9.800
    else:
        hardest = 9.600
        do_it = 9.000
elif country == "Bulgaria":
    if device == "ribbon":
        hardest = 9.600
        do_it = 9.400
    elif device == "hoop":
        hardest = 9.550
        do_it = 9.750
    else:
        hardest = 9.500
        do_it = 9.400
else:
    if device == "ribbon":
        hardest = 9.200
        do_it = 9.500
    elif device == "hoop":
        hardest = 9.450
        do_it = 9.350
    else:
        hardest = 9.700
        do_it = 9.150

total_grade = hardest + do_it
percent_to_max = (20 - total_grade) / 20 * 100

print(f"The team of {country} get {total_grade:.3f} on {device}.")
print(f"{percent_to_max:.2f}%")
