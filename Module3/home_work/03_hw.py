# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

#generating list of numbers:
from random import randint

n = int(input())
numbers = []
i = 1
while i <= n:
    numbers.append(randint(-100, 100))
    i += 1

# sum calculation:
my_sum = 0
for num in numbers:
    if num > 0 and num % 2 == 0:
        my_sum += num
print(my_sum)
