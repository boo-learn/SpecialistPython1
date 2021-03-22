# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)


def point_in_circle(x, y, xc, yc, r):
    return distance(x, y, xc, yc) < r


# Не забудьте протестировать вашу функцию
_xc = 0
_yc = 0
_r = 2
_x = 0
_y = 3
print(point_in_circle(_x, _y, _xc, _yc, _r))
