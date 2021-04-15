# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день
f = open('items_sold.txt', 'r', encoding='utf-8')
solid = {}
for line in f:
    bufer = line.strip().split(' ')
    for buf in bufer:
        key, sol = buf.split(':')
        if key in solid:
            solid[key] += float(sol)
        else:
            solid[key] = float(sol)
f.close()

print('общая выручка магазина:', sum(solid.values()))

print('выручка магазина по каждому типу товаров:')
max_price = 0
max_item = ''
for item in solid:
    print(f'{item} = {solid[item]:.2f}')
    if solid[item] > max_price:
        max_price = solid[item]
        max_item = item

print('тип товара был продан на самую большую сумму:', max_item)

print('различных типов товаров было продано за день:', len(solid.keys()))
