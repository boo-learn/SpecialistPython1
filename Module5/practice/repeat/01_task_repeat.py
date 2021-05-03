# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.
import random


def gen_list(size, of, to):
    res = []
    for _ in range(size):
        res.append(random.randint(of, to))
    return res


print(gen_list(10, -10, 10))
