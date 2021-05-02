# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
long_name = ""
for i in names:
    if len(i) > len(long_name):
        long_name = i
print(long_name)
