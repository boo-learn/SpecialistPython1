# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

from random import randint

def gen_list(size, of, to):
    l = []
    for _ in range(size): l.append(randint(of, to))
    return l

