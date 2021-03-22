# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def can_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True


x1 = int(input("x1:"))
y1 = int(input("y1:"))

x2 = int(input("x2:"))
y2 = int(input("y2:"))

x3 = int(input("x3:"))
y3 = int(input("y3:"))

a = distance(x1,y1,x2,y2)
b = distance(x2,y2,x3,y3)
c = distance(x3,y3,x1,y1)

if can_triangle(a,b,c):
    print("треугольник")
else:
    print("не треугольник")

# Не забудьте протестировать вашу функцию
