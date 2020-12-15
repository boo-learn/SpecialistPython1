# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random

# numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint

element_count = 12  # n
if 1:  # VAR1. Идея в том, чтобы инициировать пустой список, а затем использовать  for ... in range
    numbers = list()
    for _ in range(0, element_count):
        numbers.append(random.randint(-100, 100))
print(numbers)
