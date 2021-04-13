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
brands = []
for el in items:
    if el["brand"] not in brands:
        brands.append(el["brand"])
print(brands)

print("На складе больше всего товаров брэнда(ов): ")
count_brands = [el["brand"] for el in items]
count=[]
for el in brands:
    count.append((count_brands.count(el), el))
print(max(count))

print("На складе самый дорогой товар брэнда(ов): ")
item=items[0]
for el in items:
    if el["price"]>item["price"]:
        item=el
print(item)
