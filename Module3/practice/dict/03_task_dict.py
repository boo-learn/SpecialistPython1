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
max_salary=0
for st in staff:
    if st['salary']>max_salary:
        max_salary=st['salary']
        top_employee=st['name']+' '+st['surname']
print(top_employee)
# TODO: your code here

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")
min_salary=max_salary
for st in staff:
    if st['salary']<min_salary:
        min_salary=st['salary']
        bottom_employee=st['name']+' '+st['surname']
print(bottom_employee)
# TODO: your code here

print("Среднеарифметическую зарплату всех сотрудников")
aver_salary=0
for st in staff:
    aver_salary+=st['salary']
aver_salary/=len(staff)
print(aver_salary)
# TODO: your code here

print("Количество однофамильцев в организации")
counter=0
surnames=[]
for st in staff:
    surnames.append(st['surname'])
print(surnames)
for st in staff:
    counter=+surnames.count(st['surname'])
print(counter)
# TODO: your code here

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")
staff_sorted = sorted(staff, key=lambda k: k['salary'])
st_list=[]
for st in staff_sorted:
    st_list.append(str(st['name']+' '+st['surname']))
print(st_list)
# TODO: your code here
