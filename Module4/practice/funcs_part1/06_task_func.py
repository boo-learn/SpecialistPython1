# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def point_in_circle(x, y, xc, yc, r):
    a = distance(x, y, xc, yc)
    if a <= r:
        return("inside")
    return("outside")

print(point_in_circle(1, 1, 0, 0, 4))

# Не забудьте протестировать вашу функцию
