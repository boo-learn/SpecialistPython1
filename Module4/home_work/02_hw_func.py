# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)

def min_segment (a, b, c):
   segments = list(zip(('AB','BC','AC'), (distance(*(a+b)), distance(*(b+c)),distance(*(a+c)))))
   min_lenght = min(segments[0][1], segments[1][1], segments[2][1])
   for seg in segments:
       if seg[1] == min_lenght:
           return seg[0]

a = (-20, 12)
b = (14, 18)
c = (12, -12)

print("Самый короткий отрезок: ",min_segment (a, b, c))   # Выводим название отрезка, например “АС”.
