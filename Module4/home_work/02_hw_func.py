# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

A=(-2,4)
B=(4,1)
C=(4,6)
line_dict=[{
    "name":"AB",
    "dist":distance(*A,*B)
    },
    {
    "name":"BC",
    "dist":distance(*B,*C)
    },
    {
    "name":"AC",
    "dist":distance(*A,*C)
    }]
min_line=line_dict[0]
for el in line_dict:
    if el["dist"]<min_line["dist"]:
        min_line=el

# print(line_dict)

# TODO: your code here
print("Самый короткий отрезок:", min_line["name"] )  # Выводим название отрезка, например “АС”.
