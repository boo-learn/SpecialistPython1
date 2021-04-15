# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.

import math

def run():
    try:
        n, m = get_measures()
        x = count_squares(n, m)

        postfix = get_postfix(x)

        print(f'От прямоугольника {n}x{m} можно отрезать {x} квадрат{postfix} со стороной {m}.')
    except Exception as error:
        print(f'Не получилось посчитать квадраты. Возникла ошибка: {error}. Попробуем снова.')
        run()

def get_measures():
    input_str = input('Введите строку формата nxm, означающую стороны квадрата (например, 4x2): ')
    
    measures = input_str.split('x')
    
    if len(measures) == 2:
        return int(measures[0]), int(measures[1])
    else:
        print('Строка была введена в неправильном формате! Попробуйте ещё раз...')
        return get_measures()

def count_squares(n, m):
    squares = n / m
    return math.floor(squares)

def get_postfix(x):
    if x > 9 and x < 21:
        return "ов"

    remainder = x % 10

    if remainder == 1:
        return ""
        
    if remainder > 1 and remainder < 5:
        return "а"

    return "ов"

run()
