days = int(input())
total_food = float(input())
days_counter = 0
dog_food = 0
cat_food = 0
cookies = 0
for day in range(days):
    days_counter += 1
    dog_eaten_food = int(input())
    cat_eaten_food = int(input())
    dog_food += dog_eaten_food
    cat_food += cat_eaten_food
    if days_counter == 3:
        eaten_food_per_third_day = (dog_eaten_food + cat_eaten_food) * 0.1
        cookies += eaten_food_per_third_day
        days_counter = 0
total_food_eaten = dog_food + cat_food
total_percent_eaten_food = (dog_food + cat_food) / total_food * 100
percent_dog_food = dog_food / total_food_eaten * 100
percent_cat_food = cat_food / total_food_eaten * 100
print(f"Total eaten biscuits: {round(cookies)}gr.")
print(f"{total_percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog_food:.2f}% eaten from the dog.")
print(f"{percent_cat_food:.2f}% eaten from the cat.")
