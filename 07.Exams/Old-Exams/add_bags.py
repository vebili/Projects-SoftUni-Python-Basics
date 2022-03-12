prise_above_20_kg = float(input())
baggage_kg = float(input())
days_to_travel = int(input())
count_of_baggage = int(input())

baggage_price = 0

if baggage_kg < 10:
    baggage_price = prise_above_20_kg * 0.20
elif 10 <= baggage_kg <= 20:
    baggage_price = prise_above_20_kg * 0.50
elif baggage_kg > 20:
    baggage_price = prise_above_20_kg

if days_to_travel > 30:
    baggage_price *= 1.10
elif 7 <= days_to_travel <= 30:
    baggage_price *= 1.15
elif days_to_travel < 7:
    baggage_price *= 1.40

total_price = baggage_price * count_of_baggage

print(f'The total price of bags is: {total_price:.2f} lv.')
