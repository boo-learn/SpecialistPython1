# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
numbers = []

#print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
n = int(input())

for i in range(0, n):
    numbers.append(random.randint(-100, 100))

num_sum = 0

for number in numbers:
    if number > 0 and number%2 == 0:
        num_sum += number

print("Сумма =", num_sum)
