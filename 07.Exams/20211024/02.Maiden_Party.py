price_of_party = float(input())
number_of_love_messages = int(input())
number_of_wax_roses = int(input())
number_of_keychains = int(input())
number_of_cartoons = int(input())
number_of_lucky_surprises = int(input())

price_love_messages = number_of_love_messages * 0.60
price_of_wax_roses = number_of_wax_roses * 7.20
price_of_keychains = number_of_keychains * 3.60
price_of_cartoons = number_of_cartoons * 18.20
price_of_lucky_surprises = number_of_lucky_surprises * 22

sum_prices = price_of_keychains + price_of_wax_roses + price_of_lucky_surprises + price_love_messages + price_of_cartoons

num_of_articles = number_of_love_messages + number_of_lucky_surprises + number_of_keychains + number_of_wax_roses + number_of_cartoons

if num_of_articles >= 25:
    sum_prices = sum_prices * 0.65

hosting_cost = sum_prices * 0.90

if hosting_cost >= price_of_party:
    money_left = hosting_cost - price_of_party
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_need = price_of_party - hosting_cost
    print(f"Not enough money! {money_need:.2f} lv needed.")
