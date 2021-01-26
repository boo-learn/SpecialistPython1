# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

with open("data/info.txt", "r") as f:
    sum = 0
    for line in f:
        s = line.split()
        if s[0].isnumeric():
            sum += int(s[0])

    print(sum)
