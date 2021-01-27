# Даны два уравнения прямых вида у=kx+b и виде строки. Проверить, пересекаются ли данные прямые?
# Примеры уравнений: "y = 2x + 4"  "y = -12x -12"

# Проверьте входные данные на корректность

def check_equation(in_data):
    if len(in_data) != 3 and len(in_data) != 5:
        return False
    elif in_data[0] != 'y' or in_data[1] != '=' or in_data[2].find('x') == -1:
        return False

    if len(in_data) > 3:
        if in_data[3] != '+' and in_data[3] != '-':
            return False
        elif not(in_data[4].isdigit()):
            return False

    return True

def get_x(in_str_x):
    x = in_str_x.strip('x')
    if len(x) == 0:
        return [True, 1]
    elif len(x) == 1 and x[0] == '-':
        return [True, -1]

    if x[0] == '-':
        x = x[1:]
        minus = True
    else:
        minus = False

    if x.isdigit():
        x = int(x)
        return [True, (-1)*x if minus else x]

    return [False, x]

def get_const(sign, number):
    return (-1)*int(number) if sign == '-' else int(number)

def get_data_from_equation(in_data):
    if not check_equation(in_data):
        raise ValueError('Неверный формат введённых данных')
    x = get_x(in_data[2])
    if x[0] is False:
        raise ValueError('Неверный формат для X')
    if len(in_data) == 5:
        const = get_const(in_data[3], in_data[4])
    else:
        const = 0

    return [x[1], const]

while True:
    #in_data_1 = 'y = x - 34'.split()
    #in_data_2 = 'y = -x + 6'.split()
    in_data_1 = input("Введите первое уравнение: ").split()
    in_data_2 = input("Введите второе уравнение: ").split()
    try:
        eq_1 = get_data_from_equation(in_data_1)
        eq_2 = get_data_from_equation(in_data_2)
    except ValueError as err:
        print("Ошибка данных", err)
    except Exception as err:
        print("Непредвиденная ошибка", err)
    else:
        break
        
print(eq_1)
print(eq_2)
if eq_1[0] != 0 and eq_2[0] != 0:
    if eq_1[0] - eq_2[0] == 0:
        print('Линии параллельны')
    else:
        x = (eq_1[1] - eq_2[1]) / (eq_2[0] - eq_1[0])
        y = eq_1[0]*x + eq_1[1]
        print('Линии пересекаются в точке:',  x , y)
else:
    print("Одно из уравнений не является прямой")
