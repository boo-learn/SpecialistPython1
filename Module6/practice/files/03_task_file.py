# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день
f = open('data/items_sold.txt', 'r', encoding='utf-8')

items_sold = {}
for line in f:
    for item in line.strip().split():
        val = item.split(':')
        if items_sold.get(val[0]) is None:
            items_sold[val[0]] = float(val[1])
        else:
            items_sold[val[0]] += float(val[1])

print(items_sold)

max_sold = max(items_sold.values())
key_max_sold = ''
for key, item in items_sold.items():
    if item == max_sold:
        key_max_sold = key

print(f'Товар на самую большую сумму: {key_max_sold}')

print(f'Кол-во типов товаров: {len(items_sold.keys())}')

f.close()
