# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

import random
a = []
n = int(input ("How many list members do you want: "))
i = 0
pos_sum=0
for elements in range (n):
    a.append(random.randrange(-10,10))
    if a[i]>0:
        pos_sum+=a[i]
    i+=1
#print (a)
print(pos_sum)
