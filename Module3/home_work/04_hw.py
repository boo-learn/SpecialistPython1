# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

import random
numbers = []

n = int(input("Please enter n: "))
i = 0

while i < n:
    numbers.append(random.randint(-100, 100))
    i = i + 1

print ("Initial list: ", numbers)

sq_numbers = []
sq = 0
i = 0

while i < n:
    if numbers[i] > 0:
        sq = numbers[i]**0.5
        if int(sq) == sq:               #suggestion from StackOverflow portal
            sq_numbers.append(int(sq))
    i = i + 1

print ("SQRTs list: ", sq_numbers)
