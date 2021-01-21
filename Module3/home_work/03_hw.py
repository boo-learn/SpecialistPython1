# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# Для создания входных данных используем решение из предыдущей задачи
import random

n = int(input('Введите количество элементов: '))
numbers = []
i = 0
while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1
print(numbers) # Отладка

# Решение этой задачи
numbers_sum = 0
for number in numbers:
    if number > 0 and number % 2 == 0:
        numbers_sum += number
print(numbers_sum)
