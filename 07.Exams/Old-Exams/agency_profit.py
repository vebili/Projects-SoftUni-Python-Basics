company = input()
adults = int(input())
children = int(input())
net_price_adult = float(input())
tax = float(input())

net_price_child = net_price_adult * 0.3
price_after_tax_adult = tax + net_price_adult
price_after_tax_child = net_price_child + tax

total_price_all_tickets = (children * price_after_tax_child) + (adults * price_after_tax_adult)
earnings = total_price_all_tickets * 0.2

print(f"The profit of your agency from {company} tickets is {earnings:.2f} lv.")
