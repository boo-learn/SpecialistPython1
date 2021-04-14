# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of, to):
    pass

import random
def gen_list(size = 10, of = -10, to = 10):
    new_list = []
    for _ in range(size):
        new_list.append(random.randint(of, to))
    return new_list

print(gen_list())
