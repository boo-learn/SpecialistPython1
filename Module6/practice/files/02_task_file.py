# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара
f = open('sold.txt', 'r', encoding='utf-8' )
sum = 0
max_price = 0
for line in f:
    lst = line.split(' ')
    if sum == 0:
        min_price = float(lst[0])
    for price in lst:
        price = float(price)
        sum += price
        if price > max_price:
            max_price = price
        if price < min_price:
            min_price = price
f.close()
print(f'all_sum {sum}, max_price {max_price}, min_price {min_price}')
