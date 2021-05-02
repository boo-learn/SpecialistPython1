# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
sum = 0
numbers = []
n = int(input("Введите  n:"))
for i in range(0, n):
    numbers.append(random.randint(-100, 100))
print(numbers)
for pos in numbers:
    if pos >= 0 and pos % 2 == 0:
        sum += pos
print("sum :",sum)
