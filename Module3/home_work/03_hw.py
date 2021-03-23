# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум

import random
numbers = []

n = int(input("Please enter n: "))
i = 0

while i < n:
    numbers.append(random.randint(-100, 100))
    i = i + 1

print (numbers)

s = 0
i = 0

while i < n:
    if (numbers[i] > 0) and (numbers[i] % 2 == 0):
        s = s + int(numbers[i])
    i = i + 1
print("Sum of positive numbers dividable by 2:", s)
