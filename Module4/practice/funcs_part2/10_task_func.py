# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов


    
def average(*args):
    i = 0
    sum_args = 0
    for arg in args:
        sum_args += arg
        i += 1
    mid_sum = sum_args / i
    return mid_sum



print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
