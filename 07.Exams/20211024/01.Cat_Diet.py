percent_fats = int(input())
percent_proteins = int(input())
percent_carbs = int(input())
all_calories = int(input())
percent_water = int(input())

fats_grams = ((percent_fats / 100) * 2500) / 9
protein_grams = ((percent_proteins / 100) * 2500) / 4
carb_grams = ((percent_carbs / 100) * 2500) / 4


cat_weight = fats_grams + protein_grams + carb_grams
weight_per_gram = 2500 / cat_weight

calories = weight_per_gram * (1 - percent_water / 100)
print(f"{calories:.4f}")
