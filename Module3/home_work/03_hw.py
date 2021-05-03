# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

numbers = []
n = 10

i = 0
while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1
print(numbers)

s = 0
for number in numbers:
    if number > 0 and number % 2 == 0:
        s += number
print(s)
