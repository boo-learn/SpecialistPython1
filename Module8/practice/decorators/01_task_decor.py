# Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
# Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
# ********
# *Привет*
# ********
# ****
# *23*
# ****
# (кол-во звездочек зависит от длины возвращаемого значения)
def stars_decorator(func_to_decor):
    def wrapper():
        print("*" * (len(func_to_decor())+2))
        print("*{}*".format(func_to_decor()))
        print("*" * (len(func_to_decor())+2))
    return wrapper

@stars_decorator
def print_hello():
    return "Привет"

print_hello()
