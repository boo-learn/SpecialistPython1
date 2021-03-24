# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельных символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего

# 1. Вывод содержимого файла в консоль


f = open("limericks.txt", "r", encoding="utf-8")

for line in f:
    print(line.rstrip())

# 2. Подсчёт количества непробельных символов в файле


f = open("limericks.txt", "r", encoding="utf-8")

i = 0
char = ""
for char in f:
    if not(char.isspace()):
        i += 1

print("Non-spaces count: ", i)

# 3. Подсчёт количества стихотворений

f = open("limericks.txt", "r", encoding="utf-8")

i = 0
for line in f:
    if line.isspace():
        i += 1

print("Strings count: ", i+1)
