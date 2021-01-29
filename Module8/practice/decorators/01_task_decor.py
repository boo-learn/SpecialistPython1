# Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
# Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
# ********
# *Привет*
# ********
# ****
# *23*
# ****
# (кол-во звездочек зависит от длины возвращаемого значения)
def dunc_dec(func):
    def wrapper():
        print((len(func())+2)*"*")
        print("*"+func()+"*")
        print((len(func()) + 2) * "*")
    return wrapper

@dunc_dec
def func():
    return "Qwerty!@#$%"

func()
