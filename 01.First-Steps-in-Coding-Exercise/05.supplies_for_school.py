bag_pencils = int(input())
bag_markers = int(input())
liters_cleaner = float(input())
percent_discount = int(input())

sum_pencils = bag_pencils * 5.80
sum_markers = bag_markers * 7.20
sum_cleaner = liters_cleaner * 1.20

sum_all = sum_cleaner + sum_markers + sum_pencils

price_after_disc = sum_all - (sum_all * (percent_discount / 100))

print(float(price_after_disc))