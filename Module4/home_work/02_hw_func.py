# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5
A = [0,0]
B = [0,1]
C = [10,1]

def minimal_side(**kwargs):
    m_side = min(kwargs.values())
    for key, value in kwargs.items():
        if value == m_side:
            return key

m_side = minimal_side(AB=distance(*A, *B), BC = distance (*B,*C), AC = distance (*C,*A))
print (f'наименьшая сторона: {m_side}')
