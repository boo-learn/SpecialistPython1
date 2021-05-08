# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего

f = open("data/limericks.txt", "r", encoding="utf-8")
# for line in f:
#     print(line.rstrip())
#
# print("=======================")

f.seek(0)
res = f.readlines()
line = " ".join(res)
spacers = [" ", "\n", "\t"]
for space in spacers:
    line = line.replace(space, "")
print(len(line))

f.seek(0)
count_limericks = 1
for line in f:
    if line.strip() == "":
        count_limericks += 1
print(count_limericks)
