# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

import random
numbers = []

n = input("Введите целое число: ")
i = 0
sum_el = 0
while i < int(n):
    el = random.randint(-100, 100)
    numbers.append(el)
    i += 1

    if el > 0 and el%2 == 0:
        sum_el += el

print(numbers)
print(sum_el)
