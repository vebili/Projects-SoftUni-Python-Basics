import csv

max = int(input("Qty of lines to read: "))

k = 0
with open('1.csv') as f:
  f_csv = csv.reader(f)
  headers = next(f_csv)
  for row in f_csv:
    print(row)
    k = k + 1
    if k == max:
        break
