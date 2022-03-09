nylon_needed = int(input())
paint_in_l = int(input())
thinner_in_l = int(input())
hours_of_work = int(input())

sum_nylon = (nylon_needed + 2) * 1.50
sum_paint_in_l = (paint_in_l + (paint_in_l * (10 / 100))) * 14.50
sum_thinner_in_l = thinner_in_l * 5
sum_bags = 0.4

sum_all = sum_bags + sum_nylon + sum_thinner_in_l + sum_paint_in_l

sum_for_workers = (sum_all * 0.3) * hours_of_work

sum_everything = sum_all + sum_for_workers

print(sum_everything)
