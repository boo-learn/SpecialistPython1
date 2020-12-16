# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

# TODO: your code here
def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
    # TODO: your code here
    pass

def can_triangle(p1, p2, p3):
    a=distance(*p1,*p2) #(p1[0],p1[1],p2[0],p2[1])
    b=distance(*p2,*p3) #(p2[0],p2[1],p3[0],p3[1])
    c=distance(*p3,*p1) # (p3[0],p3[1],p1[0],p1[1])
    # set_triang=list({p1p2,p2p3,p3p1})
    # print(p1p2,p2p3,p3p1)

    return a+b>c and a+c>b and b+c>a

def perimetr (a,b,c):
    return a+b+c

def area (a,b,c):
    p=(a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5

A=(2,4)
B=(2,8)
C=(8,8)
if not(can_triangle(A,B,C)):
    print("Треугольник построить нельзя")
else:
    a=distance(*A,*B)
    b=distance(*B,*C)
    c=distance(*C,*A)
    print("Периметр равен: ", perimetr(a,b,c))
    print("Площадь равна: ", area(a,b,c))
    # TODO: your code here
    pass

# Не забудьте протестировать вашу функцию
