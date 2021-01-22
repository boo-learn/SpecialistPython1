# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
x3 = int(input('x3 = '))
y3 = int(input('y3 = '))

ab = distance(x1, y1, x2, y2)
bc = distance(x2, y2, x3, y3)
ac = distance(x1, y1, x3, y3)

min_name = ''

if ab < bc and ab < ac:
    min_name = 'AB'
elif bc < ab and bc < ac:
    min_name = 'BC'
else:
    min_name = 'AC'
print("Самый короткий отрезок:", min_name)  # Выводим название отрезка, например “АС”.
