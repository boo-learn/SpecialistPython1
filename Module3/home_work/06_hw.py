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

brands = []
for item in items:
    brands.append(item["brand"])
brands_short = []
for brand in brands:
    if brand not in brands_short:
        brands_short.append(brand)
for el in brands_short:
    print(el)

print("На складе больше всего товаров брэнда(ов): ")
brands_count = {brand: brands.count(brand) for brand in brands}
count_max = 0
brand_count_max = []
for brand in brands_short:
    if brands_count[brand] > count_max:
        brand_count_max.append(brand)
for brand in brands_short:
    if brands_count[brand] == count_max:
        brand_count_max.append(brand)
for brand in brand_count_max:
    print(brand)

print("На складе самый дорогой товар брэнда(ов): ")
brand_prices = {}
for item in items:
    brand_prices[item["price"]] = item["brand"]
prices = brand_prices.keys()
max_price = max(prices)
max_prices = []
for price in prices:
    if price == max_price:
        max_prices.append(brand_prices[price])
for el in max_prices:
    print(el)
