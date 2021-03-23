# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of, to):
    import random as rd
    rnd = []
    for i in range(size):
        rnd_el = rd.randint(of, to)
        rnd.append(rnd_el)

    return rnd

print(gen_list(10, 1, 10))
print(gen_list(5, 1, 3))
print(gen_list(20, 1, 100))
