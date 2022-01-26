import math

balls = int(input())
points = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
others = 0
for x in range(balls):
    ball_color = input()
    if ball_color == 'red':
        red += 1
        points += 5
    elif ball_color == 'orange':
        orange += 1
        points += 10
    elif ball_color == 'yellow':
        yellow += 1
        points += 15
    elif ball_color == 'white':
        white += 1
        points += 20
    elif ball_color == 'black':
        black += 1
        points = math.floor(points / 2)
    else:
        others += 1

print(f'Total points: {points}')
print(f'Points from red balls: {red}')
print(f'Points from orange balls: {orange}')
print(f'Points from yellow balls: {yellow}')
print(f'Points from white balls: {white}')
print(f'Other colors picked: {others}')
print(f'Divides from black balls: {black}')