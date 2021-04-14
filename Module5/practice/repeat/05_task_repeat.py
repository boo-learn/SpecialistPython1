# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def last_page(num_items, items_on_page):
    full_pages = num_items // items_on_page
    remainder = num_items - items_on_page * full_pages
    return remainder if remainder > 0 else items_on_page
