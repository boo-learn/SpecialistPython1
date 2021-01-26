
# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

#if line.strip().isdigit():
#    num_array.append(int(line))

# Функция распознавания только положительных целых чисел
def get_num(line):
    return int(line) if line.strip().isdigit() else 0

# Функция распознавания все чисел
def get_num_exp(line):
    try:
        return int(line)
    except ValueError:
        return 0

# Функция работы с файлом
def get_nums_from_file(f_path, foo):
    ret_result =[]
    with open(f_path, "r") as f:
        for line in f:
             ret_result.append(foo(line))
    return ret_result

# Решение
num_array = get_nums_from_file('data/info.txt', get_num)
print("Сумма всех положительных целых чисел:", sum(num_array))
num_array = get_nums_from_file('data/info.txt', get_num_exp)
print("Сумма всех целых чисел:", sum(num_array))
