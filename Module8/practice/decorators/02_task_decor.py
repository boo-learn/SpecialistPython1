# Напишите функцию декоратор, которая округляет значение декорируемой функции до двух знаков после  запятой.
# Если округление невозможно, например там строка, или не требуется(целое число) то оставляем результат без изменений.
# Примечание: используйте встроенную функцию round()

import random

def float_decorator(foo):
    def wrapper(data):
        try:
            result = round(foo(data), 2)
            return result if len(str(data)) > len(str(result)) else data
        except ValueError:
            print('Ошибка преобразования!')
            return data

    return wrapper

@float_decorator
def get_float(in_data):
    return float(in_data)

print(get_float('aerw'))
print(get_float(42))
print(get_float('42'))
print(get_float(42.4242))
print(get_float('-42.4242'))
