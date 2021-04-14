# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона


def distance(x1, y1, x2, y2):
    total = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return total

  
def can_triangle(p1, p2, p3):
    # прямая проходит через точки p1 и p2
    # лежит ли p3 на этой прямой?
    total = (p3[0]-p1[0]) * (p2[1]-p1[1]) - (p2[0]-p1[0])*(p3[1]-p1[1])
    if total == 0:
        return False
    return True

  
def size_triangle(p1, p2, p3):
    if p_04.can_triangle(p1, p2, p3) is False:
        return False
    side1 = distance(p1[0], p1[1], p2[0], p2[1])
    side2 = distance(p1[0], p1[1], p3[0], p3[1])
    side3 = distance(p2[0], p2[1], p3[0], p3[1])
    perimeter = side1 + side2 + side3
    perimeter_half = perimeter / 2
    area = (perimeter_half * (perimeter_half - side1) * (perimeter_half - side2) * (perimeter_half - side3)) ** 0.5
    return perimeter, area


triangle = size_triangle((10, 12), (14, 18), (12, 12))
print(f'Периметр = {round(triangle[0],2)}, площадь = {round(triangle[1],2)}')
triangle = size_triangle((10, 10), (5, 5), (1, 1))
print(triangle)
