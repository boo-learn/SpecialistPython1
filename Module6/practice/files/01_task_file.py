# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара
t=False
while(t!=True):
    s=input('NxM')
    try:
        n=0
        m=0
        n=s[:s.find('x')]
        m=s[s.find('x')+1:]
        print(int(n)/int(m))
        t=True
    except ValueError:
        print('Format error')
