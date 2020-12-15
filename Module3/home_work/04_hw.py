# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
import random

element_count = 4  # n

numbers = list()
for _ in range(0, element_count):
    numbers.append(random.randint(8, 16))
print('dano: ', numbers)

new_list = list()
for el in numbers:
    if el <= 0:
        continue
    boolean = int(el ** 0.5) == el ** 0.5
    if boolean:
        new_list.append(el)
print('result: ', new_list)
