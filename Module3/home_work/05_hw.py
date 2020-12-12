# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

max_name_len = len(names[0])
for name in names:
    if len(name) >= max_name_len:
        max_name_len = len(name)
        max_name = name
print(max_name)
