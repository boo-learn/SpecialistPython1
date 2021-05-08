# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день
f = open('items_sold.txt', 'r', encoding='utf-8' )

dict = {}
for line in f:
    lst = line.split()
    for part in lst:
        lst2 = part.split(':')
        price = float(lst2[1])
        try:
            dict[lst2[0]].append(price)
        except:
            dict[lst2[0]] = [price]
print(f'Всего типов товаров: {len(dict)}')

all_sum = 0
max_tov 
for k in dict.keys():
    sum_gr_tov = sum(dict[k])
    all_sum += sum(dict[k])
    print(f'Товар: {k}, выручка: {round(sum_gr_tov, 2)}')
print(f'Выручка за день: {all_sum}')
