# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def pagination_last_page (num_items, items_on_page):
    if num_items % items_on_page == 0:
        return(items_on_page)
    else:
        return (num_items % items_on_page)

print('Pages:', pagination_last_page (20,10))
