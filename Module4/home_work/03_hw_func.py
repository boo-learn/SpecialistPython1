# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def circle_in_circle(x1, y1, x2, y2, r1, r2):
    if r1 < r2 and distance(x1, y1, x2, y2) < r1:
        return "circle in circle"
    elif r2 < r1 and distance(x1, y1, x2, y2) < r2:
        return "circle in circle"
    else:
        return "circle not in circle"

print(circle_in_circle(1, 0.5, 1.5, 3, 4, 2))
