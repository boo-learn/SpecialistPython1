# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
numbers = []
i=0
while(i<5):
    i+=1
    numbers.append(random.randint(-100, 100))
print(numbers)
sum=0
for elm in numbers:
    if(elm>0 and (not (elm%2) ) ):
        sum= sum + elm
print(sum)

