# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random
def gen_list(size, of, to):
    numbers = []
    for i in range(size):
        r = random.randint(of, to)
        numbers.append(r)
    return numbers

