# Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
# Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
# ********
# *Привет*
# ********
# ****
# *23*
# ****
# (кол-во звездочек зависит от длины возвращаемого значения)

# Это и есть функцяи декоратор
def new_decorator(function_to_decorate):
    def wrapper():
        str = function_to_decorate()  # Сама функция
        l = len(str)
        str2 = "**"
        while l > 0:
            str2 += '*'
            l -= 1
        print(str2)
        print('*'+str+'*')
        print(str2)
    return wrapper


# Вот так просто мы можем декорировать любую функцию
@new_decorator
def simple_function():
    return "Hello"
#
#
# # Вызываем декорируемую функцию:
simple_function()
