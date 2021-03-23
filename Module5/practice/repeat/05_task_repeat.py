# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def num_of_items_on_last_page(num_items, items_on_page):
    return items_on_page if num_items % items_on_page == 0 else num_items % items_on_page


print(num_of_items_on_last_page(8, 4))
print(num_of_items_on_last_page(7, 4))
