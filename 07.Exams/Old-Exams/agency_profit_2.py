company = input()
adult_tickets = int(input())
kids_tickets = int(input())
price_adult = float(input())
taxes = float(input())

price_kids = price_adult * 0.3
profit = (adult_tickets * price_adult + kids_tickets * price_kids + (adult_tickets + kids_tickets) * taxes) * 0.2

print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")
