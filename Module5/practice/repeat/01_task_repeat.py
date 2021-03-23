# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.


import random


def gen_list(size, of, to):
    i = 0
    rand_list = []
    while i < size:
        rand_list.append(random.randint(of, to))
        i += 1
    return rand_list

print(gen_list(10, 1, 5))
print(gen_list(3, -1, 1))
print(gen_list(7, 0, 135))
print(gen_list(25, -10, 10))
