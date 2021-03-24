# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл,
# наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара

f = open("data//sold.txt", "r", encoding="utf-8")

prices = []
for line in f:
    prices += line.split()

prices_num = []
for el in prices:
    prices_num.append(float(el))

print(prices)
print(prices_num)

# 1. На какую сумму было продано товаров

print("Prices sum: ", sum(prices_num))

# 2. Цена самого дорогого товара

print("Maximum price: ", max(prices_num))

# 3. Цена самого дешевого товара

print("Maximum price: ", min(prices_num))

f.close()
