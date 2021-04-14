# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random
def gen_list(size, of=-10, to =10):
    rand_list = []
    for _ in range(size):
        rand_list.append(random.randint(of,to))

    return rand_list

print(gen_list(6))
