# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

max_len = 0
max_name = ''

for el in names:
    if len(el) > max_len:
        max_len = len(el)
        max_name = el

print(max_name)
