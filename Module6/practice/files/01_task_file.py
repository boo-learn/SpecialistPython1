# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего

f = open("data/limerics.txt", "r", encoding="UTF-8")


for line in f:
    print(line.rstrip())

f.seek(0)
total = 0
for line in f:
    total += len(line.strip().replace(' ', ''))

print(f'Кол-во не пробельных символов {total}')

f.seek(0)
total = 1
for line in f:
    if line == '\n':
        total += 1
print(f'Кол-во стихотворений {total}')





