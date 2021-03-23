# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of, to):
    import random
    ret_list = []
    for _ in range(size):
        ret_list.append(random.randint(of, to))
    return ret_list

print(gen_list(20, -2, 6)
