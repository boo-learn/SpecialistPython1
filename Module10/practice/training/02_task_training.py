# На числовой прямой расположены точки A, B, C и D.
# Напишите программу, которая выведет, во сколько раз отрезок AB больше, чем отрезок CD.
# Формат входных данных:
# На вход программе подается четыре целых числа A, B, C и D.
# Расположение точек относительно друг друга на координатной прямой произвольное.
# Формат выходных данных:
# Выведите, во сколько раз отрезок AB больше, чем отрезок CD. Ответ введите с точностью до 6-ти знаков после запятой.

n = 4
points = []
while n:
    list_points = ['0', 'D', 'C', 'B', 'A']
    try:
        points.append(float(input(f'Введит точку {list_points[n]}: ')))
        n -= 1
    except (ValueError, TypeError):
        print('необходимо ввести число')

ab = abs(points[0] - points[1])
cd = abs(points[2] - points[3])
total = round(ab / cd, 6)
print(f'Отрезок АВ больше отрезка CD в {total} раз')
