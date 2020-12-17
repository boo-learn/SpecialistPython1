# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def pagination_tail(num_items, items_on_page):
    count_tail=num_items%items_on_page

    return count_tail

print(pagination_tail(99,10))
