# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def size_tib(p1, p2, p3):
  AB = distance(*p1, *p2)
  AC = distance(*p1, *p3)
  BC = distance(*p2, *p3)
  if AB < AC and AB < BC:
    return "Min Size AB:", AB
  elif  AC < AB and AC < BC:
    return "Min Size AC:", AC
  else: return "Min Size AB:", BC


# TODO: your code here
print(size_tib((10, 5), (14, 22), (2, 12)))
print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
