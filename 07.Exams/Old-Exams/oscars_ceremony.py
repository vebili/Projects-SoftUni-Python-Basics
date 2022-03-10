rent = int(input())

statues = rent * 0.7
catering = statues * 0.85
sound = catering / 2

total_sum = rent + statues + catering + sound
print(f'{total_sum:.2f}')
