# Напишите функцию принимающую общее количество объектов(например, товаров)
# которые нужно отобразить и количество объектов, которые нужно отобразить на каждой странице.
# Функция должна вычислять количество страниц для отображения всех объектов.

# Под пагинацией понимают показ ограниченной части информации на одной
# веб-странице и вывода списка остальных страниц.

def pagination(num_items, items_on_page):
    if num_items <= items_on_page:
        page_count = 1
    elif (num_items%items_on_page) != 0:
        page_count = (num_items // items_on_page) + 1
    else:
        page_count = num_items / items_on_page

    return page_count
