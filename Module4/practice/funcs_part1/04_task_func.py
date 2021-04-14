# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
    is_one_line = ((p2[1] - p1[1]) / (p2[0] - p1[0]) == (p3[1] - p1[1]) / (p3[0] - p1[0]))
    return not is_one_line

print( can_triangle((10, 12), (14, 18), (12, 12)) )
print( can_triangle((1, 1), (2, 2), (12, 12)) )

# Не забудьте протестировать вашу функцию
