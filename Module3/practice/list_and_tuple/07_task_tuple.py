# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here
max_i = tup[1]
for i in tup:
    if max_i < i:
        max_i = i

print(max_i)
