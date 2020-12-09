# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.
from random import randint

mylist = [randint(-100, 100) for x in range(1, 100)]
print('Summa:', sum(x for x in mylist if x % 2 and x > 0))
