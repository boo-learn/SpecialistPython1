# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара
import os
import settings

cass_bill_file = os.path.join(settings.BASE_DIR, 'files', 'sold.txt')
with open(cass_bill_file) as f:
    s = 0
    for line in f:
        s += sum(map(float, line.split()))
print(s)
