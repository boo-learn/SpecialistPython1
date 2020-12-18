# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию написанную на одном из прошлых занятий.
# Получите новый список, элементами которого будут:
#   1. неповторяющиеся(уникальные) элементы исходного списка:
#   например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
#   2. элементы исходного списка, которые не имеют повторений(встречаются только один раз):
#   например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
import random
def gen_list(size=20, of=1, to=5):
    rand_list=[]
    for i in range(size):
        rand_list.append(random.randint(of, to))
    return rand_list


lst1=gen_list()
lst1_unic=list(set(lst1))
print(lst1)
print(lst1_unic)
lst2=gen_list(10,1,10)
lst2_np_repeat=[]
for el in lst2:
    if lst2.count(el)==1:
        lst2_np_repeat.append(el)
print(lst2)
print(lst2_np_repeat)
