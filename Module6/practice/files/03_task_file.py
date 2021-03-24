# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день
f = open("data/items_sold.txt", "r", encoding="utf-8")

items_list = []
for line in f:
    items_list += line.split()

items_dict = {}
for el in items_list:
    pair = el.split(":")
    if items_dict.get(pair[0]):
        items_dict[pair[0]] += float(pair[1])
    else:
        items_dict[pair[0]] = float(pair[1])

# print(items_list)

# 1. Какова общая выручка магазина
total = sum(items_dict.values())

# 2. Какова выручка магазина по каждому типу товаров
# print(items_dict)

# 3. Какой тип товара был продан на самую большую сумму
max_prod = max(items_dict, key=items_dict.get)

# 4. Сколько различных типов товаров было продано за день
unique_prod = set(items_list)

print(f"1_total={total}\n2_prod_type:{items_dict}\n3_max_prod={max_prod}\n4_unique_prod:{unique_prod}")
