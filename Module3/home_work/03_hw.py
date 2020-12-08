# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
numbers = []
for i in range(random.randint(0, 10)):
    numbers.append(random.randint(-100, 100))
#print(numbers)

summ = 0
for number in numbers:
    if number > 0 and number % 2 == 0:
        summ += number

print(summ)
