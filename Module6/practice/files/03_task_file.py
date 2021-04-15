# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день
f_data = open("data/items_sold.txt", "r", encoding="utf-8")
dic_sales = {}
for line in f_data:
    sales = line.split(sep=" ")
    for sale in sales:
        pair = sale.split(sep=":")
        if pair[0] in dic_sales:
            dic_sales[pair[0]] += float(pair[1])
        else:
            dic_sales[pair[0]] = float(pair[1])

print("total: ", sum(dic_sales.values()))

print("sum by item: ", dic_sales)

max_sum = sorted(dic_sales.values(), key=lambda x: -x)[0]
print("items of max sum: ", list( filter(lambda kv: kv[1] == max_sum, dic_sales.items()) ) )

print("item count: ", len(dic_sales))
