# Вывод символов по диагоналям
# Даны сторона квадрата. Вывести его диагонали символами #.
# Формат входных данных: На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных: Требуется вывести диагонали символами # (см. примеры)
# Примеры:
# a = 6
#    #
 #  #
  ##
  ##
 #  #
#    #

# a = 3
# #
 #
# #

a = int(input('a = '))
i = 0
j = 0
for i in range(a):
    diagonal = ''
    for j in range(a):
        if i == j or i == a - j - 1:
            diagonal += '#'
        else:
            diagonal += ' '
        j += 1
    print(diagonal)
    i += 1
