# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# TODO: your code here
def min_segments(**kwargs):
    min_arg = min(kwargs.values())
    for key, value in kwargs.items():
        if value == min_arg:
            return key


a = (1, 1)
b = (1, 4)
c = (1, 2)
min_segment = min_segments(AB=distance(*a, *b), AC=distance(*a, *c), BC=distance(*a, *c))

print("Самый короткий отрезок:", min_segment)  # Выводим название отрезка, например “АС”.
