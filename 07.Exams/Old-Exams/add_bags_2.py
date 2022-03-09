price_suitcase_over_20_kg = float(input())
kg_suitcase = float(input())
day_to_travel = int(input())
number_suitcase = int(input())

if kg_suitcase < 10:
    price_suitcase_over_20_kg *= 0.2
elif 10 <= kg_suitcase <= 20:
    price_suitcase_over_20_kg /= 2
if day_to_travel < 7:
    price_suitcase_over_20_kg *= 1.4
elif 7 <= day_to_travel <= 30:
    price_suitcase_over_20_kg *= 1.15
else:
    price_suitcase_over_20_kg *= 1.1
total_cost = price_suitcase_over_20_kg * number_suitcase
print(f"The total price of bags is: {total_cost:.2f} lv.")
