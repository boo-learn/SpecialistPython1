# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

numbers=[]

with open("data/info.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip()
        if line[0] == "-" and line[1:].isdigit() or line.isdigit():
            line = int(line)
            numbers.append(line)
print(numbers)
