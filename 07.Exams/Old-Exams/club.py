want_income = int(input())
cocktail = input()
price_per_cocktail = 0
total_income = 0
total = 0
while cocktail != 'Party!':
    number_cocktail = int(input())
    price_per_cocktail = len(cocktail)
    total += (number_cocktail * price_per_cocktail)
    if total % 2 != 0:
        total *= 0.75
    total_income += total
    total = 0
    if want_income <= total_income:
        print(f"Target acquired.")
        print(f"Club income - {total_income:.2f} leva.")
        break
    cocktail = input()
want_income -= total_income
if cocktail == 'Party!':
    print(f"We need {want_income:.2f} leva more.")
    print(f"Club income - {total_income:.2f} leva.")
