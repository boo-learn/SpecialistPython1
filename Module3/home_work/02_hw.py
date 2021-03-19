# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here
from random import randint

n = int(input())
numbers = []
i = 1
while i <= n:
    numbers.append(randint(-100, 100))
    i += 1
print(numbers)
