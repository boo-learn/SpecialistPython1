# Данные о сотрудниках в программе хранятся в словаре
import sys

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

max_salary = 0
for el in staff:
    if el["salary"] > max_salary:
        max_employee = el
        max_salary = el["salary"]
print(max_employee["name"], max_employee["surname"])

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

min_salary = sys.maxsize * 2 + 1
for el in staff:
    if el["salary"] < min_salary:
        min_employee = el
        min_salary = el["salary"]
print(min_employee["name"], min_employee["surname"])

print("Среднеарифметическую зарплату всех сотрудников")

summa = 0
for el in staff:
    summa += el["salary"]
print(summa / len(staff))

print("Количество однофамильцев в организации")

# TODO: your code here

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

# TODO: your code here

