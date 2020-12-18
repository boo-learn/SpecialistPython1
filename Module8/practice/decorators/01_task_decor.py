# Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
# Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
# ********
# *Привет*
# ********
# ****
# *23*
# ****
# (кол-во звездочек зависит от длины возвращаемого значения)

def stars(function_to_decorate):
    def wrapper():
        stroke = list(function_to_decorate().split(" "))
        for el in stroke:
            print('*'*len(str(el))+'**')
            print(f'*{el}*')
            print('*' * len(str(el)) + '**')
        return

    return wrapper

@stars
def re_line():
    return input()


re_line()
