# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара
f = open("data1/my_file.txt", "r", encoding="utf-8")
costs_str = []
for line in f:
    costs_str += line.split()
costs = []
for el in costs_str:
    costs.append(float(el))

print(sum(costs))
print(min(costs))
print(max(costs))
f.close()
