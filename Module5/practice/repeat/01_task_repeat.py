# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of=1, to=100):
    import random
    list = []
    for _ in range(size):
        list.append(random.randint(of, to))
    return list


print(gen_list(15))
