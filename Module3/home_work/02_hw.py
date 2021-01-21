# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []

#print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
n = int(input())

for i in range(0, n):
    numbers.append(random.randint(-100, 100))

for number in numbers:
    print(number)
