# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
f = open("sold.txt", "r", encoding="UTF-8")
f_list = []
for line in f:
    line = line.split()
    f_list.extend(line)
    print(f_list)
# 1. На какую сумму было продано товаров
sum = 0
for el in f_list:
    sum += float(el)
print(sum)
# 2. Цену самого дорогого товара
expensive = 0
for el in f_list:
    if expensive < float(el):
        expensive = float(el)
print(expensive)
# 3. Цену самого дешевого товара
cheapest = float(f_list[0])
for el in f_list:
    if cheapest > float(el):
        cheapest = float(el)
print(cheapest)

f.close()
