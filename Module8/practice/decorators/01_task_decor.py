# Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
# Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
# ********
# *Привет*
# ********
# ****
# *23*
# ****
# (кол-во звездочек зависит от длины возвращаемого значения)
def new_decorator(function_to_decorate):
    def wrapper(*args):
        # print("Я - код, который отработает до вызова функции")
        # function_to_decorate()  # Сама функция

        lst = list(function_to_decorate())
        leng = len(lst)
        out = []
        for _ in lst:
            out.append('*')

        print(str(out))
        print(function_to_decorate())
        print(str(out))

        # print("А я - код, срабатывающий после")

    return wrapper


# Вот так просто мы можем декорировать любую функцию
@new_decorator
def simple_function(text):
    return text
#
#
# # Вызываем декорируемую функцию:
text = input('Введите слово:')
simple_function(text)
