# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день
f = open("data\items_sold.txt", "r", encoding="utf-8")

sold_sum = 0
bill = []
product = set()
product_sold_sum = []
product_max_price = 0
product_max_price_name = ''


for line in f:
     line = line.split()
     for obj in line:
         pos = obj.split(":")
         bill.append(dict(key=pos[0], value=pos[1]))
for el in bill:
    sold_sum += float(el['value'])
    product.add(el['key'])

for el1 in product:
    i = {}
    prd_sum = 0
    for pos in bill:
        if pos['key'] == el1:
            prd_sum += float(pos['value'])
            i = {'key': pos['key'], 'value': prd_sum}
    product_sold_sum.append(i)


print("total sold:",sold_sum)

print("\nproduct - total sold count:")
for el in product_sold_sum:
    print(el['key'], "-", el['value'])
for el in product_sold_sum:
    if el['value'] > product_max_price:
        product_max_price = el['value']
        product_max_price_name = el['key']

print("\nmax sold for -", product_max_price_name)

print("\ntotal product amount:", len(product))
