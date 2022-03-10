import math

people = int(input())
tax = float(input())
price_bed = float(input())
price_umbrella = float(input())

total_price_bed = math.ceil(people * 0.75) * price_bed
total_price_umbrella = math.ceil(people / 2) * price_umbrella
total_price_tax = people * tax
total = total_price_tax + total_price_umbrella + total_price_bed
print(f'{total:.2f} lv.')
