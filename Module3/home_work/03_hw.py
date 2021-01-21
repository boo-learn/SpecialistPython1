# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

numbers = []

n = int(input("Введите количество чисел: "))
sum = 0
for i in range(n):
    numbers.append(random.randint(-100, 100))
    if numbers[i] > 0 and numbers[i] % 2 == 0:
        sum += numbers[i]
print(numbers)
print(sum)
