# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара
f = open('data/sold.txt', 'r', encoding='utf-8')


sold_items = []
for line in f.readlines():
    line_x = line.rstrip().split(' ')
    for item in line_x:
        sold_items.append(float(item))
total = 0
min_sold = sold_items[0]
max_sold = 0
for item in sold_items:
    total += item
    if item < min_sold:
        min_sold = item
    if item > max_sold:
        max_sold = item

print(sold_items)
print(f'Сумма товаров = {total}, макс.стоимость = {max_sold}, мин.стоимость = {min_sold}')

f.close()
