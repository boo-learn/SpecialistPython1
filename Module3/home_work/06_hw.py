# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

# TODO: your code here
brands = set()
for el in items:
    brands.add(el.get('brand'))
print(', '.join(brands))

print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here
# brand_list = []
# for item in items:
#     brand_list.append(item.get('brand'))
# print(brand_list)
# count_list = []
# for item in brand_list:
#     count_list.append(brand_list.count(item))
# print(count_list)

print("На складе самый дорогой товар брэнда(ов): ")

# TODO: your code here
max_price = items[0]['price']
top_cost_brand = ''
for item in items:
    if item.get('price') > max_price:
        max_price = item.get('price')
        top_cost_brand = item.get('brand')
print(top_cost_brand)
