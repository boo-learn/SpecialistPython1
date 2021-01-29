# Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
# Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
# ********
# *Привет*
# ********
# ****
# *23*
# ****
# (кол-во звездочек зависит от длины возвращаемого значения)

def decorator(function_to_decorate):
    def wrapper():
        print('*' * (len(function_to_decorate()) + 2))
        res = function_to_decorate()
        print(f'*{res}*')  # Сама функция
        print('*' * (len(function_to_decorate()) + 2))

    return wrapper


@decorator
def function():
    # print('asasas')
    return 'asasas'


# # Вызываем декорируемую функцию:
function()

# new_decorator(simple_function)()
