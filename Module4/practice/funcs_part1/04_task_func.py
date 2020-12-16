# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def can_triangle(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p3, *p2)
    c = distance(*p1, *p3)
    return (c < a + b) and (b < a + c) and (a < b + c)


# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))

print(can_triangle((1, 1), (2, 2), (3, 3.5)))
print(can_triangle((1, 1), (2, 2), (3, 3)))
# Не забудьте протестировать вашу функцию
