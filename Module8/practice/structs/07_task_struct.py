# Вы написали программу для работы с сотрудниками и вам ее необходимо протестировать.
# Для теста нужны большие списки сотрудников (100+).
# Вбивать вручную столько данных займет очень много времени.
# Напишите программу, генерирующую списки сотрудников со следующими параметрами:
# 1. Имя
# 2. Фамилия
# 3. Возраст
# 4. Профессия
# 5. Зарплата
# Примечание: Данные сгенерированных сотрудников могут повторяться

import os
import random


def import_data(file_name, dir="data"):
    names = []
    full_name = os.path.join(dir, file_name)

    with open(full_name, "r", encoding='UTF-8') as f:
        for line in f:
            line = line.lstrip()
            line = line.rstrip()
            names.append(line)

    return names


def gen_uniq_name(init_list, does_not_mach):
    import random
    does_not_mach_list = list()
    for lst in does_not_mach:
        does_not_mach_list += lst

    while True:
        rnd_name = random.choice(init_list)
        if rnd_name not in does_not_mach_list:
            return rnd_name


def gen_age(fr, to):
    import random
    return random.randint(fr, to)


def gen_salary(fr, to):
    import random
    return random.randint(fr, to)


boys_names = list()
boys_names = import_data(file_name="boys_names.txt")
# print(f"boys_names:{boys_names}")

girls_names = list()
girls_names = import_data(file_name="girls_names.txt")
# print(f"girls_names:{girls_names}")

names = boys_names + girls_names
# print(names)

professions = list()
professions = import_data(file_name="professions.txt")
# print(professions)


res_all = list()
for i in range(100):
    res = list()
    #name = random.choice(names)
    name = gen_uniq_name(names, res_all)
    #surname = random.choice(names)
    surname = gen_uniq_name(names, res_all)
    age = gen_age(25, 60)
    salary = gen_salary(30000, 500000)
    profession = random.choice(professions)
    res.append(name)
    res.append(surname)
    res.append(age)
    res.append(salary)
    res.append(profession)
    res_all.append(res)

for i, emp in enumerate(res_all, 1):
    print(f"employee={i}, info={emp}")

