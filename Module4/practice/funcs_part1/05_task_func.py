# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def correctness(x1, y1, x2, y2, x3, y3):
    if x1 == x2 == x3 or y1 == y2 == y3:
        return False
    return True


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def perimeter(x1, y1, x2, y2, x3, y3):
    if correctness(x1, y1, x2, y2, x3, y3):
        return distance(x1, y1, x2, y2) + distance(x1, y1, x3, y3) + distance(x2, y2, x3, y3)
    return 0

def aria(x1, y1, x2, y2, x3, y3):
    if correctness(x1, y1, x2, y2, x3, y3):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (y3 - y3) ** 2) ** 0.5
    return 0



print(perimeter(2, 4, 2, 9, 3, 6))
print(aria(2, 4, 2, 9, 3, 6))


# Не забудьте протестировать вашу функцию
