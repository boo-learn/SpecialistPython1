# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
n = int(input("Enter quantity of elements: "))
numbers = []
i = 0

for i in range(n):
    r = random.randint(-100, 100)
    numbers.append(r)

print(numbers)
