# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random

list_int = [random.randint(-10, 10) for _ in range(10)]

positive_numbers = [el for el in list_int if el >= 0]
even_numbers = [el for el in list_int if el % 2 == 0]

print(list_int)
print('список положительных чисел: ', positive_numbers)
print(f'Кол-во положительных элементов: {len(positive_numbers)}')
print(f'Сумма положительных элементов: {sum(positive_numbers)}')
print('список четных чисел: ', even_numbers)
print(f'Среднее четных чисел: {sum(even_numbers)/len(even_numbers)}')
