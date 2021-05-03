# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
    d1 = distance(p1[0], p1[1], p2[0], p2[1])
    d2 = distance(p1[0], p1[1], p3[0], p3[1])
    d3 = distance(p2[0], p2[1], p3[0], p3[1])

    return d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# Пример вызова функции
print(can_triangle((10, 12), (14, 18), (12, 12)))

# Не забудьте протестировать вашу функцию
