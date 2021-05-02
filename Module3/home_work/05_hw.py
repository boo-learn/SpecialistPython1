# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

name_length=0
for name in names:
    if len(name)>name_length:
        name_length=len(name)
for name in names:
    if len(name)==name_length:
        print(name)
