# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
n = int(input("n = "))
from random import randint
numbers  = [randint(-100, 100) for i in range(n)]
print(numbers)
