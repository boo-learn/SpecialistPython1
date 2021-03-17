# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.
import random
n = int(input("n = "))
from random import randint
numbers = [randint(-100, 100) for i in range(n)]
print(numbers)
i = 0
for num in numbers:
    if num > 0 and num%2 == 0:
        print(num)

