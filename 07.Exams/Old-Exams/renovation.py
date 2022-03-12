import math

wall_high = int(input())
wall_weight = int(input())
percent_for_windows = int(input())
paint = input()
total_paint = 0
total_wall = math.ceil((wall_weight * wall_high * 4) - (wall_weight * wall_high * 4) * percent_for_windows / 100)
while paint != 'Tired!':
    paint = int(paint)
    total_paint += paint

    if total_wall < total_paint:
        print(f"All walls are painted and you have {total_paint - total_wall} l paint left!")
        break
    elif total_wall == total_paint:
        print(f"All walls are painted! Great job, Pesho!")
        break
    paint = input()
total_wall -= total_paint
if paint == 'Tired!':
    print(f"{total_wall} quadratic m left.")
