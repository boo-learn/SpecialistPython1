# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random


def rand_list(n, low=-10, up=10):
    numbers = list()
    for _ in range(0, n):
        numbers.append(random.randint(low, up))
    return numbers


def count_el(n):
    i = 0
    for _ in n:
        i += 1
    return i


lst = rand_list(9, up=20)
print(lst)
# 1
print("number of elems le 10 ",count_el(filter(lambda x: x <= 10, lst)))
# 2
print("sum of elems gt 0",sum(filter(lambda x: x > 0, lst)))
# 3
even_count = count_el(filter(lambda x: x % 2 == 0, lst))
print(even_count)
even_sum = sum(map(lambda x: x % 2 == 0, lst))
print("mean of even elems",even_sum/even_count)
