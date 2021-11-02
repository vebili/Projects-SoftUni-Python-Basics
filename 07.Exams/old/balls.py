count_of_balls = int(input())

total_points = 0
count_red_balls = 0
count_orange_balls = 0
count_yellow_balls = 0
count_white_balls = 0
count_of_other_colors_balls = 0
count_of_divisions_from_black_balls = 0

for sequence_of_balls in range(1, count_of_balls + 1):
    ball_color = input()
    if ball_color == 'red':
        total_points += 5
        count_red_balls += 1
    elif ball_color == 'orange':
        total_points += 10
        count_orange_balls += 1
    elif ball_color == 'yellow':
        total_points += 15
        count_yellow_balls += 1
    elif ball_color == 'white':
        total_points += 20
        count_white_balls += 1
    elif ball_color == 'black':
        total_points = int(total_points / 2)
        count_of_divisions_from_black_balls += 1
    else:
        count_of_other_colors_balls += 1
        continue

print(f'Total points: {total_points}')
print(f'Points from red balls: {count_red_balls}')
print(f'Points from orange balls: {count_orange_balls}')
print(f'Points from yellow balls: {count_yellow_balls}')
print(f'Points from white balls: {count_white_balls}')
print(f'Other colors picked: {count_of_other_colors_balls}')
print(f'Divides from black balls: {count_of_divisions_from_black_balls}')
