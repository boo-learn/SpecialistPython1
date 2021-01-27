# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random

def gen_list(size, of, to):
    list = []
    while size != 0:
        list.append(random.randint(of, to))
        size -= 1
    return list

print(gen_list(10, -6, 15))
