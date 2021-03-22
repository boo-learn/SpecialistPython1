# Используя функцию average() из предыдущей задачи, найдите среднее арифметическое всех элементов списка и кортежа

def average(*args):
    i = 0
    summ = 0
    for el in args:
        summ = summ + args[i]
        i += 1
    return summ/i

def gen_list(size, at=-10, to=10):
    import random  # импорт в функции возможен, но не рекомендуется PEP-8
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(at, to))
    return result_list

my_list = gen_list(10)
my_tuple = 5, 7, -4, 10, 8

print ("List: ", my_list)
print ("Tuple: ", my_tuple)
print ("Average: ", average(*my_list, *my_tuple))
