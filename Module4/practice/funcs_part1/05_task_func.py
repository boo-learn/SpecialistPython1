# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

# TODO: your code here
def can_triangle(p1, p2, p3):
    return not (p3[0] - p1[0]) * (p2[1] - p1[1]) - (p2[0] - p1[0]) * (p3[1] - p1[1]) == 0


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)

  
def triangle_perimeter(a, b, c):
    return a + b + c


def triangle_area_heron(p, a, b, c):
    p_2 = p / 2
    return (p_2 * (p_2 - a) * (p_2 - b) * (p_2 - c)) ** 0.5


p1 = (0, 0)
p2 = (0, 3)
p3 = (2, 0)
if can_triangle(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p1, *p3)
    c = distance(*p2, *p3)
    p = triangle_perimeter(a, b, c)
    print("Периметр:", p)
    print("Площадь:", triangle_area_heron(p, a, b, c))
else:
    print("Невозможно построить треугольник с ненулевой площадью")

# Не забудьте протестировать вашу функцию
