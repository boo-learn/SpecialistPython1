# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def point_in_circle(x, y, xc, yc, r):
    dist=distance(x,y,xc,yc)
    rad=distance(xc+r,yc+r,xc,yc)
    return dist<rad
    pass

def distance(x1, y1, x2, y2):
    return ((y2 - y1) ** 2 + (x1 - x2) ** 2) ** 0.5
    pass

# Не забудьте протестировать вашу функцию
