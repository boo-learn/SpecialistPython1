# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:


def distance(x1, y1, x2, y2):
    # в своем модуле я импортирую функцию
    total = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return total


def point_in_circle(x, y, xc, yc, r):
    def point_in_circle(x, y, xc, yc, r):
    # надо найти расстояние от центра до точки и сравнить в r
    s = distance(x, y, xc, yc)
    return r > s


print(point_in_circle(3, 3, 0, 0, 1))
print(point_in_circle(1, 1, 0, 0, 2))
