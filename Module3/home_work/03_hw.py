# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

element_count = 4  # n

numbers = list()
for _ in range(0, element_count):
    numbers.append(random.randint(-100, 100))

print(numbers)
summ = 0
for number in numbers:
    if number % 2 == 0  and number > 0:
        summ += number
print(summ)
