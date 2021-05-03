# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

max_len = 0

for i, name in enumerate(names):
    if len(name) > max_len:
        max_len = len(name)
        idx = i
print(names[idx])
