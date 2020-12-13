# Даны координаты двух точек на плоскости.
# Напишите функцию нахождения расстояния между двумя точками.

import math
def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print(d)



# Тестируем функцию
print(distance(2, 4, 2, 9))
print(distance(12, 8, 12, -9))
print(distance(23, 0, 15, 32))
