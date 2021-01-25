
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# Функция получения дроби из строки
def get_num(in_str):
    num_list = in_str.split() # разделить по пробелу
    numerator = 0
    denominator = 0

    if len(num_list) == 2:           # если есть целая часть
        numerator = int(num_list[0])
        fraction_list = num_list[1].split('/')
    else:
        fraction_list = num_list[0].split('/')

    fraction_list = [int(i) for i in fraction_list]
    numerator = numerator * fraction_list[1] + fraction_list[0]
    denominator = fraction_list[1]

    return [numerator, denominator]

#in_str = input('Введите выражение:') # Пользовательский ввод

#Тестовые значения:
#in_str = '1/2 + 2 3/4'   # Не полная запись (сложение)
#in_str = '1 1/2 + 3/4'   # Не полная запись (сложение)
#in_str = '1 1/2 + 2 3/4' # Полная запись (сложение)

in_str = '1 1/2 - 2 3/4'  # Полная запись (вычитание)

operation_sign = '-'
members_list = in_str.split(' + ')

# Определение знака операции
if len(members_list) == 2:
    operation_sign = '+'
else:
    members_list = in_str.split(' - ')

# Получение дробей
fract_1 = get_num(members_list[0])
fract_2 = get_num(members_list[1])

# Отладка
#print(fract_1, fract_2)

res_denominator = fract_1[1] * fract_2[1] # Получение знаменателя

if operation_sign == '+':                 # Получение числителя
    res_numerator = fract_1[0]*fract_2[1] + fract_2[0]*fract_1[1]
else:
    res_numerator = fract_1[0]*fract_2[1] - fract_2[0]*fract_1[1]

full_part = int(res_numerator / res_denominator)  # Выделение целой части (// не подходит для отрицательных чисел)

# Отладка
#print('Дробь перед выделением целой части:', res_numerator, '/', res_denominator)
#print('Целая часть:', full_part)

print('Результат:',end=' ')
if full_part != 0:
    print(full_part, end=' ')
    res_numerator = res_numerator - (full_part * res_denominator) # Если есть целая часть, то нужно упростить числитель (операция % не годится для отрицательных чисел)
    if res_numerator < 0:
        res_numerator *= -1

print(res_numerator, '/', res_denominator)


