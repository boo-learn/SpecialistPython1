# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день

f = open('data\\items_sold.txt', "r", encoding="utf-8")

market_dict = {}
for line in f:
    element = line.split()
    for el in element:
        el_list = el.split(':')
        if market_dict.get(el_list[0]) == None:
            market_dict[el_list[0]] = float(el_list[1])
        else:
            market_dict[el_list[0]] += float(el_list[1])

print("Общая выручка: " + str(sum(market_dict.values())))
for el in market_dict:
    print(el, ":", market_dict[el])
    
max_val = max(market_dict.values())
print("Товары с максимальной ценой: ")
for el in market_dict:
    if market_dict[el] == max_val:
        print(el)

print("Всего разных товаров: ", len(market_dict))

