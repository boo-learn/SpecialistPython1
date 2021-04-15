# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего
f_lim_read = open("data/limericks.txt", "r", encoding="utf-8")
symbs = 0
lims = 0
for line in f_lim_read:
    print(line.rstrip())
    symbs += len(line.replace(" ","").replace("\n", "").replace("\t",""))
    if line.strip() == "": lims += 1
print(symbs, lims+1)
f_lim_read.close()
