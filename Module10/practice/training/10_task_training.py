# Напишите функцию принимающую на вход целое числом n. И возвращающую список из n элементов.
# заполненный случайными целыми числами в диапазоне от a до b.
# Примечание: все элементы списка должны быть гарантировано уникальными(неповторяющимися)
# Если создать список с заданными параметрами невозможно - функция должна выбросить ислючение

import random

def fill_uniq_random(n, a, b):
    if b < a:
        raise Exception(f"Некорретный диапазон случайных значений: от {a} до {b} (b < a)")

    range_length = (b - a) + 1

    if range_length < n:
        raise Exception(f"Диапазон случайных значений {range_length} (от {a} до {b}) меньше длины списка {n}")
    
    values = []

    for i in range(n):
        rand_int = get_uniq_random(values, a, b)
        values.append(rand_int)

    return values

def get_uniq_random(values, a, b):
    while True:
        rand_int = random.randint(a, b)
        if rand_int not in values:
            return rand_int

n = int(input("Введите n: "))
a = int(input("Введите a: "))
b = int(input("Введите b: "))

result = fill_uniq_random(n, a, b)

print(result)
