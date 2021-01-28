# Даны два уравнения прямых вида у=kx+b и виде строки. Проверить, пересекаются ли данные прямые?
# Примеры уравнений: "y = 2x + 4"  "y = -12x -12"

# Проверьте входные данные на корректность

# Функция удаляющая все пробелы из строки
def del_spaces(in_data: str):
    return ''.join(in_data.split())

# Функция проверяющая корректность уравнения ( без пробелов )
# В случае успешной проверки возвращает k:int
def check_equation(in_data: str):
    # Проверка первых двух символов 'y='
    if in_data[0] != 'y' and in_data[1] != '=':
        raise ValueError

    # Проверка на наличие x
    x_index = in_data.find('x')
    if x_index == -1:
        raise ValueError

    # Проверка что k это число
    k = in_data[2:x_index]
    if len(k) == 0:    # Если уравнение вида y=x+b
        k = 1
    elif len(k) == 1 and k[0] == '-': # Если уравнение вида y=-x+b
        k = -1
    else:
        k = float(k)       # Если k не число то float вывалит exception

    # Проверка что b это число
    if in_data[x_index] != in_data[-1]:  # Если x это не конец строки
        b = in_data[x_index+1:]
        b = float(b)      # Если b не число то float вывалит exception

    return int(k)

# Функция проверяющая что прямые параллельны (Через декоратор!!!)
def parallel_lines_decorator(foo):
    def wrapper(a, b):
        if foo(a, b):
            print('Линии параллельны!!!')
        else:
            print('Линии пересекаются!!!')
    return wrapper

# Собственно проверка
@parallel_lines_decorator
def check_parallel_lines_by_k(k_1, k_2):
    return True if k_1 == k_2 else False


while True:
    in_str_1 = input("Введите первое уравнение: ")
    in_str_2 = input("Введите второе уравнение: ")

    try:
        k1 = check_equation(del_spaces(in_str_1))
        k2 = check_equation(del_spaces(in_str_2))
    except ValueError as err:
        print("Ошибка данных", err)
    except Exception as err:
        print("Непредвиденная ошибка", err)
    else:
        break

check_parallel_lines_by_k(k1, k2)
