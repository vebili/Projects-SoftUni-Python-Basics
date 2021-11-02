actor = input()
academy_points = float(input())
jury = int(input())

for x in range(jury):
    jury_name = input()
    points = float(input())
    academy_points += (len(jury_name) * points) / 2
    if academy_points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {academy_points:.1f}!")
        break

if academy_points <= 1250.5:
    print(f"Sorry, {actor} you need {1250.5 - academy_points:.1f} more!")
