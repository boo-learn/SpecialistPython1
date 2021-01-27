# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def point_in_circle(x, y, xc, yc, r):
    # TODO: your code here
    dist_to_circle = distance(x, y, xc, yc)
    return not dist_to_circle >= r

print(point_in_circle(1, 1, 20, 31, 19))
