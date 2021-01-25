# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара

f = open('data\\solds.txt', 'r')

price_list = []
for line in f:
    price_list_txt = line.split()
    for price in price_list_txt:
        price_list.append(float(price))

print(price_list)
print(sum(price_list))
print(max(price_list))
print(min(price_list))
