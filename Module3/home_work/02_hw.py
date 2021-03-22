# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
numbers = []

n = int(input("n:"))

for el in range(n):
    rnd = random.randint(-100, 100)
    numbers.append(rnd)

print(numbers)
