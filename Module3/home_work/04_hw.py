# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

import random
numbers = []
list_sqrt = []

n = int(input())

for i in range(0, n):
    numbers.append(random.randint(-100, 100))

for number in numbers:
    if number > 0 and (number**.5).is_integer():
        list_sqrt.append(number)

print(list_sqrt)
