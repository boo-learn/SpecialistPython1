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
        "price": 4800
    },
    {
         "name": "Носки",
         "brand": "reebok",
         "price": 4800
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

brands = []
for item in items:
    brands.append(item["brand"])
for brand in brands[:]:
    if brands.count(brand) > 1:
        brands.remove(brand)

print(brands)

print("\nНа складе больше всего товаров брэнда(ов): ")

brands = []
for item in items:
    brands.append(item["brand"])
max_brand = []
count = brands.count(brands[0])
for brand in brands:
    if brands.count(brand) > count:
        max_brand.clear()
        max_brand.append(brand)
        count = brands.count(brand)
    elif brands.count(brand) == count:
        if max_brand.count(brand) == 0:
            max_brand.append(brand)

print(max_brand)

print("\nНа складе самый дорогой товар брэнда(ов): ")

max_item = items[0]
max_price_brand = []
for item in items:
    if item["price"] > max_item["price"]:
        max_price_brand.clear()
        max_item = item
        max_price_brand.append(item["brand"])
    elif item["price"] == max_item["price"]:
        if max_price_brand.count(item["brand"]) == 0:
            max_price_brand.append(item["brand"])

print(max_price_brand)
