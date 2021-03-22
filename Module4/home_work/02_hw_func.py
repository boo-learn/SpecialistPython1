# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

a1 = int(input("Please enter A coordinate x: "))
a2 = int(input("Please enter A coordinate y: "))

b1 = int(input("Please enter B coordinate x: "))
b2 = int(input("Please enter B coordinate y: "))

c1 = int(input("Please enter C coordinate x: "))
c2 = int(input("Please enter C coordinate y: "))

AB = distance(a1, a2, b1, b2)
BC = distance(b1, b2, c1, c2)
AC = distance(a1, a2, c1, c2)

print("Самый короткий отрезок:")
if AB < BC:
    if AB < AC:
        print ("AB")
    else:
        print ("AC")
elif BC < AC:
    print ("BC")

#print("Самый короткий отрезок:", min_el)  # Выводим название отрезка, например “АС”.
