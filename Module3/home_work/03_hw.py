# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = int(input("Введите число n: "))

numbers = []

for i in range(n):
    numbers.append(random.randint(-100, 100))

print(numbers)

total = 0

for num in numbers:
    if num % 2 == 0 and num > 0:
        total += num

print(total)
