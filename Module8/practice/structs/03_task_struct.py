# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random

def get_rand_int_list(low, high, size):
    return [random.randint(low, high) for _ in range(size)]

rand_list = get_rand_int_list(5, 20, 10)
print(rand_list)

less_ten_list = list(filter(lambda x: x <= 10, rand_list))
print(less_ten_list)

sum_all = sum(list(filter(lambda x: x > 0, rand_list)))
print(sum_all)

even_list = list(filter(lambda x: not x % 2, rand_list))
print(even_list)

avarage = sum(even_list)/len(even_list)
print(avarage)
