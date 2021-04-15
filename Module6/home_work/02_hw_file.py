# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

with open("data/info.txt", "r") as f:
    import re

pattern = re.compile('[-]{0,1}[0-9]{1,}')
with open("data/info.txt", "r") as f:
    items = []
    for line in f:
        if pattern.findall(line.rstrip()):
            items.append(int(pattern.findall(line.rstrip())[0]))

print(items)
print(sum(items))
