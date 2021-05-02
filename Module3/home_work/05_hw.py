# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них
# TODO: your code here
names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
max_len_name = 0
index = 0
for name in names:
    if len(name) > max_len_name:
        max_len_name = len(name)
        max_name = name
print(max_name, f' - длина имени {max_len_name}')
