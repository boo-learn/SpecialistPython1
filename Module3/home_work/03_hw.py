# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

# Используем генератор списка из предыдущего задания
import random
#print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here
n = int(input('Введите количество элементов списка: '))
a = -100
b = 100
numbers = []
for _ in range(n):
    number = random.randint(a, b)
    numbers.append(number) 
print(numbers)
#=============================================================================
# Вывести на экран сумму всех положительных элементов кратных двум.
sum_num = 0
for number in numbers:
    if number > 0 and number % 2 == 0:
        sum_num += number
print(sum_num)
