# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

numbers = [2, -5, 8, 9, -25, 25, 4]

if 0:
    sqrt_numbers = []
    for num in numbers:
        sqrt_num = num**0.5
        if num > 0 and (round(sqrt_num) - sqrt_num) == 0:
            sqrt_numbers.append(sqrt_num) 
    print(sqrt_numbers)
#======================

if 1:
    sqrt_numbers = []
    for num in numbers:
        sqrt_num = num**0.5
        if num > 0 and sqrt_num.is_integer():
            sqrt_numbers.append(sqrt_num) 
    print(sqrt_numbers)
