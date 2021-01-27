# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random
import statistics

def random_list(min, max, size):
    list = []
    for el in range(size):
        new_el = random.randint(min, max)
    return list.append(new_el)


new_list = random_list(-10, 50, 10)

not_more_10 = [el for el in new_list if el <= 10]

positive_list = [el for el in new_list if el > 0]

sum_list = statistics.mean(map(lambda el: el // 2 == 0, new_list))
