# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего
f = open('data/limericks.txt', 'r', encoding='utf-8')
simbols = 0
poem_count = 0
for line in f:
    for s in line:
        if not s.isspace():
            simbols += 1
        elif line[0] == '\n':
            poem_count += 1
            simbols += 1
print()
print(f'Непробельных символов: {simbols}')
print(f'Стихотворений: {poem_count + 1}')
