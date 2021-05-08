# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.
def last_page(num_items, items_on_page):
    if num_items%items_on_page==0:
        return 0
    else:
        return num_items%items_on_page
