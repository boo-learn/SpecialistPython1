# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов

def average(*args):
    avg = 0
    i = 0
    for num in args:
        avg += num
        i += 1
    avg = avg / i
    return avg


print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
print(average(2, 2, 2))
