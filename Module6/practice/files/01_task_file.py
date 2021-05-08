# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего

f = open("limericks.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())

f.seek(0)
count = 0
for line in f:
    line = line.strip()
    for ch in line:
        if ch != " ":
            count += 1
print(count)

f.seek(0)
count = 0
for line in f:
    if line == "\n":
        count += 1
print(count + 1)

f.close()
