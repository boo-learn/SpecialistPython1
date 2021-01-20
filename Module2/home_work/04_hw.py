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
sq_len = int(input('Введите длину стороны квадрата: '))

width_len = height_len = 0

while height_len < sq_len:
    if height_len == 0 or height_len == sq_len - 1:
        block_texture = '#'
    else:
        block_texture = ' '
    side = ''
    width_len = 0
    while width_len < sq_len:
        if width_len == 0 or width_len == sq_len - 1:
            side += '#'
        else:
            side += block_texture
        width_len += 1
    height_len += 1
    print(side)
