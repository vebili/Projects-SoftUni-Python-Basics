import math

movie_name = input()
seasons = int(input())
episode = int(input())
time_episode = float(input())
time_advertising = seasons * episode * time_episode * 1.2 + (seasons * 10)
print(f"Total time needed to watch the {movie_name} series is {math.ceil(time_advertising)} minutes.")
