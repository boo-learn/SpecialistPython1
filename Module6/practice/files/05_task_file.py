# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально,
# а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os
from settings import BASE_DIR
from pprint import pprint


def list_from_file(f):
    lst = list(line.rstrip() for line in f)
    f.close()
    return list(line.split() for line in lst[:])


def str_to_digit(lst):
    for el in lst:
        i = 0
        while i < len(el):
            el[i] = float(el[i]) if el[i].isdigit() else el[i]
            i += 1
    return lst


file_path_workers = os.path.join(BASE_DIR, "Files", "workers.txt")
file_path_hours = os.path.join(BASE_DIR, "Files", "hours_of.txt")
f_workers = open(file_path_workers, "r", encoding="utf-8")
f_hours = open(file_path_hours, "r", encoding="utf-8")
list_workers = str_to_digit(list_from_file(f_workers)[1:])
list_hours = str_to_digit(list_from_file(f_hours)[1:])

# Решение не очень нравится... быстродействие порядка O(n^2). Надо как-то по другому
for el in list_workers:
    for i in list_hours:
        if i[0] + i[1] == el[0] + el[1]:
            el.append(i[2])
    el.append(el[2] * el[5] / el[4] if el[5] <= el[4] else el[2] * (1 + 2 * (el[5] - el[4]) / el[4]))
    el[-1] = round(el[-1], 2)
pprint(list_workers)
