cinema_places_1 = int(input())
people = input()

cinema_places = cinema_places_1

total_money = 0
money_for_group = 0
ticket_price = 5

while people != "Movie time!":
    people = int(people)
    cinema_places -= people
    if cinema_places < 0:
        print(f"The cinema is full.")
        break
    money_for_group = ticket_price * people
    if people % 3 == 0:
        money_for_group -= 5
    total_money += money_for_group
    money_for_group = 0
    people = input()
if people == "Movie time!":
    print(f"There are {cinema_places} seats left in the cinema.")

print(f"Cinema income - {total_money} lv.")
