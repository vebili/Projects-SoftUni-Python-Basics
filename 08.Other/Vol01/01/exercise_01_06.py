# Списък от числа:
nums = [5, 10, 1, 60, 25, 3]
# Показване съдържанието на списъка:
print("Списък от числа:", nums)
# Дължина на списъка:
print("Дължина на списъка:", len(nums))
# Първи елемент:
print("Първи елемент:", nums[0])
# Последен елемент:
print("Последен елемент:", nums[-1])
# Най-голяма стойност:
print("Най-голяма стойност:", max(nums))
# Най-малка стойност:
print("Най-малка стойност:", min(nums))
# Сума:
print("Сума:", sum(nums))
# Списък в обратен ред:
print("Списък в обратен ред:", list(reversed(nums)))
# Сортиране по възходяща стойност:
print("По възходяща стойност:", sorted(nums))
# Сортиране по низходяща стойност:
print("По низходяща стойност:", sorted(nums, reverse=True))
# Изходен списък:
print("Изходен списък:", nums)
# Промяна на стойността на елемент в списъка:
nums[1] = "текст"
# Показване съдържанието на списъка:
print("След осъществяване на промяната:", nums)
# Срез:
print("Срез:", nums[1:len(nums) - 1])
# Замяна на част от елементите на списъка:
nums[1:-1] = ["A", "B"]
# Списъкът след замяна на елементите:
print("След замяна на елементите:", nums)
# Списък с числата от 5 до 10:
nums = list(range(5, 11))
print("Списък с числата от 5 до 10:", nums)
# Изтриване на елементи от списъка:
nums[2:4] = []
print("След изтриване на два елемента:", nums)
# Изтриване на последния елемент:
del nums[len(nums) - 1]
print("Изтрит е последният елемент:", nums)
# Нечетни числа:
nums = [2 * k + 1 for k in range(5)]
print("Нечетни числа:", nums)
# Създаване на списък от символи въз основа на текст:
symbs = list("Python")
# Показване съдържанието на списъка:
print("Списък от символи:", symbs)
# Първите два символа:
print("Първите два символа:", symbs[:2])
# Останалите символи:
print("Останалите символи:", symbs[2:])
