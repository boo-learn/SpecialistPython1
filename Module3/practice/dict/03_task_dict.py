staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")

# TODO: your code here
max_salary = sorted(staff, key = lambda x: -x["salary"])[0]["salary"]
employees_max_salary = filter(lambda x: x["salary"] == max_salary, staff)
print(list(employees_max_salary))


print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

# TODO: your code here
min_salary = sorted(staff, key = lambda x: x["salary"])[0]["salary"]
employees_min_salary = filter(lambda x: x["salary"] == min_salary, staff)
print(list(employees_min_salary))


print("Среднеарифметическую зарплату всех сотрудников")

# TODO: your code here
sum_salary, cnt = 0, 0
for employee in staff:
    sum_salary += employee["salary"]
    cnt += 1
print(f"avg salary: {sum_salary / cnt :.2f}")

print("Количество однофамильцев в организации")

# TODO: your code here
dic_dupl, cnt_dupl = {}, 0
for employee in staff:
    if employee["surname"] in dic_dupl:
        dic_dupl[employee["surname"]] += 1
    else:
        dic_dupl[employee["surname"]] = 1
for sn in dic_dupl.values():
    if sn > 1:
        cnt_dupl += 1
print(cnt_dupl)

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

# TODO: your code here
def salary_sort(dic):
    return dic["salary"]

dic_sort = sorted(staff, key=salary_sort)
print(dic_sort)
