# Първи речник:
nums = {100: "стотица", 1: "единица", 10: "десетка"}
# Съдържание на речника:
print(nums)
print("1:  ", nums[1])
print("10: ", nums[10])
print("100:", nums[100])
# Операции с речника:
nums[3] = "тройка"
nums[10] = "десетка"
nums.pop(100)
print(nums)
# Втори речник:
order = dict(Първи=1, Трети=3, Последен=10)
# Съдържание на речник:
print(order)
print("Първи:   ", order["Първи"])
print("Трети:   ", order["Трети"])
print("Последен:", order["Последен"])
# Операции с речник:
order["Последен"] = 12
del order["Трети"]
order["Пети"] = 5
print(order)