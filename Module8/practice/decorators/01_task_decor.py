# Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
# Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
# ********
# *Привет*
# ********
# ****
# *23*
# ****
# (кол-во звездочек зависит от длины возвращаемого значения)

def decor(func):
    def wrapper(*args, **kwargs):
        string = str(func(*args, **kwargs))
        print('*' * (4 + len(string)))
        print('*', string, '*')
        print('*' * (4 + len(string)))

    return wrapper()


@decor
def return_true():
    return True


@decor
def is_wrong_year(num_year):
    return not (num_year % 4 != 0 or (num_year % 100 == 0 and num_year % 400 != 0))


return_true()
is_wrong_year(2000)
