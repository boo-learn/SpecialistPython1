# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

numbers = []

with open("data/info.txt", "r", encoding='UTF-8') as f:
    for line in f:
        line = line.replace("\n", "")
        if line.isdigit():
            line = int(line)
            numbers.append(line)

# print(numbers)
print(sum(numbers))

