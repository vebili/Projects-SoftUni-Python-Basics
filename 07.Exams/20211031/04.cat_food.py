import math

number_of_cats = int(input())
cat_counter = 1
group_1 = 0
group_2 = 0
group_3 = 0
total_food_weight_grams = 0.0
food_weight_in_grams = 0.0
while cat_counter <= number_of_cats:
    food_weight_in_grams = float(input())
    total_food_weight_grams += food_weight_in_grams
    if 100 <= food_weight_in_grams < 200:
        group_1 += 1
    elif 200 <= food_weight_in_grams < 300:
        group_2 += 1
    elif 300 <= food_weight_in_grams <= 400:
        group_3 += 1
    cat_counter += 1

price_for_food = (total_food_weight_grams / 1000) * 12.45
price_for_food = math.floor(price_for_food * 100) / 100
print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {price_for_food:.2f} lv.")
