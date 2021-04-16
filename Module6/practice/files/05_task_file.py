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


def dict_from_list(lst):
    d_lst = {}
    for el in lst[1:]:
        i = 2
        dict = {}
        while i < len(lst[0]):
            dict[lst[0][i]] = el[i]
            i += 1
        d_lst[f"{el[1]}_{el[0]}"] = dict
    return d_lst


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
list_workers = str_to_digit(list_from_file(f_workers))
list_hours = str_to_digit(list_from_file(f_hours))
dict_workers = dict_from_list(list_workers)
dict_hours = dict_from_list(list_hours)

for el in dict_workers.items():
    dw = dict_workers[el[0]]
    dh = dict_hours[el[0]]
    if dw["Норма_часов"] >= dh["Отработано_часов"]:
        dw["На_руки"] = round(dw["Зарплата"] / dw["Норма_часов"] * dh["Отработано_часов"], 2)
    else:
        dw["На_руки"] = round(
            dw["Зарплата"] * (1 + 2 * (dh["Отработано_часов"] - dw["Норма_часов"]) / dw["Норма_часов"]), 2)
    dw["Отработано_часов"] = dh["Отработано_часов"]


# pprint(list(dict_workers.items()))
f=open(os.path.join(BASE_DIR,"Files","wokers_salary.txt"), "w", encoding="utf-8")
for el in dict_workers.items():
    f.writelines(f"{el[0]}\n{el[1]}\n")
f.close()
