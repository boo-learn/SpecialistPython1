# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего

limerics = open('Data/limerics.txt', 'r', encoding='utf-8')

symbols_count = 0
block_count = 0
for line in limerics:
    print(line.strip())
    symbols_count += len(line.strip())
    if line == '\n':
        block_count += 1

print(symbols_count)
print(block_count +1)
