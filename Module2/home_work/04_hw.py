# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести диагонали символами # (см. пример)

# Пример:
# Входные данные
# 6
# Выходные данные
######
#    #
#    #
#    #
#    #
######

a = int(input("Размер стороны квадрата: "))
s = "#"
print(s*a)
for i in range(a - 2):
    print(s,' ' * (a-4), s)
print(s*a)
