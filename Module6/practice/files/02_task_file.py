# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара

f = open("data\sold.txt", "r", encoding="utf-8")

sold_sum = 0
prices = []

for line in f:
    line = line.split()
    for num in line:
        prices.append(float(num))

min_sold_price = prices[0]
max_sold_price = prices[0]

for price in prices:
    if price < min_sold_price:
        min_sold_price = price
    if price > max_sold_price:
        max_sold_price = price
    sold_sum += 1

print("expensive:", max_sold_price)
print("cheap:", min_sold_price)
print("total sold:",sold_sum)
