# Дан список из n элементов,
# заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.
import random

n = []
n_positive = []
cnt = int(input("cnt elements:"))

for i in range(cnt):
    rnd = (random.randint(-100, 100))
    n.append(rnd)

for el in n:
    if el > 0 and el % 2 == 0:
        n_positive.append(el)

res = sum(n_positive)

print(n)
print(n_positive)
print(res)
