
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

all_brands = []  # Список всех брендов с повторяющимися
brands = []      # Список уникальных названий брендов
max_price = 0    
for item in items:
    brand = item.get("brand")
    if brands.count(brand) == 0:
        brands.append(brand)
    all_brands.append(brand)
    if item.get("price") > max_price:
        max_price = item.get("price")

# Найдите:
print("Товары на складе представлены брэндами: ")
print(brands)

# ТУТ ВОТ НЕ ПОНЯТНО!!!! Нужно посчитать каких name больше всего и вывести названия и бренды?
#                        Или посчитать каких brand больше всего? (тут реализованно именно это)
print("На складе больше всего товаров брэнда(ов): ")
max_count = 0
max_brand = []
for brand in brands:       # первый пробег определяет какие из названий брендов чаще всего повторяются
    count = all_brands.count(brand)
    if count > max_count:
        max_count = count

for brand in brands:       # второй пробег формирует список из чаще всего повторяющихся брендов
    if all_brands.count(brand) == max_count:
        max_brand.append(brand)
print(max_brand)

print("На складе самый дорогой товар брэнда(ов): ")
for item in items:
    if item.get("price") == max_price:
        print(item.get("brand"))
