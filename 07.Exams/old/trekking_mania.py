groups = int(input())
musala = 0
monblan = 0
kilimangaro = 0
k2 = 0
everest = 0
total_people = 0
for group in range(groups):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group < 6:
        musala += people_in_group
    elif people_in_group < 13:
        monblan += people_in_group
    elif people_in_group < 26:
        kilimangaro += people_in_group
    elif people_in_group < 41:
        k2 += people_in_group
    else:
        everest += people_in_group
musala = musala / total_people * 100
monblan = monblan / total_people * 100
kilimangaro = kilimangaro / total_people * 100
k2 = k2 / total_people * 100
everest = everest / total_people * 100
print(f'{musala:.2f}%')
print(f'{monblan:.2f}%')
print(f'{kilimangaro:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')
