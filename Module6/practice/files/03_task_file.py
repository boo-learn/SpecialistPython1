# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день

f = open("items_sold.txt", "r", encoding="utf-8")

d = {}
for line in f:
    items = line.split(" ")
    for item in items:
        tokens = item.split(":")
        if d.get(tokens[0]) is None:
            d[tokens[0]] = []
        val = d[tokens[0]]
        val.append(float(tokens[1]))
        d[tokens[0]] = val

f.close()

s = 0
for _, val in d.items():
    for el in val:
        s += el
print(s)

print()

items_val = []
for key, val in d.items():
    s = 0
    for el in val:
        s += el
    items_val.append((key, s))
    print(f"{key}: {s:.2f}")

print()

max_it = ["", 0]
for el in items_val:
    if el[1] > max_it[1]:
        max_it = el
print(max_it[0])

print()

print(len(d.keys()))
