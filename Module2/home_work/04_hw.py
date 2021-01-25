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
square_side = int(input('enter square side value: '))

line_counter = 1
while line_counter <= square_side:
    column_counter = 1
    string = ''
    if (line_counter == 1 or line_counter == square_side):
        while column_counter <= square_side:
            string += '#'
            column_counter += 1
    else:
        while column_counter <= square_side:
            if column_counter == 1 or column_counter == square_side:
                string += '#'
            else:
                string += ' '
            column_counter += 1
    print(string)
    line_counter += 1
