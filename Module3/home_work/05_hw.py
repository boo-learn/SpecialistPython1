# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр",]

# TODO: your code here

max_len = len(names[0])
biggest_name = ''
for el in names:
    if len(el) > max_len:
        max_len=len(el)
        biggest_name = el
print(biggest_name)
