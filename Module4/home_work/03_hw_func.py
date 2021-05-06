# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def in_circle(ca, ra, cb, rb):
    small_r = (ra + rb - abs(ra - rb)) / 2
    big_r = ra + rb - small_r
    return big_r > distance(*ca, *cb) + small_r


c1 = (10, 12)
c2 = (14, 18)
r1 = 20
r2 = 10
# r2 = 15
if in_circle(c1, r1, c2, r2):
    print("Одна окружность находится целиком внутри другой")
else:
    print("Одна окружность не находится целиком внутри другой")
