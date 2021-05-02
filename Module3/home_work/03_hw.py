# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
n = int(input('Введите n: '))
numbers = []
sum = 0
i = 1
while i <= n:
    numbers.append(random.randint(-100, 100))
    i += 1
print(numbers)

for number in numbers:
    if number > 0 and number % 2 == 0:
        sum += number
print('Cумма положительных элементов кратных двум:', sum)
