deposit_sum = float(input())
month = int(input())
gpr = float(input())/100
month_profit = (deposit_sum * gpr) / 12
profit = deposit_sum + (month * month_profit)
print(profit)