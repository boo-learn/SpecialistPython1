# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

f_list = []
digit_list = []
sum_digits = 0
with open("data/info.txt", "r", encoding="UTF-8") as f:
    for i in f:
        if i.strip().isdigit():
            digit_list.append(int(i.strip()))
            sum_digits += int(i.strip())
        f_list.append(i.strip())

print(f_list)
print(digit_list)
print(sum_digits)
