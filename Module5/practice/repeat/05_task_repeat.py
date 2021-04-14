# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def count_items_last_page(num_item, page_item):
    if num_item % page_item == 0:
        return page_item
    return num_item % page_item
