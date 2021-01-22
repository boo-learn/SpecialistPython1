# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random

def gen_list(size, of, to):
    ret_list = []
    while size > 0:
        ret_list.append(random.randint(of, to))
        size -= 1
    return ret_list

print(gen_list(4, 5, 8))
