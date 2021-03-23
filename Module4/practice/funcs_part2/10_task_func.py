# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов


def average(*args):
    div = 0
    total = 0
    for arg in args:
        total = total + arg
        div += 1
    return total / div


print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
