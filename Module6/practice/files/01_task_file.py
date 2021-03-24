# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего
f = open("data1/my_file.txt", "r", encoding="utf-8")
#for line in f:
#    print(line.rstrip())

sum = 0
lim= 0
for line in f:
    print(line.rstrip())
    if line.strip() == "":
        lim += 1
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    sum += len(line)

print(sum)
print(lim + 1)
