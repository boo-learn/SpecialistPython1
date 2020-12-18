# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random

def gen_list(size, of=-6, to=16):
    return [random.randint(of, to) for _ in range(size)]

lst = gen_list(6)

count_ten = len (list(filter(lambda el: el<=10,lst)))
plus_sum = sum(el for el in lst if el>0)
mid_arif = (sum(el for el in lst if el%2==0)/len(list(el for el in lst if el%2==0)))
print(lst)
print(count_ten)
print(plus_sum)
print(mid_arif)
