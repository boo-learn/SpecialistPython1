# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию написанную на одном из прошлых занятий.
# Получите новый список, элементами которого будут:
#   1. неповторяющиеся(уникальные) элементы исходного списка:
#   например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
#   2. элементы исходного списка, которые не имеют повторений(встречаются только один раз):
#   например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
def gen_digits(n):
    import random
    numbers = []
    for _ in range(n):
        new_el = random.randint(-100, 100)
        numbers.append(new_el)
    return numbers


our_list = gen_digits(10)
our_list = [1, 2, 4, 5, 6, 2, 5, 2]
print(our_list)
list_uniq = [our_list[0]]

for i in our_list:
    count = 0
    for j in range(len(our_list)):
        if i == our_list[j]:
            count += 1
    if count > 1:
        our_list.remove(i)
print(our_list)
