# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию написанную на одном из прошлых занятий.
# Получите новый список, элементами которого будут:
#   1. неповторяющиеся(уникальные) элементы исходного списка:
#   например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
#   2. элементы исходного списка, которые не имеют повторений(встречаются только один раз):
#   например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
import random

def get_rand_int_list(low, high, size):
    return [random.randint(low, high) for i in range(size)]

rand_list = get_rand_int_list(0, 10, 10)
print(rand_list)

uniq_list = []
for i in rand_list:
    if uniq_list.count(i) == 0:
        uniq_list.append(i)

print(uniq_list)

not_repeated_list = []
for i in rand_list:
    if rand_list.count(i) == 1:
        not_repeated_list.append(i)

print(not_repeated_list)
