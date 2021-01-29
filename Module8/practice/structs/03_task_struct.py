# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random


def gen_list(size, at=-10, to=10):
    return [random.randint(at, to) for _ in range(size)]


lst1 = gen_list(10, -10, 20)
print(lst1)

ten = [el for el in lst1 if el < 10]
# print(ten)
print('1. Количество элементов списка не превышающие 10')
print(len(ten))

positive = [el for el in lst1 if el > 0]
# print(positive)
print('2. Сумму всех положительных элементов списка')
print(sum(positive))

avg_positive_even = [el for el in lst1 if el % 2 == 0]
# print(avg_positive_even)
print('3. Среднее арифметическое всех четных элементов')
print(sum(avg_positive_even)/len(avg_positive_even))
