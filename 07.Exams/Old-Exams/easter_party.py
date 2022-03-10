guests = int(input())
price_per_person = float(input())
budget = float(input())

if 9 < guests < 16:
    price_per_person *= 0.85
elif 15 < guests < 21:
    price_per_person *= 0.8
elif 20 < guests:
    price_per_person *= 0.75
cake_price = budget * 0.1
total_bill = guests * price_per_person + cake_price
rest = abs(total_bill - budget)
if total_bill <= budget:
    print(f"It is party time! {rest:.2f} leva left.")
else:
    print(f"No party! {rest:.2f} leva needed.")
