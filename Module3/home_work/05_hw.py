# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
length = 0
long_names = []
for name in names:
    if len(name) >= length:
        long_names.append(name)
        length = len(name)
print(long_names[-1])
