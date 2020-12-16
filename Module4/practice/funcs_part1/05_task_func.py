# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def can_triangle(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p3, *p2)
    c = distance(*p1, *p3)
    return (c < a + b) and (b < a + c) and (a < b + c)


def perimeter(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p3, *p2)
    c = distance(*p1, *p3)
    return a + b + c


def area(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p3, *p2)
    c = distance(*p1, *p3)
    p = perimeter(p1, p2, p3)
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


# TODO: your code here
a = (2, 12)
b = (3, 3)
c = (4, 4)
abc_perimeter = perimeter(a, b, c) if can_triangle(a, b, c) else 'can`t make triangle'
abc_area = area(a, b, c) if can_triangle(a, b, c) else 'can`t make triangle'

print('area',abc_area)
print('perimeter',abc_perimeter)
# Не забудьте протестировать вашу функцию
