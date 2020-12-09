# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

numbers = [2, -5, 8, 9, -25, 25, 4]

# import random
# numbers = []
# for i in range(random.randint(8, 10)):
#     numbers.append(random.randint(4, 81))
# print(numbers)

new_numbers = []

i = 0
for number in numbers:
    if number > 0 and number ** (1/2) % 1 == 0:
        new_numbers.append(int(number ** (1/2)))
        i += 1

print(new_numbers)
