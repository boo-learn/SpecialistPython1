# Дан словарь, содержащий данные о товаре из магазина
# "price" - цена товара в валюте "currency"
# "count" - количествотовара в магазине
# Считая,что курс доллара равен dollar_rate
# Вычислите цену всех товаров с названием "name" в долларах

item = {"name": "Кроссовки", "price": "7540.5", "currency": "rub", "count": "10"}
dollar_rate = 74.12

# TODO: your code here

print(f"Стоимость {item['name']} составляет {'{:.2f}'.format(float(item['price']) / dollar_rate * int(item['count']))}")
