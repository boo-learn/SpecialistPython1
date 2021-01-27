# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random


def gen_list(size, of, to):
    my_list = []
    for _ in range(size):
        my_list.append(random.randint(of, to))
    return my_list


size = int(input('Размер: '))
of = int(input('Значения с: '))
to = int(input('Значения по: '))

print(gen_list(size, of, to))
