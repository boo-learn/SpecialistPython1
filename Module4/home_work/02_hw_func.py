# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(xa, ya, xb, yb, xc, yc):
    shortest = ''
    ab = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
    bc = ((xb - xc) ** 2 + (yb - yc) ** 2) ** 0.5
    ac = ((xa - xb) ** 2 + (xc - yc) ** 2) ** 0.5
    if ab < bc and ab < ac:
        shortest = 'AB'
    if bc < ac:
        shortest = 'BC'
    shortest = 'AC'
    return shortest


print("Самый короткий отрезок:", distance(5, 3, 1, 1.4, 8, 4))
