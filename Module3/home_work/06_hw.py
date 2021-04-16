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

brands = {}

for item in items:
    brand = item["brand"]
    amount = brands.get(brand, 0)
    amount += 1
    brands[brand] = amount

print("Товары на складе представлены брэндами: ")

print(list(brands.keys()))

print("На складе больше всего товаров брэнда(ов): ")

max_amount = 0
most_presented_brand = ""

for brand, amount in brands.items():
    if amount > max_amount:
        max_amount = amount
        most_presented_brand = brand

print(most_presented_brand)

print("На складе самый дорогой товар брэнда(ов): ")

max_price = 0
most_expensive_brand = ""

for item in items:
    price = item["price"]
    if price > max_price:
        max_price = price
        brand = item["brand"]
        most_expensive_brand = brand

print(most_expensive_brand)
