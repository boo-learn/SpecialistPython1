# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

def try_parse_int(s):
    try:
        return int(s)
    except ValueError:
        return 0

total = 0
try:
    with open("data/info.txt", "r") as f:
        for line in f: total += try_parse_int(line.strip())
except Exception as e:
    print(e)
