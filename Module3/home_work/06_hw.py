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

brand_name =[]
for br in items:
    brand = br["brand"]
    brand_name.append(brand)
for brand in brand_name.copy():
    if brand_name.count(brand) != 1:
        brand_name.remove(brand)
print(brand_name)

print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here 

print("На складе самый дорогой товар брэнда(ов): ")

biggest_price = items[0]["price"]
hight_price = {}

for br in items:
    pr = br['price']
    if pr > biggest_price:
        biggest_price = pr
        hight_price = br

print("Самый дорогой товар бренда:", hight_price["brand"])
