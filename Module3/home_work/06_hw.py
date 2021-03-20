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

unique_brands = []
for elem in items:
    if elem.get("brand") not in unique_brands:
        unique_brands.append(elem.get("brand"))

print("Товары на складе представлены брэндами:", ', '.join(unique_brands))

all_brands = []
for elem in items:
    all_brands.append(elem.get("brand"))

brands_count = {}
for brand in unique_brands:
    brands_count[brand] = all_brands.count(brand)

max_count = 0
for brand in unique_brands:
    if brands_count.get(brand) >= max_count:
        max_count = brands_count.get(brand)


for brand in unique_brands:
    if brands_count.get(brand) < max_count:
        brands_count.pop(brand)

print("На складе больше всего товаров брэнда(ов):", ', '.join(brands_count.keys()))
print("Количество:", max_count, "шт")

brands_price = []
max_price = 0
for elem in items:
    if elem.get("price") >= max_price:
        max_price = elem.get("price")
        brands_price.append(elem)

brands_price_copy = brands_price.copy()
for item in brands_price:
    if item.get("price") < max_price:
        brands_price_copy.remove(item)

print("На складе самый дорогой товар брэнда(ов):")

for elem in brands_price_copy:
    print(elem.get("brand"))
    print("Наименование товара -", elem.get("name"))

print("Цена:", max_price)
