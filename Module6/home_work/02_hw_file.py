# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

total = 0
with open("data/info.txt", "r") as f:
    for line in f:
        # if line.strip().isdigit():
        if is_digit(line.strip()):
            # print(line)
            total += float(line.strip())
print(total)
