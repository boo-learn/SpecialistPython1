# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара
import sys

f = open("sold.txt", "r", encoding="utf-8")

s = 0
for line in f:
    goods = line.split(" ")
    for good in goods:
        s += float(good)
print(s)

f.seek(0)
max = 0
for line in f:
    goods = line.split(" ")
    for good in goods:
        if float(good) > max:
            max = float(good)
print(max)

f.seek(0)
min = sys.maxsize * 2 + 1
for line in f:
    goods = line.split(" ")
    for good in goods:
        if float(good) < min:
            min = float(good)
print(min)

f.close()
