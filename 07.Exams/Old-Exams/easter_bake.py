import math

number_bake = int(input())

counter_sugar = 0
counter_flour = 0
max_sugar = 0
max_flour = 0
pocket_of_sugar = 0
pocket_of_flour = 0

for bake in range(1, number_bake + 1):
    needed_sugar = int(input())
    needed_flour = int(input())
    if max_sugar <= needed_sugar:
        max_sugar = needed_sugar
    if max_flour <= needed_flour:
        max_flour = needed_flour
    counter_flour += needed_flour
    counter_sugar += needed_sugar

pocket_of_sugar = math.ceil(counter_sugar / 950)
pocket_of_flour = math.ceil(counter_flour / 750)

print(f"Sugar: {pocket_of_sugar}")
print(f"Flour: {pocket_of_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
