# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

max_len = 0
longest_name = ""

for name in names:
    name_len = len(name)
    if name_len > max_len:
        max_len = name_len
        longest_name = name
        
print(longest_name)
