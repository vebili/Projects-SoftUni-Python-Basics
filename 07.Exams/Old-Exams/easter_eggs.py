number_of_eggs = int(input())

counter_red = 0
counter_orange = 0
counter_blue = 0
counter_green = 0
max_eggs = 0
color = 0

for egg in range(1, number_of_eggs + 1):
    color_to_paint = input()
    if color_to_paint == 'red':
        counter_red += 1
    elif color_to_paint == 'orange':
        counter_orange += 1
    elif color_to_paint == 'blue':
        counter_blue += 1
    elif color_to_paint == 'green':
        counter_green += 1

if counter_red >= counter_orange and counter_red >= counter_blue and counter_red >= counter_green:
    max_eggs = counter_red
    color = 'red'
elif counter_orange >= counter_red and counter_orange >= counter_blue and counter_orange >= counter_green:
    max_eggs = counter_orange
    color = 'orange'
elif counter_blue >= counter_red and counter_blue >= counter_orange and counter_blue >= counter_green:
    max_eggs = counter_blue
    color = 'blue'
elif counter_green >= counter_red and counter_green >= counter_orange and counter_green >= counter_blue:
    max_eggs = counter_green
    color = 'green'

print(f"Red eggs: {counter_red}")
print(f"Orange eggs: {counter_orange}")
print(f"Blue eggs: {counter_blue}")
print(f"Green eggs: {counter_green}")
print(f"Max eggs: {max_eggs} -> {color}")
