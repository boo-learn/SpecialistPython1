# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def pagination(num_items, items_on_page):
    pages = num_items % items_on_page
    return pages


objects = 1022
one_page_elements = 10

print(pagination(objects, one_page_elements))
