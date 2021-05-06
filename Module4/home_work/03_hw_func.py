# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def is_circumference_inside(c1, c2, r1, r2):
    return r1 + distance(*c1, *c2) < r2


c1 = 0, 0
c2 = 1, 1
r1 = 2
r2 = 3

print(is_circumference_inside(c1, c2, r1, r2))
