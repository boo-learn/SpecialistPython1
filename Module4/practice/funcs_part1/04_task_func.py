# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
def can_triangle(p1, p2, p3):
    r1 = distance(p1[0], p1[1], p2[0], p2[1])
    r2 = distance(p1[0], p1[1], p3[0], p3[1])
    r3 = distance(p3[0], p3[1], p2[0], p2[1])
    return r1+r2>r3 and r1+r3>r2 and r2+r3>r1
    pass


def distance(x1, y1, x2, y2):
    # TODO: your code here
    return ((y2 - y1) ** 2 + (x1 - x2) ** 2) ** 0.5
    pass


# Пример вызова функции
print(can_triangle((10, 12), (14, 18), (12, 12)))

# Не забудьте протестировать вашу функцию
