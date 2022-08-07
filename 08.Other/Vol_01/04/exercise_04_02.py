# Включване на функция за генериране на случайни числа:
from random import *

# Инициализация на генератор на случайни числа:
seed(2019)
# Брой различни случайни числа:
count = 10
# Създаване на празно множество:
nums = set()
# Генериране на случайни числа:
while len(nums) < count:
    nums.add(randint(1, count + 5))
# Показване на резултата:
print(nums)