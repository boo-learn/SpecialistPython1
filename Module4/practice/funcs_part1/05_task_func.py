# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def can_triangle(p1, p2, p3):
    d1 = distance(*p1, *p2)
    d2 = distance(*p1, *p3)
    d3 = distance(*p2, *p3)
    return d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def perimeter(p1, p2, p3):
    d1 = distance(*p1, *p2)
    d2 = distance(*p1, *p3)
    d3 = distance(*p2, *p3)
    return d1 + d2 + d3


def square(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p1, *p3)
    c = distance(*p2, *p3)
    p = perimeter(p1, p2, p3) / 2

    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


points = ((10, 12), (14, 18), (12, 12))

if can_triangle(*points):
    print(perimeter(*points))
    print(square(*points))
else:
    print("Построить нельзя")

    # Не забудьте протестировать вашу функцию
