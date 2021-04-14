# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

# TODO: your code here
def can_triangle(p1, p2, p3):
    d12, d13 = p2[0] - p1[0], p3[0] - p1[0]
    if d12 == 0 or d13 == 0:
        return d12 != d13
    is_one_line = ((p2[1] - p1[1]) / d12 == (p3[1] - p1[1]) / d13)
    return not is_one_line

def distance(x1, y1, x2, y2):
    return ( (x2 - x1)**2 + (y2 - y1)**2 )**0.5

def triangle_perimeter(p1, p2, p3):
    if not can_triangle(p1, p2, p3):
        print("Not a triangle")
        return 0
    p = distance(p1[0], p1[1], p2[0], p2[1]) + distance(p1[0], p1[1], p3[0], p3[1]) + distance(p2[0], p2[1], p3[0], p3[1])
    return p

def triangle_square(p1, p2, p3):
    if not can_triangle(p1, p2, p3):
        print("Not a triangle")
        return 0
    p = triangle_perimeter(p1, p2, p3) / 2
    d12 = distance(p1[0], p1[1], p2[0], p2[1])
    d13 = distance(p1[0], p1[1], p3[0], p3[1])
    d23 = distance(p2[0], p2[1], p3[0], p3[1])
    return ( p * (p - d12) * (p - d13) * (p - d23) ) **0.5


# Не забудьте протестировать вашу функцию
print(triangle_perimeter((1,1),(2,2),(3,3)))
print(triangle_perimeter((0,0),(3,0),(0,4)))

print(triangle_square((1,1),(2,2),(3,3)))
print(triangle_square((0,0),(3,0),(0,4)))
