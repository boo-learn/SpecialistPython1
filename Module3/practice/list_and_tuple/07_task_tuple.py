# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

max_el = -float("inf")
for el in tup:
    if max_el < el:
        max_el = el

print("Max:", max_el)
