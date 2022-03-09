budget = float(input())
people = int(input())
price_per_cloth = float(input())

price_for_decor = budget * 0.10
total_sum_cloth = people * price_per_cloth
if people > 150:
    total_sum_cloth *= 0.90

total_sum = price_for_decor + total_sum_cloth

if total_sum > budget:
    result = total_sum - budget
    print("Not enough money!")
    print(f'Wingard needs {result:.2f} leva more.')
elif total_sum <= budget:
    result = budget - total_sum
    print("Action!")
    print(f'Wingard starts filming with {result:.2f} leva left.')
