age_of_members_of_the_family = input()

price_toy = 5
price_sweaters = 15
below_16 = 0
over_16 = 0

while age_of_members_of_the_family != "Christmas":
    age = int(age_of_members_of_the_family)

    if age <= 16:
        below_16 += 1
    else:
        over_16 += 1
    age_of_members_of_the_family = input()

money_for_toys = below_16 * price_toy
money_for_sweaters = over_16 * price_sweaters

print(f"Number of adults: {over_16}")
print(f"Number of kids: {below_16}")
print(f"Money for toys: {money_for_toys:.0f}")
print(f"Money for sweaters: {money_for_sweaters:.0f}")
