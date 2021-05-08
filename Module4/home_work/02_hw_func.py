# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1)*2 + (y2 - y1)**2)**0.5

xa, ya = 4, 6
pa = xa, ya
xb, yb = 2, -6
pb = xb, yb
xc, yc = -2, 12
pc = xc, yc

def min_length(pa, pb, pc):
    ab = distance(*pa, *pb)
    bc = distance(*pb, *pc)
    ac = distance(*pc, *pa)
    if ab <= bc and ab <= ac:
        return 'AB'
    elif bc <= ab and bc <= ac:
        return 'BC'
    else:
        return 'AC'
print("Самый короткий отрезок:", min_length(pa, pb, pc)  # Выводим название отрезка, например “АС”.
