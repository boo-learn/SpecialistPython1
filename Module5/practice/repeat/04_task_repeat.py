# Напишите функцию принимающую общее количество объектов(например, товаров)
# которые нужно отобразить и количество объектов, которые нужно отобразить на каждой странице.
# Функция должна вычислять количество страниц для отображения всех объектов.

# Под пагинацией понимают показ ограниченной части информации на одной
# веб-странице и вывода списка остальных страниц.

def pagination(num_items, items_on_page):
    tf = num_items % item_on_page
    if num_items % item_on_page:
        num_pages = num_items // items_on_page +1
    else:
        num_pages = num_items // items_on_page
    return num_pages


num_items = 99
item_on_page = 10
print(pagination(num_items, item_on_page))
