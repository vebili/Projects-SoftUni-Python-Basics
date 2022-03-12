bed = float(input())
cat_toilet = float(input())

food = cat_toilet * 1.25
toys = food * 0.5
doctor = toys * 1.1
month_expenses = cat_toilet + food + toys + doctor
month_expenses *= 1.05

total_expenses = month_expenses * 12 + bed

print(f'{total_expenses:.2f} lv.')
