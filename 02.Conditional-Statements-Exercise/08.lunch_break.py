import math

serie = input()
timeEpisode = int(input())
timeBreak = int(input())
timeLunch = timeBreak / 8.0
timeRelax = timeBreak / 4.0
restBreak = timeBreak - timeLunch - timeRelax

if restBreak >= timeEpisode:
    print(f"You have enough time to watch {serie} and left with {math.ceil(restBreak - timeEpisode)} minutes free time.")
elif restBreak < timeEpisode:
    print(f"You don't have enough time to watch {serie}, you need {math.ceil(timeEpisode - restBreak)} more minutes.")