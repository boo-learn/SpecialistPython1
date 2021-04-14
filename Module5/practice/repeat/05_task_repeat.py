# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def pagination(num_items, items_on_page):
    import math
    return math.ceil(num_items / items_on_page)


all_items = 121
items_page = 20

print('На последней странице:', all_items - (pagination(all_items, items_page) - 1) * items_page, 'объект(ов)')
