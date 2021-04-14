# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5
Xa = int(input('Введите координату Xa: ' ))
Ya = int(input('Введите координату Ya: ' ))
Xb = int(input('Введите координату Xb: ' ))
Yb = int(input('Введите координату Yb: ' ))
Xc = int(input('Введите координату Xc: ' ))
Yc = int(input('Введите координату Yc: ' ))

AB = distance (Xa,Ya,Xb,Yb)
BC = distance (Xb,Yb,Xc,Yc)
AC = distance (Xa,Ya,Xc,Yc)

if AB+BC>AC and AB+AC>BC and BC+AC>AB:
    if AB<BC and AB<AC:
        print ('Наименьшая сторона AB')
    elif BC<AB and BC<AC:
        print ('Наименьшая сторона BC')
    else:
        print ('Наименьшая сторона AC')


# TODO: your code here
print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
