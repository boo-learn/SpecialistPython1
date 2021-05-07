# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random
def gen_list(size, of, to):
# pass
    numbers = []
    for _ in range(size):
        numbers.append(random.randrange(of, to))
    return numbers

of = int(input("of:"))
to = int(input("to:"))
size = int(input("size:"))
res = gen_list(size, of, to)
print(res)
