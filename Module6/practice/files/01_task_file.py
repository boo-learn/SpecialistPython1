# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего

f = open("limericks.txt", "r", encoding="utf-8")
# 1
lines = f.readlines()

# 2
new_lines = ''
for line in lines:
    new_lines += line

for char in ' «»-—,?.!/;:\n':
    new_lines = new_lines.replace(char,'')

print(new_lines)
count = 0
for line in new_lines:
    count += 1
print(count)
