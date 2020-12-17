# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.
num_items = 99
item_on_page = 10
items_on_last_page = num_items % item_on_page
print(items_on_last_page, 'elements shown on the last page' )
