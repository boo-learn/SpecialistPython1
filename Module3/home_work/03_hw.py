# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = int(input('Введите кол-во элементов: '))
numbers = []
while n > 0:
    numbers.append(random.randint(-100, 100))
    n -= 1
print(numbers)

pos_sum = 0
for el in numbers:
    if el % 2 == 0 and el >= 0:
        pos_sum += el

print(pos_sum)
