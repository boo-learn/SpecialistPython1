# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой
def distance(x1, y1, x2, y2):
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

coord1 = (2, 2)
coord2 = (5, 5)

r1 = 2
r2 = 4

d = round((distance(*coord1, *coord2)), 2)

def is_circle1_inside_circel2(l, r1, r2):
    small_r = r1
    big_r = r2
    if r2 < r1:
        small_r = r2
        big_r = r1

    return small_r + l <= big_r

if is_circle1_inside_circel2(d, r1, r2):
    print("Один кружочек внутри другого кружочка")
else:
    print("Окружности кружочков пересеклись")
