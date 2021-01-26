# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

big_name = names[0]

for name in names:
    if len(name) > len(big_name):
        big_name = name

print(big_name)
