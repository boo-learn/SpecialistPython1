# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def circle(x1, y1, x2, y2, r1, r2):
    return distance(x1, y1, x2, y2) <= abs(r2 - r1)


x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
r1 = int(input('r1 = '))
r2 = int(input('r2 = '))

print(circle(x1, y1, x2, y2, r1, r2))
