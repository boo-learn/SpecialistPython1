# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.
import random

random.seed(2)


def list_number(at, to, size):
    numbers = []
    while size > 1:
        numbers.append(random.randint(at, to))
        size -= 1
    return numbers


a = -50
b = 50
n = 30
tup1 = (list_number(a, b, n))
tup2 = (list_number(a, b, n))
tup3 = (list_number(a, b, n))

print(tup1)
print(tup2)
print(tup3)
i = 0  # счетчик одинаковых элементов
match_numbers = []  # список совпадающих элементов
for el in tup1:
    if tup2.count(el) > 0 and tup3.count(el) > 0 and match_numbers.count(el) == 0:
        match_numbers.append(el)
        i += 1
print('\n'f"Совпадающих элементов {i} - {match_numbers}")
