# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
max_len = 0
big_name = ''
for name in names:
    if max_len < len(name):
        max_len = len(name)

for name in names:
    if max_len == len(name):
        big_name = name

print(big_name)
