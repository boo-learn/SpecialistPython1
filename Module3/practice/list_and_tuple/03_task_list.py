# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.
import random
a = []
n = int(input ("How many list members do you want: "))
for elements in range (n):
    a.append(random.randrange(-10,10))
#print (a)
print(sum(a))
