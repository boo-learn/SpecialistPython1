# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

long_name = max(len(name) for name in names)

for name in names:
    if len(name) == long_name:
        k = name

print(k)
        

