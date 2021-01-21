# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
len_name = 0

for name in names:
    if len_name < len(name):
        len_name = len(name)

for name in names:
    if len_name == len(name):
        print(name)
        break
