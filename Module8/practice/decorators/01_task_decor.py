# Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
# Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
# ********
# *Привет*
# ********
# ****
# *23*
# ****
# (кол-во звездочек зависит от длины возвращаемого значения)
def dec_func(func):
    def wrapper():
        print("*"*(len(func())+2))
        print("*{}*".format(func()))
        print("*" * (len(func()) + 2))
    return wrapper

@dec_func
def hello_base():
    return "Привет"

hello_base()
