# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально,
# а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os
import settings
from pprint import pprint

datadir = os.path.join(settings.BASE_DIR, 'Mod06', 'data')
# print(datadir)
str_workers = os.path.join(datadir, 'workers.txt')
str_hours = os.path.join(datadir, 'hours_of.txt')


# print(str_workers)
# print(str_hours)

# parse space separated file
def parse(fname):
    with open(fname, 'r', encoding='utf-8') as fil:
        out_list = list()
        header = ''
        while not header:
            header = fil.readline()
            header = header.rstrip()
        keys = header.split()
        for line in fil:
            words = line.split()
            out_list.append(dict(zip(keys, words)))
    return out_list


worker_base = parse(str_workers)
worker_hours_base = parse(str_hours)
# pprint(worker_base)
# pprint(worker_hours_base)

salary_list = list()
for worker in worker_base:
    lam = lambda x: (x['Имя'] == worker['Имя']) and (x['Фамилия'] == worker['Фамилия'])
    worker_hours = list(filter(lam, worker_hours_base))
    # pprint(worker_hours)
    fact = float(worker_hours[0]["Отработано"])
    tariff = float(worker['Зарплата'])
    norm = float(worker["Норма_часов"])
    if norm >= fact:
        salary = tariff * fact / norm
    else:
        salary = (2 * fact - norm) / norm * tariff

    salary_list.append({'Имя': worker['Имя'], 'Фамилия': worker['Фамилия'], 'начислено': salary})
pprint(salary_list)
