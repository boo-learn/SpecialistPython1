# Напишите функцию принимающую на вход целое числом n. И возвращающую список из n элементов.
# заполненный случайными целыми числами в диапазоне от a до b.
# Примечание: все элементы списка должны быть гарантировано уникальными(неповторяющимися)
# Если создать список с заданными параметрами невозможно - функция должна выбросить ислючение
import random


def gen_list(count, start, stop):
    data = []
    try:
        if (stop - start) < count:
            raise ValueError
        while len(data) < count:
            rand_value = random.randrange(start, stop)
            if data.count(rand_value) == 0:
                data.append(rand_value)
        return data
    except ValueError:
        print("Невозможно создать такой список")
        return None


print(gen_list(89, 1, 90))

print(gen_list(90, 1, 90))
