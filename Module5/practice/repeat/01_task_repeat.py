# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random

def gen_list(size, of, to):
    list = []
    i = 0
    while i <= size:
        element = random.randrange(of, to)
        list.append(element)
        i += 1
    return list

print(gen_list(10, 0, 100))
