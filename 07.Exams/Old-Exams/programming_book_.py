cost_for_page = float(input())
cost_for_cover = float(input())
percent_discount_for_paper_print = int(input())
designer_cost = float(input())
percent_paid_of_team = int(input())

preliminary_cost = (cost_for_page * 899) + (cost_for_cover * 2)

publishing_house_discount = percent_discount_for_paper_print / 100

discount_cost = preliminary_cost - (preliminary_cost * publishing_house_discount)

current_cost = discount_cost + designer_cost

team_discount = current_cost * percent_paid_of_team / 100

final_cost = current_cost - team_discount

print(f'Avtonom should pay {final_cost:.2f} BGN.')
