recording_time = int(input())
number_of_scene = int(input())
time_for_scene = int(input())

area = recording_time * 0.15
area_1 = (number_of_scene * time_for_scene) + area
time = abs(recording_time - area_1)

if recording_time >= area_1:
    print(f"You managed to finish the movie on time! You have {round(time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(time)} minutes.")
