# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара

file = open('data/sold.txt', 'r', encoding='utf-8')

summa = 0
for line in file:
    line = line.strip().split()
    print(line)
    for new_line in line:
        summa += float(new_line)
print(summa)

file.close()
