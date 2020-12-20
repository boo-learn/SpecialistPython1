# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.
import math

def distance(x1, y1, x2, y2):
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

def cmp_line(ab,bc,ca):
    if ab<bc and ab<ca:
        return('ab',ab)
    elif bc<ab and bc<ca:
        return ('BC', bc)
    else:
        return ('CA',ca)

print("Самый короткий отрезок:", cmp_line(distance(1,0,2,7), distance(2,7,7,0), distance(1,0,7,0)))
