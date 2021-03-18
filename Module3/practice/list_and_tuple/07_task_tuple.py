# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

el_max = 0
for el in tup:
    if el > el_max:
        el_max = el
print(el_max)

# TODO: your code here
