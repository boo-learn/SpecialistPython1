# Напишите функцию принимающую на вход целое числом n. И возвращающую список из n элементов.
# заполненный случайными целыми числами в диапазоне от a до b.
# Примечание: для генерации случайного числа используйте import random

import random

def fill_random(n, a, b):
    values = []
    for i in range(n):
        rand_int = random.randint(a, b)
        values.append(rand_int)
    return values

# То же самое, но через генератор:
def gen_random(n, a, b):
    return [random.randint(a, b) for i in range(n)]

n = int(input("Введите n: "))
a = int(input("Введите a: "))
b = int(input("Введите b: "))

result = fill_random(n, a, b)

# Раскомментировать, если нужно сделать через генератор:
#result = gen_random(n, a, b)

print(result)
