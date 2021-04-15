# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего
f = open('limericks.txt', 'r', encoding='utf-8')
simbol = 0
verse = 0
for line in f:
    print(line.rstrip())
    if line.isspace():
        verse += 1
    else:
        simbol += len(line.strip().replace(' ', ''))
print('Стихов: ', verse + 1)
print('Не пробельных символов:', simbol)
