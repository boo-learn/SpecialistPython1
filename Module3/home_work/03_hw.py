# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
numbers = []
n = 10
for _ in range(n):
    numbers.append(random.randint(-100, 100))
summa = 0
for num in numbers:
    if num > 0 and num % 2 == 0:
        summa += num
print(summa)
