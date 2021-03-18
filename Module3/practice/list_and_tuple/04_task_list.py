# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

import random
numbers = []

n = int(input("Please enter n: "))
i = 0

while i < n:
    numbers.append(random.randint(-10, 10))
    i = i + 1

print ("List: ", numbers)

i = 0
sum = 0

while i < n:
    if numbers[i] > 0:
        sum = sum + numbers[i]
    i = i + 1
    
print ("Sum of positives: ", sum)
