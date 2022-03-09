chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

price_chicken_menu = chicken_menu * 10.35
price_fish_menu = fish_menu * 12.40
price_vegetarian_menu = vegetarian_menu * 8.15

sum_all_menus = price_fish_menu + price_chicken_menu + price_vegetarian_menu

dessert = sum_all_menus * 0.20

final_sum = sum_all_menus + dessert + 2.50

print(final_sum)
