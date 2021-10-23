lenght_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percentage_full = float(input())

volume_of_aquarium = lenght_in_cm * width_in_cm * height_in_cm
volume_in_l = volume_of_aquarium * 0.001
needed_l_to_fill = volume_in_l * (1 - (percentage_full / 100))

print(needed_l_to_fill)