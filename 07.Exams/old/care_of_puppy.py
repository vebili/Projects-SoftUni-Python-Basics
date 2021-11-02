purchased_kg_food = int(input())
eat_gr_per_day = input()
purchased_kg_food *= 1000
needed_food = 0
while eat_gr_per_day != 'Adopted':
    eat_gr_per_day = int(eat_gr_per_day)
    needed_food += eat_gr_per_day
    eat_gr_per_day = input()
diff_food = abs(needed_food - purchased_kg_food)
if needed_food <= purchased_kg_food:
    print(f"Food is enough! Leftovers: {diff_food} grams.")
else:
    print(f"Food is not enough. You need {diff_food} grams more.")
