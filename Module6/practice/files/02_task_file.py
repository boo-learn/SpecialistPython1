# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара
f_sold = open("data/sold.txt", "r", encoding="utf-8")
lst_prices= []
for line in f_sold:
    prices = line.split(sep=" ")
    for price in prices:
        lst_prices.append((float(price)))
f_sold.close()
print("total = ", sum(lst_prices))
print("max price = ", max(lst_prices))
print("min price = ", min(lst_prices))
