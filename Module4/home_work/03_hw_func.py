# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


def is_circle_inside(center1, r1, center2, r2):
    op1 = (distance(*center1, *center2))
    op2 = abs(r2 - r1)
    return (distance(*center1, *center2)) < abs(r2 - r1)


p1 = (0, 0)
r1 = 2
p2 = (0, 1)
r2 = 0.5
print(is_circle_inside(p1, r1, p2, r2))

p1 = (0, 0)
r1 = 2
p2 = (0, 1)
r2 = 1
print(is_circle_inside(p1, r1, p2, r2))
