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

brands = []
for good in items:
    brand = good["brand"]
    if brand not in brands:
        brands.append(brand)

print("Товары на складе представлены брэндами: ", ", ".join(brands))

brands = []
max_brands = 0
for good in items:
    brand = good["brand"]
    brands.append(brand)
    if brand in brands:
        max_brands

brands_count = {}
for brand in brands:
    brands_count[brand] = 0

for good in items:
    brand = good["brand"]
    brands_count[brand] += 1
max_items_per_brand = max(brands_count.values())

top_brands = []
for brand, count in brands_count.items():
    if count == max_items_per_brand:
        top_brands.append(brand)

print("На складе больше всего товаров брэнда(ов): ", ", ".join(top_brands))

max_price = 0
for good in items:
    price = good["price"]
    if price > max_price:
        max_price = price

max_brands = []
for good in items:
    price = good["price"]
    if price == max_price:
        max_brands.append(good["brand"])

print("На складе самый дорогой товар брэнда(ов): ", ", ".join(max_brands))

