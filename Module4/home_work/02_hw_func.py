# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def minimal_len(*args):
    min_len = args[0]
    for arg in args:
        if arg['lnt'] < min_len['lnt']:
            min_len = arg
    return min_len


a = (10, 12)
b = (14, 18)
c = (12, 12)
ab = {'name': 'AB', 'lnt': distance(*a, *b)}
bc = {'name': 'BC', 'lnt': distance(*b, *c)}
ac = {'name': 'AC', 'lnt': distance(*a, *c)}
print(f"Самый короткий отрезок: {minimal_len(ab, bc, ac)['name']}")  # Выводим название отрезка, например “АС”.
