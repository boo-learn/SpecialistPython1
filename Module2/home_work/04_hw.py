# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести стороны символами # (см. пример)

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

n = int(input("n: "))

# upper horizontal
i = 1
str = "#"
while i < n:
    str = str + "#"
    i = i+1
print(str)

# horizontals
j = 2
while j < n: #looper for horizontals
    str = "#"
    i = 2
    while i < n: #looper for backspaces within one line
        str = str + " "
        i = i+1
    str = str + "#"
    print(str)
    j = j+1

# lower horizontal
i = 1
str = "#"
while i < n:
    str = str + "#"
    i = i+1
print(str)
