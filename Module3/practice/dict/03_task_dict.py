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

# TODO: your code here
max_salary = 0
for person in staff:
    if person['salary'] > max_salary:
        max_salary = person['salary']
        name = person['name'] + ' ' + person['surname']
print(name)
#print(max_salary)

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")
# TODO: your code here
min_salary = 0
for person in staff:
    if min_salary == 0 or person['salary'] < min_salary:
        min_salary = person['salary']
        name = person['name'] + ' ' + person['surname']
print(name)



print("Среднеарифметическую зарплату всех сотрудников")
# TODO: your code here
average_salary = 0
for person in staff:
    average_salary += person['salary']
print(average_salary/len(staff))



print("Количество однофамильцев в организации")
# TODO: your code here
list = []
for person in staff:
    list.append(person['surname'])
num = 0
same_surname = {}
for surname in list:
    if list.count(surname) > 1:
        same_surname[surname] = list.count(surname)
print(len(same_surname.keys()))


print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")
# TODO: your code here
salary_list = []
for person in staff:
    salary_list.append(int(person['salary']))
salary_list = sorted(salary_list)
print(salary_list)
name_list = []
for salary in salary_list:
    for person in staff:
        if int(person['salary']) == salary:
            print(person['name'] + ' ' + person['surname'])
