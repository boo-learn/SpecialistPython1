# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here
max_value = tup[0]
for t in tup:
    if t > max_value:
        max_value = t

print(max_value)
