import math

series = input()
timeEpisode = int(input())
timeBreak = int(input())
timeLunch = timeBreak / 8.0
timeRelax = timeBreak / 4.0
restBreak = timeBreak - timeLunch - timeRelax

if restBreak >= timeEpisode:
    print(f"You have enough time to watch {series} and left with "
          f"{math.ceil(restBreak - timeEpisode)} minutes free time.")
elif restBreak < timeEpisode:
    print(f"You don't have enough time to watch {series}, you need "
          f"{math.ceil(timeEpisode - restBreak)} more minutes.")
