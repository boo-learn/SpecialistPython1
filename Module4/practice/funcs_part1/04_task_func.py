# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle (p1,p2,p3):
    if (p1[0] == p2[0] and p1[0] == p3[0]) or (p1[1] == p2[1] and p1[1] == p3[1]):
        return('impossible')
    else:
        a = ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
        b = ((p1[0]-p3[0])**2+(p1[1]-p3[1])**2)**0.5
        c = ((p3[0]-p2[0])**2+(p3[1]-p2[1])**2)**0.5
        perimetr = a + b + c
        area = (perimetr*(perimetr-a)*(perimetr - b)*(perimetr - c)) ** 0.5
        return (perimetr, area)

print(can_triangle((10, 12), (14, 18), (12, 12)))
print(can_triangle((10, -12), (14, -18), (-12, 12)))
print(can_triangle((10, 12), (10, 18), (10, 12)))
