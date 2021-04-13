# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
from random import randint

n = int(input("n: "))
i, my_list = 0, []

while i < n:
    my_list.append(randint(-10,10))
    i += 1

total = 0
for elt in my_list:
    total += elt if elt > 0 else 0

print(my_list)
print(total)
