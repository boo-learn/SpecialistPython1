# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def triangle(p1, p2, p3):
    ab = distance(*p1, *p2)
    bc = distance(*p2, *p3)
    ac = distance(*p1, *p3)
    if ab - bc < 0 and ab - ac < 0:
        #return ab
        return "AB"
    if bc - ac < 0 and bc - ab < 0:
        #return bc
        return "BC"
    #return ac
    return "AC"

p1, p2, p3 = ((10, 15), (12, 15), (13, 15))
#print(triangle(p1, p2, p3))

print("Самый короткий отрезок:", triangle(p1, p2, p3))
