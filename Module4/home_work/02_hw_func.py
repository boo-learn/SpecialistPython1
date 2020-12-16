# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


a = (1, 1)
b = (2, 2)
c = (3, 3)

lst_od_dicts = [{'name': "ab", 'len': distance(*a, *b)},
                {'name': "ac", 'len': distance(*a, *c)},
                {'name': "bc", 'len': distance(*c, *b)},
                ]
print(lst_od_dicts)
lst_od_dicts.sort(key=lambda x: x['len'])

# TODO: your code here
# print("Самый короткий отрезок:", lst_od_dicts[0]['name'])  # Выводим название отрезка, например “АС”.
