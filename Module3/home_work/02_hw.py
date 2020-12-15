# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here

n = int(input('Введите количество элементов списка: '))

a = -100
b = 100

numbers = []
for _ in range(n):
    number = random.randint(a, b)
    numbers.append(number) 
print(numbers)
