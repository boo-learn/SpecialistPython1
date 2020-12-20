# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара
import os
path = os.path.join('Files', 'data/sold.txt')
sold = []

with open(path, 'r') as f:
    for line in f:
        sold = sold + line.split()

#print(sold)
sold_f = []
for el in sold:
    sold_f.append(float(el))

print(sum(sold_f))
print(max(sold_f))
print(min(sold_f))
