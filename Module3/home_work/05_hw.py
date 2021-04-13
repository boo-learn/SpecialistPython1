# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
# Вариант 1
max_name = names[0]
for el in names:
    if len(el) > len(max_name):
        max_name = el
print(max_name)

# Вариант 2 (в стиле R)
word_len = list(map(len, names))
print(names[word_len.index(max(word_len))])
