number = int(input())
area_left = 0
area_right = 0

for x in range(number):
    number_left = int(input())
    area_left += number_left
for i in range(number):
    number_right = int(input())
    area_right += number_right
if area_left == area_right:
    print(f'Yes, sum = {area_right}')
else:
    print(f'No, diff = {abs(area_right - area_left)}')
