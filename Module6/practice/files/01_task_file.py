# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего

f = open("data/limericks.txt", "r", encoding="utf-8")
sym_count = 0
lick_count = 0


for line in f:
    if line == "\n":
        lick_count += 1
    for char in line:
        if char != " " and char != "\n":
            sym_count += 1

    print(line.rstrip())  # 1.
print("")
print("Число символов в файле -", sym_count) # 2.
print("Число стихотворений -", lick_count)  # 3.
