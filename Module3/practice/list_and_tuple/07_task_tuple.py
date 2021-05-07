# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)
max_el = 0

for el in tup:
    if el > max_el:
        max_el = el
print(max_el)
