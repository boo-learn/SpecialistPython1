# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def min_len(dict_sides):
    min_val = dict_sides['sides'][0]
    for side in dict_sides['sides']:
        if side['val'] < min_val['val']:
            min_val = side
    return min_val


a, b, c = (0, 12), (11, 0), (0, 0)
sides = {}
sides.update(
    {
        'sides': [{'name': 'AB', 'val': distance(*a, *b)},
                  {'name': 'AC', 'val': distance(*a, *c)},
                  {'name': 'BC', 'val': distance(*b, *c)}]
    }
)

print(f"Самый короткий отрезок: {min_len(sides)['name']}")
