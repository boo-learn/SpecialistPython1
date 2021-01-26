# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

biggest_name = names[0]

for i in names:
    if len(i) > len(biggest_name):
        biggest_name = i

print(biggest_name)
