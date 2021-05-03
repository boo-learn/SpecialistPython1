# Данные о сотрудниках в программе хранятся в словаре
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

for pers in staff:
    if dict(pers)["salary"]>highest_salary:
        highest_salary = float(dict(pers)["salary"])
        highest_salary_name = [dict(pers)['surname'], dict(pers)['name']]
highest_salary_name=" ".join(highest_salary_name)

for pers in staff:
    if dict(pers)["salary"]<lowest_salary:
        lowest_salary = float(dict(pers)["salary"])
        lowest_salary_name = [dict(pers)['surname'], dict(pers)['name']]
lowest_salary_name=" ".join(lowest_salary_name)
print(f"{highest_salary_name} has the highest salary")
print(f"{lowest_salary_name} has the lowest salary")

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

# TODO: your code here

print("Среднеарифметическую зарплату всех сотрудников")

# TODO: your code here

print("Количество однофамильцев в организации")

# TODO: your code here

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

# TODO: your code here
