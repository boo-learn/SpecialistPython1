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
brands = {}
for item in items:
    brand_name = item["brand"]
    if not brand_name in brands.keys():
        brands[brand_name] = {"number_of_sku": 1, "max_price": item["price"]}
    else:
        brands[brand_name]["number_of_sku"] += 1
        if brands[brand_name]["max_price"] < item["price"]:
            brands[brand_name]["max_price"] = item["price"]

print(list(brands.keys()))


print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here
brand_of_max_sku = sorted(brands.items(), key=lambda kv: -kv[1]["number_of_sku"])[0]
max_num_of_sku = brand_of_max_sku[1]["number_of_sku"]
print(max_num_of_sku)

brands_of_max_sku = filter(lambda kv: kv[1]["number_of_sku"] == max_num_of_sku, brands.items())

print(list(brands_of_max_sku))


print("На складе самый дорогой товар брэнда(ов): ")

# TODO: your code here
brand_of_max_price = sorted(brands.items(), key=lambda kv: -kv[1]["max_price"])[0]
max_price = brand_of_max_price[1]["max_price"]
print(max_price)

brands_of_max_price = filter(lambda kv: kv[1]["max_price"] == max_price, brands.items())

print(list(brands_of_max_price))
