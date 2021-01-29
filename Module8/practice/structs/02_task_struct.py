# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию написанную на одном из прошлых занятий.
# Получите новый список, элементами которого будут:
#   1. неповторяющиеся(уникальные) элементы исходного списка:
#   например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
#   2. элементы исходного списка, которые не имеют повторений(встречаются только один раз):
#   например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
import random

amount = random.randrange(10, 15)
print(amount)
list = []
while amount != 0:
    list.append(random.randint(0, 100))
    amount -= 1

print(list)
no_repeats = set(list)
print(no_repeats)
no_repeats_from_list = set()

for el in no_repeats:
    i = 0
    for obj in list:
        if obj == el:
            i += 1
    #print(i)
    if i == 1:
        no_repeats_from_list.add(el)

print(no_repeats_from_list)
