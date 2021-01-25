# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего

in_file = open('data\\limerics.txt', 'r', encoding="utf-8")

all_lines = []
for line in in_file:
   all_lines.append(line)
   print(line)

non_space = 0
for line in all_lines:
    non_space += len(line) - line.count(' ')

print(non_space)

poem_num = 1
for line in all_lines:
    if line[0] == '\n':
        poem_num += 1

print(poem_num)
