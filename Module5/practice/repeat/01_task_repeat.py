# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.
import random

def gen_list(size, of, to):
    new_list = []
    for _ in range(size):
        new_list.append(randint(of, to))
    return new_list
